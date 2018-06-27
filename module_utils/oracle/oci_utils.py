# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import logging
import logging.config
import os
import tempfile
from datetime import datetime

import oci
import yaml

from oci.constants import HEADER_NEXT_PAGE
from oci.exceptions import InvalidConfig, InvalidPrivateKey, MissingPrivateKeyPassphrase, ConfigFileNotFound, \
    ServiceError, MaximumWaitTimeExceeded
from oci.identity.identity_client import IdentityClient
from oci.object_storage.models import CreateBucketDetails
from oci.object_storage.models import UpdateBucketDetails
from oci.retry import RetryStrategyBuilder
from oci.util import to_dict, Sentinel

from ansible.module_utils.basic import _load_params

__version__ = '0.15.0'

MAX_WAIT_TIMEOUT_IN_SECONDS = 1200

# If a resource is in one of these states it would be considered inactive
DEAD_STATES = ["TERMINATING", "TERMINATED", "FAULTY", "FAILED", "DELETING", "DELETED", "UNKNOWN_ENUM_VALUE",
               "DETACHING", "DETACHED"]

# If a resource is in one of these states it would be considered available
DEFAULT_READY_STATES = ["AVAILABLE", "ACTIVE", "RUNNING", "PROVISIONED", "ATTACHED", "ASSIGNED"]

# If a resource is in one of these states, it would be considered deleted
DEFAULT_TERMINATED_STATES = ["TERMINATED", "DETACHED", "DELETED"]


def get_common_arg_spec(supports_create=False, supports_wait=False):
    """
    Return the common set of module arguments for all OCI cloud modules.
    :param supports_create: Variable to decide whether to add options related to idempotency of create operation.
    :param supports_wait: Variable to decide whether to add options related to waiting for completion.
    :return: A dict with applicable module options.
    """
    common_args = dict(
        config_file_location=dict(type='str', required=False),
        config_profile_name=dict(type='str', required=False, default="DEFAULT"),
        api_user=dict(type='str', required=False),
        api_user_fingerprint=dict(type='str', required=False, no_log=True),
        api_user_key_file=dict(type='str', required=False),
        api_user_key_pass_phrase=dict(type='str', required=False, no_log=True),
        tenancy=dict(type='str', required=False),
        region=dict(type='str', required=False)
    )

    if supports_create:
        common_args.update(key_by=dict(type='list', required=False),
                           force_create=dict(type='bool', required=False, default='no'))

    if supports_wait:
        common_args.update(wait=dict(type='bool', required=False, default=True),
                           wait_timeout=dict(type='int', required=False, default=MAX_WAIT_TIMEOUT_IN_SECONDS),
                           wait_until=dict(type='str', required=False))

    return common_args


def get_oci_config(module):
    """Return the OCI configuration to use for all OCI API calls. The effective OCI configuration is derived by merging
    any overrides specified for configuration attributes through Ansible module options or environment variables. The
    order of precedence for deriving the effective configuration dict is:
    1. If a config file is provided, use that to setup the initial config dict.
    2. If a config profile is specified, use that config profile to setup the config dict.
    3. For each authentication attribute, check if an override is provided either through
        a. Ansible Module option
        b. Environment variable
        and override the value in the config dict in that order."""
    config = None

    try:
        config_file = module.params.get('config_file_location')
        _debug("Config file through module options - {} ".format(config_file))
        if not config_file:
            if 'OCI_CONFIG_FILE' in os.environ:
                config_file = os.environ['OCI_CONFIG_FILE']
                _debug("Config file through OCI_CONFIG_FILE environment variable - {}".format(config_file))
            else:
                config_file = "~/.oci/config"
                _debug("Config file (fallback) - {} ".format(config_file))

        config_profile = module.params.get('config_profile_name')
        if not config_profile:
            if 'OCI_CONFIG_PROFILE' in os.environ:
                config_profile = os.environ['OCI_CONFIG_PROFILE']
            else:
                config_profile = "DEFAULT"

        config = oci.config.from_file(file_location=config_file, profile_name=config_profile)
        config["additional_user_agent"] = "Oracle-Ansible/{}".format(__version__)

        # Merge any overrides through other IAM options
        _merge_auth_option(config, module, module_option_name="api_user", env_var_name="OCI_USER_ID",
                           config_attr_name="user")
        _merge_auth_option(config, module, module_option_name="api_user_fingerprint",
                           env_var_name="OCI_USER_FINGERPRINT", config_attr_name="fingerprint")
        _merge_auth_option(config, module, module_option_name="api_user_key_file",
                           env_var_name="OCI_USER_KEY_FILE", config_attr_name="key_file")
        _merge_auth_option(config, module, module_option_name="api_user_key_pass_phrase",
                           env_var_name="OCI_USER_KEY_PASS_PHRASE", config_attr_name="pass_phrase")
        _merge_auth_option(config, module, module_option_name="tenancy",
                           env_var_name="OCI_TENANCY", config_attr_name="tenancy")
        _merge_auth_option(config, module, module_option_name="region",
                           env_var_name="OCI_REGION", config_attr_name="region")
    except (ConfigFileNotFound, InvalidConfig, InvalidPrivateKey,
            MissingPrivateKeyPassphrase) as ex:
        module.fail_json(msg=ex.args)

    return config


def _merge_auth_option(config, module, module_option_name, env_var_name, config_attr_name):
    """Merge the values for an authentication attribute from ansible module options and
    environment variables with the values specified in a configuration file"""
    _debug("Merging {}".format(module_option_name))

    auth_attribute = module.params.get(module_option_name)
    _debug("\t Ansible module option {} = {}".format(module_option_name, auth_attribute))
    if not auth_attribute:
        if env_var_name in os.environ:
            auth_attribute = os.environ[env_var_name]
            _debug("\t Environment variable {} = {}".format(env_var_name, auth_attribute))

    # An authentication attribute has been provided through an env-variable or an ansible
    # option and must override the corresponding attribute's value specified in the
    # config file [profile].
    if auth_attribute:
        _debug("Updating config attribute {} -> {} ".format(config_attr_name, auth_attribute))
        config.update({config_attr_name: auth_attribute})


def bucket_details_factory(bucket_details_type, module):
    bucket_details = None
    if bucket_details_type == "create":
        bucket_details = CreateBucketDetails()
    elif bucket_details_type == "update":
        bucket_details = UpdateBucketDetails()

    bucket_details.compartment_id = module.params['compartment_id']
    bucket_details.name = module.params['name']
    bucket_details.public_access_type = module.params['public_access_type']
    bucket_details.metadata = module.params['metadata']

    return bucket_details


def list_all_resources(target_fn, **kwargs):
    """
    Return all resources after paging through all results returned by target_fn.
    :param target_fn: The target OCI SDK paged function to call
    :param kwargs: All arguments that the OCI SDK paged function expects
    :return: List of all objects returned by target_fn
    :raises ServiceError: When the Service returned an Error response
    :raises MaximumWaitTimeExceededError: When maximum wait time is exceeded while invoking target_fn
    """
    existing_resources = None
    response = call_with_backoff(target_fn, **kwargs)
    existing_resources = response.data
    while response.has_next_page:
        kwargs.update(page=response.headers.get(HEADER_NEXT_PAGE))
        response = call_with_backoff(target_fn, **kwargs)
        existing_resources += response.data
    return existing_resources


def _debug(s):
    get_logger("oci_utils").debug(s)


def get_logger(module_name):
    oci_logging = setup_logging()
    return oci_logging.getLogger(module_name)


def setup_logging(default_config_file='/etc/ansible/oci_logging.yaml', default_level="INFO",
                  default_log_path=tempfile.gettempdir()):
    """Setup logging configuration"""
    env_config_file = 'LOG_CONFIG'
    env_log_path = 'LOG_PATH'
    env_log_level = 'LOG_LEVEL'

    config_file = os.getenv(env_config_file, default_config_file)
    log_path = os.getenv(env_log_path, default_log_path)

    files_handlers = ['debug_file_handler',
                      'error_file_handler', 'info_file_handler']

    if os.path.exists(config_file):
        with open(config_file, 'rt') as f:
            config = yaml.safe_load(f.read())
            for files_handler in files_handlers:
                config["handlers"][files_handler]["filename"] \
                    = config["handlers"][files_handler]["filename"] \
                    .format(path=log_path, date=datetime.today().strftime('%d-%m-%Y'))
        logging.config.dictConfig(config)
    else:
        log_level_str = os.getenv(env_log_level, default_level)
        log_level = logging.getLevelName(log_level_str)

        log_file_path = os.path.join(tempfile.gettempdir(), 'oci_ansible_module.log')

        logging.basicConfig(filename=log_file_path,
                            filemode='a', level=log_level)
    return logging


def check_and_update_attributes(target_instance, attr_name, input_value, existing_value, changed):
    if input_value is not None and input_value != existing_value:
        changed = True
        target_instance.__setattr__(attr_name, input_value)
    else:
        target_instance.__setattr__(attr_name, existing_value)
    return changed


def check_and_update_resource(resource_type, get_fn, kwargs_get, update_fn, primitive_params_update,
                              kwargs_non_primitive_update, module, update_attributes):
    """
    This function handles update operation on a resource. It checks whether update is required and accordingly returns
    the resource and the changed status.
    :param resource_type: The type of the resource. e.g. "private_ip"
    :param get_fn: Function used to get the resource. e.g. virtual_network_client.get_private_ip
    :param kwargs_get: Dictionary containing the arguments to be used to call get function.
           e.g. {"private_ip_id": module.params["private_ip_id"]}
    :param update_fn: Function used to update the resource. e.g virtual_network_client.update_private_ip
    :param primitive_params_update: List of primitive parameters used for update function. e.g. ['private_ip_id']
    :param kwargs_non_primitive_update: Dictionary containing the non-primitive arguments to be used to call get
     function with key as the non-primitive argument type & value as the name of the non-primitive argument to be passed
     to the update function. e.g. {UpdatePrivateIpDetails: "update_private_ip_details"}
    :param module: Instance of AnsibleModule
    :param update_attributes: Attributes in update model.
    :return: Returns a dictionary containing the "changed" status and the resource.
    """
    try:
        result = dict(changed=False)
        resource = call_with_backoff(get_fn, **kwargs_get).data

        attributes_to_update = []
        for attr in update_attributes:
            resources_attr_value = getattr(resource, attr, None)
            user_provided_attr_value = module.params.get(attr, None)
            if resources_attr_value != user_provided_attr_value:
                # only update if the user has explicitly provided a value for this attribute
                # otherwise, no update is necessary because the user hasn't expressed a particular
                # value for that attribute
                if has_user_provided_value_for_option(module, attr):
                    attributes_to_update.append(attr)

        if attributes_to_update:
            kwargs_update = dict()
            for param in primitive_params_update:
                kwargs_update[param] = module.params[param]
            for param in kwargs_non_primitive_update:
                update_object = param()
                for key in update_object.attribute_map:
                    if key in attributes_to_update:
                        setattr(update_object, key, module.params[key])

                kwargs_update[kwargs_non_primitive_update[param]] = update_object
            resource = call_with_backoff(update_fn, **kwargs_update).data
            result['changed'] = True
        result[resource_type] = to_dict(resource)
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def get_taggable_arg_spec(supports_create=False, supports_wait=False):
    """
    Returns an arg_spec that is valid for taggable OCI resources.
    :return: A dict that represents an ansible arg spec that builds over the common_arg_spec and adds free-form and
    defined tags.
    """
    tag_arg_spec = get_common_arg_spec(supports_create, supports_wait)
    tag_arg_spec.update(dict(
        freeform_tags=dict(type='dict'),
        defined_tags=dict(type='dict')
    ))
    return tag_arg_spec


def add_tags_to_model_from_module(model, module):
    """
    Adds free-form and defined tags from an ansible module to a resource model
    :param model: A resource model instance that supports 'freeform_tags' and 'defined_tags' as attributes
    :param module: An AnsibleModule representing the options provided by the user
    :return: The updated model class with the tags specified by the user.
    """
    freeform_tags = module.params.get('freeform_tags', None)
    defined_tags = module.params.get('defined_tags', None)
    return add_tags_to_model_class(model, freeform_tags, defined_tags)


def add_tags_to_model_class(model, freeform_tags, defined_tags):
    """
    Add free-form and defined tags to a resource model.
    :param model:  A resource model instance that supports 'freeform_tags' and 'defined_tags' as attributes
    :param freeform_tags:  A dict representing the freeform_tags to be applied to the model
    :param defined_tags: A dict representing the defined_tags to be applied to the model
    :return: The updated model class with the tags specified by the user
    """
    try:
        if freeform_tags is not None:
            _debug("Model {} set freeform tags to {}".format(model, freeform_tags))
            model.__setattr__("freeform_tags", freeform_tags)

        if defined_tags is not None:
            _debug("Model {} set defined tags to {}".format(model, defined_tags))
            model.__setattr__("defined_tags", defined_tags)
    except AttributeError as ae:
        _debug("Model {} doesn't support tags. Error {}".format(model, ae))

    return model


def check_and_create_resource(resource_type, create_fn, kwargs_create, list_fn, kwargs_list,
                              module, model, existing_resources=None, exclude_attributes=None, dead_states=None,
                              default_attribute_values=None):
    """
    This function checks whether there is a resource with same attributes as specified in the module options. If not,
    it creates and returns the resource.
    :param resource_type: Type of the resource to be created.
    :param create_fn: Function used in the module to handle create operation. The function should return a dict with
                      keys as resource & changed.
    :param kwargs_create: Dictionary of parameters for create operation.
    :param list_fn: List function in sdk to list all the resources of type resource_type.
    :param kwargs_list: Dictionary of parameters for list operation.
    :param module: Instance of AnsibleModule
    :param model: Model used to create a resource.
    :param exclude_attributes: The attributes which should not be used to distinguish the resource. e.g. display_name,
     dns_label.
    :param dead_states: List of states which can't transition to any of the usable states of the resource. This deafults
    to ["TERMINATING", "TERMINATED", "FAULTY", "FAILED", "DELETING", "DELETED", "UNKNOWN_ENUM_VALUE"]
    :param default_attribute_values: A dictionary containing default values for attributes.
    :return: A dictionary containing the resource & the "changed" status. e.g. {"vcn":{x:y}, "changed":True}
    """

    if module.params.get('force_create', None):
        _debug("Force creating {}".format(resource_type))
        result = call_with_backoff(create_fn, **kwargs_create)
        return result

    # Get the existing resources list sorted by creation time in descending order. Return the latest matching resource
    # in case of multiple resource matches.
    if exclude_attributes is None:
        exclude_attributes = {}
    try:
        if existing_resources is None:
            kwargs_list["sort_by"] = "TIMECREATED"
            existing_resources = list_all_resources(list_fn, **kwargs_list)
    except ValueError:
        # list_fn doesn't support sort_by, so remove the sort_by key in kwargs_list and retry
        kwargs_list.pop("sort_by", None)
        try:
            existing_resources = list_all_resources(list_fn, **kwargs_list)
        # Handle errors like 404 due to bad arguments to the list_all_resources call.
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result = dict()

    attributes_to_consider = _get_attributes_to_consider(exclude_attributes, model, module)
    resource_matched = None
    for resource in existing_resources:
        if _is_resource_active(resource, dead_states):
            _debug("Comparing user specified values {} against an existing resource's values {}".format(module.params,
                                                                                                        to_dict(
                                                                                                            resource)))
            if does_existing_resource_match_user_inputs(to_dict(resource), module, attributes_to_consider, exclude_attributes,
                                                        default_attribute_values):
                resource_matched = to_dict(resource)
                break

    if resource_matched:
        _debug("Resource with same attributes found: {}.".format(resource_matched))
        result[resource_type] = resource_matched
        result['changed'] = False
    else:
        _debug("No matching resource found. Attempting to create a new resource.")
        result = call_with_backoff(create_fn, **kwargs_create)

    return result


def _get_attributes_to_consider(exclude_attributes, model, module):
    """
    Determine the attributes to detect if an existing resource already matches the requested resource state
    :param exclude_attributes: Attributes to not consider for matching
    :param model: The model class used to create the Resource
    :param module: An instance of AnsibleModule that contains user's desires around a resource's state
    :return: A list of attributes that needs to be matched
    """

    # If a user explicitly requests us to match only against a set of resources (using 'key_by', use that as the list
    # of attributes to consider for matching.
    if 'key_by' in module.params and module.params['key_by'] is not None:
        attributes_to_consider = module.params['key_by']
    else:
        # ToDo: Drop the code for adding defined_tags to exclude_list once tagging is supported in all the modules.
        if "defined_tags" not in exclude_attributes:
            exclude_attributes.update({'defined_tags': True})

        # Consider all attributes except freeform_tags as freeform tags do not distinguish a resource.
        attributes_to_consider = list(model.attribute_map)
        if "freeform_tags" in attributes_to_consider:
            attributes_to_consider.remove("freeform_tags")
        # Temporarily removing node_count as the exisiting resource does not reflect it
        if "node_count" in attributes_to_consider:
            attributes_to_consider.remove("node_count")
    _debug("attributes to consider: {}".format(attributes_to_consider))
    return attributes_to_consider


def _is_resource_active(resource, dead_states):
    if dead_states is None:
        dead_states = DEAD_STATES

    if "lifecycle_state" not in resource.attribute_map:
        return True
    return resource.lifecycle_state not in dead_states


def is_attr_assigned_default(default_attribute_values, attr, assigned_value):
    if not default_attribute_values:
        return False

    if attr in default_attribute_values:
        default_val_for_attr = default_attribute_values.get(attr, None)
        if isinstance(default_val_for_attr, dict):
            # only compare keys that are in default_attribute_values[attr]
            # this is to ensure forward compatibility when the API returns new keys that are not known during
            # the time when the module author provided default values for the attribute
            return default_val_for_attr == {k: v for k, v in assigned_value.items() if k in default_val_for_attr}
        # non-dict, normal comparison
        return default_val_for_attr == assigned_value
    else:
        # module author has not provided a default value for attr
        return True


def has_user_provided_value_for_option(module, option):
    if option in _load_params():
        return True

    # User can specify value for option either using option name or its alias.
    # module.aliases is a dictionary with key as alias name and its value as option name.
    # Get one or more aliases of the option into a list.
    aliases = []
    for alias, opt in module.aliases.items():
        if opt == option:
            aliases.append(alias)
    # Check if one of the aliases of option is specified by user.
    for alias in aliases:
        if alias in _load_params():
            return True

    # Case where the attribute_name in resource(passed as option to this function) is an alias for some option X and
    # user has provided value for option X in the playbook, then return True if X is in _load_params().
    if option in module.aliases and module.aliases[option] in _load_params():
        return True

    return False


def create_resource(resource_type, create_fn, kwargs_create, module):
    """
    Create an OCI resource
    :param resource_type: Type of the resource to be created. e.g.: "vcn"
    :param create_fn: Function in the SDK to create the resource. e.g. virtual_network_client.create_vcn
    :param kwargs_create: Dictionary containing arguments to be used to call the create function create_fn
    :param module: Instance of AnsibleModule
    """
    result = dict(changed=False)
    try:
        resource = to_dict(call_with_backoff(create_fn, **kwargs_create).data)
        _debug("Created {}, {}".format(resource_type, resource))
        result['changed'] = True
        result[resource_type] = resource
        return result
    except ServiceError as ex:
        module.fail_json(msg=str(ex))


def does_existing_resource_match_user_inputs(existing_resource, module, attributes_to_compare, exclude_attributes,
                                             default_attribute_values=None):
    """
    Check if 'attributes_to_compare' in an existing_resource match the desired state provided by a user in 'module'.
    :param existing_resource: A dictionary representing an existing resource's values.
    :param module: The AnsibleModule representing the options provided by the user.
    :param attributes_to_compare: A list of attributes of a resource that are used to compare if an existing resource
                                    matches the desire state of the resource expressed by the user in 'module'.
    :param exclude_attributes: The attributes, that a module author provides, which should not be used to match the
        resource. This dictionary typically includes: (a) attributes which are initialized with dynamic default values like
        'display_name', 'security_list_ids' for subnets and (b) attributes that don't have any defaults like 'dns_label'
        in VCNs. The attributes are part of keys and 'True' is the value for all existing keys.
    :param default_attribute_values: A dictionary containing default values for attributes.
    :return: True if the values for the list of attributes is the same in the existing_resource and module instances.
    """

    if not default_attribute_values:
        default_attribute_values = {}

    for attr in attributes_to_compare:
        attribute_with_default_metadata = None
        if attr in existing_resource:
            resources_value_for_attr = existing_resource[attr]
            # Check if the user has explicitly provided the value for attr.
            user_provided_value_for_attr = _get_user_provided_value(module, attr)
            if user_provided_value_for_attr is not None:
                res = [True]
                check_if_user_value_matches_resources_attr(attr, resources_value_for_attr,
                                                           user_provided_value_for_attr, exclude_attributes,
                                                           default_attribute_values, res)
                if not res[0]:
                    _debug("Mismatch on attribute '{}'. User provided value is {} & existing resource's value is {}.".
                           format(attr, user_provided_value_for_attr, resources_value_for_attr))
                    return False
            else:
                # If the user has not explicitly provided the value for attr and attr is in exclude_list, we can
                # consider this as a 'pass'. For example, if an attribute 'display_name' is not specified by user and
                # that attribute is in the 'exclude_list' according to the module author(Not User), then exclude

                if exclude_attributes.get(attr) is None and resources_value_for_attr is not None:
                    if module.argument_spec.get(attr):
                        attribute_with_default_metadata = module.argument_spec.get(attr)
                        default_attribute_value = attribute_with_default_metadata.get('default', None)
                        if default_attribute_value is not None:
                            if existing_resource[attr] != default_attribute_value:
                                return False
                        # Check if attr has a value that is not default. For example, a custom `security_list_id`
                        # is assigned to the subnet's attribute `security_list_ids`. If the attribute is assigned a
                        # value that is not the default, then it must be considered a mismatch and false returned.
                        elif not is_attr_assigned_default(default_attribute_values, attr, existing_resource[attr]):
                            return False
        else:
            _debug("Attribute {} is in the create model of resource {}"
                   "but doesn't exist in the get model of the resource".format(attr, existing_resource.__class__))
    return True


def check_if_user_value_matches_resources_attr(attribute_name, resources_value_for_attr, user_provided_value_for_attr,
                                               exclude_attributes, default_attribute_values, res):
    if isinstance(default_attribute_values.get(attribute_name), dict):
        default_attribute_values = default_attribute_values.get(attribute_name)
    if isinstance(exclude_attributes.get(attribute_name), dict):
        exclude_attributes = exclude_attributes.get(attribute_name)
    if isinstance(resources_value_for_attr, list):
        user_provided_value_for_attr_copy = list(user_provided_value_for_attr)
        if len(resources_value_for_attr) > len(user_provided_value_for_attr_copy):
            for i in range(len(user_provided_value_for_attr_copy), len(resources_value_for_attr)):
                user_provided_value_for_attr_copy.append(None)
        elif len(user_provided_value_for_attr_copy) > len(resources_value_for_attr):
            for i in range(len(resources_value_for_attr), len(user_provided_value_for_attr_copy)):
                resources_value_for_attr.append(None)
        for index, resources_value_for_attr_part in enumerate(resources_value_for_attr):
            check_if_user_value_matches_resources_attr(attribute_name, resources_value_for_attr_part,
                                                       user_provided_value_for_attr_copy[index],
                                                       exclude_attributes, default_attribute_values, res)
    elif isinstance(resources_value_for_attr, dict):
        # Perform a deep equivalence check for dict typed attributes
        if not resources_value_for_attr and user_provided_value_for_attr:
            res[0] = False
        for key in resources_value_for_attr:
            if user_provided_value_for_attr is not None and user_provided_value_for_attr:
                check_if_user_value_matches_resources_attr(key, resources_value_for_attr.get(key),
                                                           user_provided_value_for_attr.get(key),
                                                           exclude_attributes, default_attribute_values, res)
            else:
                if exclude_attributes.get(key) is None:
                    if default_attribute_values.get(key) is not None:
                        user_provided_value_for_attr = default_attribute_values.get(key)
                        check_if_user_value_matches_resources_attr(key, resources_value_for_attr.get(key),
                                                                   user_provided_value_for_attr,
                                                                   exclude_attributes, default_attribute_values, res)
                    else:
                        res[0] = is_attr_assigned_default(default_attribute_values, attribute_name,
                                                          resources_value_for_attr.get(key))

    elif resources_value_for_attr != user_provided_value_for_attr:
        if exclude_attributes.get(attribute_name) is None and default_attribute_values.get(attribute_name) is not None:
            # As the user has not specified a value for an optional attribute, if the existing resource's
            # current state has a DEFAULT value for that attribute, we must not consider this incongruence
            # an issue and continue with other checks. If the existing resource's value for the attribute
            # is not the default value, then the existing resource is not a match.
            if not is_attr_assigned_default(default_attribute_values, attribute_name,
                                            resources_value_for_attr):
                res[0] = False
        elif user_provided_value_for_attr is not None:
            res[0] = False


def are_dicts_equal(option_name, existing_resource_dict, user_provided_dict, exclude_list,
                    default_attribute_values):
    if not user_provided_dict:
        # User has not provided a value for the map option. In this case, the user hasn't expressed an intent around
        # this optional attribute. Check if existing_resource_dict matches default.
        # For example, source_details attribute in volume is optional and does not have any defaults.
        return is_attr_assigned_default(default_attribute_values, option_name, existing_resource_dict)

    # If the existing resource has an empty dict, while the user has provided entries, dicts are not equal
    if not existing_resource_dict and user_provided_dict:
        return False

    # check if all keys of an existing resource's dict attribute matches user-provided dict's entries
    for sub_attr in existing_resource_dict:
        # If user has provided value for sub-attribute, then compare it with corresponding key in existing resource.
        if sub_attr in user_provided_dict:
            if existing_resource_dict[sub_attr] != user_provided_dict[sub_attr]:
                _debug("Failed to match: Existing resource's attr {} sub-attr {} value is {}, while user "
                       "provided value is {}".format(option_name, sub_attr, existing_resource_dict[sub_attr],
                                                     user_provided_dict.get(sub_attr, None)))
                return False

        # If sub_attr not provided by user, check if the sub-attribute value of existing resource matches default value.
        else:
            if not should_dict_attr_be_excluded(option_name, sub_attr, exclude_list):
                default_value_for_dict_attr = default_attribute_values.get(option_name, None)
                if default_value_for_dict_attr:
                    # if a default value for the sub-attr was provided by the module author, fail if the existing
                    # resource's value for the sub-attr is not the default
                    if not is_attr_assigned_default(default_value_for_dict_attr, sub_attr,
                                                    existing_resource_dict[sub_attr]):
                        return False
                else:
                    # No default value specified by module author for sub_attr
                    _debug("Consider as match: Existing resource's attr {} sub-attr {} value is {}, while user did not "
                           "provide a value for it. The module author also has not provided a default value for it or "
                           "marked it for exclusion. So ignoring this attribute during matching and continuing with"
                           "other checks".format(option_name, sub_attr, existing_resource_dict[sub_attr]))

    return True


def should_dict_attr_be_excluded(map_option_name, option_key, exclude_list):
    """An entry for the Exclude list for excluding a map's key is specifed as a dict with the map option name as the
    key, and the value as a list of keys to be excluded within that map. For example, if the keys "k1" and "k2" of a map
    option named "m1" needs to be excluded, the exclude list must have an entry {'m1': ['k1','k2']} """
    for exclude_item in exclude_list:
        if isinstance(exclude_item, dict):
            if map_option_name in exclude_item:
                if option_key in exclude_item[map_option_name]:
                    return True
    return False


def create_and_wait(resource_type, client, create_fn, kwargs_create, get_fn, get_param, module, states=None,
                    wait_applicable=True, kwargs_get=None):
    """
    A utility function to create a resource and wait for the resource to get into the state as specified in the module
    options.
    :param wait_applicable: Specifies if wait for create is applicable for this resource
    :param resource_type: Type of the resource to be created. e.g. "vcn"
    :param client: OCI service client instance to call the service periodically to retrieve data.
                   e.g. VirtualNetworkClient()
    :param create_fn: Function in the SDK to create the resource. e.g. virtual_network_client.create_vcn
    :param kwargs_create: Dictionary containing arguments to be used to call the create function create_fn.
    :param get_fn: Function in the SDK to get the resource. e.g. virtual_network_client.get_vcn
    :param get_param: Name of the argument in the SDK get function. e.g. "vcn_id"
    :param module: Instance of AnsibleModule.
    :param states: List of lifecycle states to watch for while waiting after create_fn is called.
                   e.g. [module.params['wait_until'], "FAULTY"]
    :param kwargs_get: Dictionary containing arguments to be used to call a multi-argument `get` function
    :return: A dictionary containing the resource & the "changed" status. e.g. {"vcn":{x:y}, "changed":True}
    """
    try:
        return create_or_update_resource_and_wait(resource_type, create_fn, kwargs_create, module, wait_applicable,
                                                  get_fn, get_param, states, client, kwargs_get=None)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def update_and_wait(resource_type, client, update_fn, kwargs_update, get_fn, get_param, module, states=None,
                    wait_applicable=True):
    """
    A utility function to update a resource and wait for the resource to get into the state as specified in the module
    options. It wraps the create_and_wait method as apart from the method and arguments, everything else is similar.
    :param wait_applicable: Specifies if wait for create is applicable for this resource
    :param resource_type: Type of the resource to be created. e.g. "vcn"
    :param client: OCI service client instance to call the service periodically to retrieve data.
                   e.g. VirtualNetworkClient()
    :param update_fn: Function in the SDK to update the resource. e.g. virtual_network_client.update_vcn
    :param kwargs_update: Dictionary containing arguments to be used to call the update function update_fn.
    :param get_fn: Function in the SDK to get the resource. e.g. virtual_network_client.get_vcn
    :param get_param: Name of the argument in the SDK get function. e.g. "vcn_id"
    :param module: Instance of AnsibleModule.
    :param states: List of lifecycle states to watch for while waiting after update_fn is called.
                   e.g. [module.params['wait_until'], "FAULTY"]
    :return: A dictionary containing the resource & the "changed" status. e.g. {"vcn":{x:y}, "changed":True}
    """
    try:
        return create_or_update_resource_and_wait(resource_type, update_fn, kwargs_update, module, wait_applicable,
                                                  get_fn, get_param, states, client)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def create_or_update_resource_and_wait(resource_type, function, kwargs_function, module, wait_applicable, get_fn, get_param, states, client, kwargs_get=None):
    """
    A utility function to create or update a resource and wait for the resource to get into the state as specified in
    the module options.
    :param resource_type: Type of the resource to be created. e.g. "vcn"
    :param function: Function in the SDK to create or update the resource.
    :param kwargs_function: Dictionary containing arguments to be used to call the create or update function
    :param module: Instance of AnsibleModule.
    :param wait_applicable: Specifies if wait for create is applicable for this resource
    :param get_fn: Function in the SDK to get the resource. e.g. virtual_network_client.get_vcn
    :param get_param: Name of the argument in the SDK get function. e.g. "vcn_id"
    :param states: List of lifecycle states to watch for while waiting after create_fn is called.
                   e.g. [module.params['wait_until'], "FAULTY"]
    :param client: OCI service client instance to call the service periodically to retrieve data.
                   e.g. VirtualNetworkClient()
    :param kwargs_get: Dictionary containing arguments to be used to call the get function which requires multiple arguments.
    :return: A dictionary containing the resource & the "changed" status. e.g. {"vcn":{x:y}, "changed":True}
    """
    result = create_resource(resource_type, function, kwargs_function, module)
    resource = result[resource_type]
    if wait_applicable and module.params.get('wait', None):
        if kwargs_get:
            response_get = call_with_backoff(get_fn, **kwargs_get)
        else:
            response_get = call_with_backoff(get_fn, **{get_param: resource['id']})
        if states is None:
            states = module.params.get('wait_until') or DEFAULT_READY_STATES
        resource = to_dict(oci.wait_until(client,
                                          response_get,
                                          evaluate_response=lambda r: r.data.lifecycle_state in states,
                                          max_wait_seconds=module.params.get('wait_timeout',
                                                                             MAX_WAIT_TIMEOUT_IN_SECONDS)).data)
        result[resource_type] = resource
    return result


def delete_and_wait(resource_type, client, get_fn, kwargs_get, delete_fn, kwargs_delete, module, states=None,
                    wait_applicable=True):
    """A utility function to delete a resource and wait for the resource to get into the state as specified in the
    module options.
    :param wait_applicable: Specifies if wait for delete is applicable for this resource
    :param resource_type: Type of the resource to be deleted. e.g. "vcn"
    :param client: OCI service client instance to call the service periodically to retrieve data.
                   e.g. VirtualNetworkClient()
    :param get_fn: Function in the SDK to get the resource. e.g. virtual_network_client.get_vcn
    :param kwargs_get: Dictionary of arguments for get function get_fn. e.g. {"vcn_id": module.params["id"]}
    :param delete_fn: Function in the SDK to delete the resource. e.g. virtual_network_client.delete_vcn
    :param kwargs_delete: Dictionary of arguments for delete function delete_fn. e.g. {"vcn_id": module.params["id"]}
    :param module: Instance of AnsibleModule.
    :param states: List of lifecycle states to watch for while waiting after delete_fn is called. If nothing is passed,
                   defaults to ["TERMINATED", "DETACHED", "DELETED"].
    :return: A dictionary containing the resource & the "changed" status. e.g. {"vcn":{x:y}, "changed":True}
    """

    result = dict(changed=False)
    try:
        resource = to_dict(call_with_backoff(get_fn, **kwargs_get).data)
        if resource:
            if "lifecycle_state" not in resource or resource['lifecycle_state'] not in \
                    {'DETACHING', 'DETACHED', 'DELETING', 'DELETED', 'TERMINATING', 'TERMINATED'}:
                call_with_backoff(delete_fn, **kwargs_delete)
                _debug("Deleted {}, {}".format(resource_type, resource))
                result['changed'] = True

                if wait_applicable and module.params.get('wait', None):
                    if states is None:
                        states = module.params.get('wait_until') or DEFAULT_TERMINATED_STATES
                    try:
                        wait_response = oci.wait_until(client,
                                                       get_fn(**kwargs_get),
                                                       evaluate_response=lambda r: r.data.lifecycle_state in states,
                                                       max_wait_seconds=module.params.get('wait_timeout',
                                                                                          MAX_WAIT_TIMEOUT_IN_SECONDS),
                                                       succeed_on_not_found=True)
                    except MaximumWaitTimeExceeded as ex:
                        module.fail_json(msg=str(ex))
                    except ServiceError as ex:
                        if ex.status != 404:
                            module.fail_json(msg=ex.message)
                        else:
                            # While waiting for resource to get into terminated state, if the resource is not found.
                            _debug("API returned Status:404(Not Found) while waiting for resource to get into"
                                   " terminated state.")
                            resource['lifecycle_state'] = "DELETED"
                            result[resource_type] = resource
                            return result
                    # oci.wait_until() returns an instance of oci.util.Sentinel in case the resource is not found.
                    if type(wait_response) is not Sentinel:
                        resource = to_dict(wait_response.data)
                    else:
                        resource['lifecycle_state'] = "DELETED"

            result[resource_type] = resource
        else:
            _debug("Resource {} with {} already deleted. So returning changed=False".format(resource_type, kwargs_get))
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)
        result[resource_type] = ''
    return result


def are_attrs_equal(current_resource, module, attributes):
    """
    Check if the specified attributes are equal in the specified 'model' and 'module'. This is used to check if an OCI
    Model instance already has the values specified by an Ansible user while invoking an OCI Ansible module and if a
    resource needs to be updated.
    :param current_resource: A resource model instance
    :param module: The AnsibleModule representing the options provided by the user
    :param attributes: A list of attributes that would need to be compared in the model and the module instances.
    :return: True if the values for the list of attributes is the same in the model and module instances
    """
    for attr in attributes:
        curr_value = getattr(current_resource, attr, None)
        user_provided_value = _get_user_provided_value(module, attribute_name=attr)

        if user_provided_value is not None:
            if curr_value != user_provided_value:
                _debug("are_attrs_equal - current resource's attribute " + attr + " value is " + str(
                    curr_value) + " and this doesn't match user provided value of " + str(user_provided_value))
                return False
    return True


def _get_user_provided_value(module, attribute_name):
    """
    Returns the user provided value for "attribute_name". We consider aliases in the module.
    """
    user_provided_value = module.params.get(attribute_name, None)
    if user_provided_value is None:
        # If the attribute_name is set as an alias for some option X and user has provided value in the playbook using
        # option X, then user provided value for attribute_name is equal to value for X.
        # Get option name for attribute_name from module.aliases.
        # module.aliases is a dictionary with key as alias name and its value as option name.
        option_alias_for_attribute = module.aliases.get(attribute_name, None)
        if option_alias_for_attribute is not None:
            user_provided_value = module.params.get(option_alias_for_attribute, None)
    return user_provided_value


def update_model_with_user_options(curr_model, update_model, module):
    """
    Update the 'update_model' with user provided values in 'module' for the specified 'attributes' if they are different
    from the values in the 'curr_model'.
    :param curr_model: A resource model instance representing the state of the current resource
    :param update_model: An instance of the update resource model for the current resource's type
    :param module: An AnsibleModule representing the options provided by the user
    :return: An updated 'update_model' instance filled with values that would need to be updated in the current resource
    state to satisfy the user's requested state.
    """
    attributes = update_model.attribute_map.keys()
    for attr in attributes:
        curr_value_for_attr = getattr(curr_model, attr, None)
        user_provided_value = _get_user_provided_value(module, attribute_name=attr)

        if curr_value_for_attr != user_provided_value:
            if user_provided_value is not None:
                # Only update if a user has specified a value for an option
                _debug("User requested {} for attribute {}, whereas the current value is {}. So adding it "
                       "to the update model".format(user_provided_value, attr, curr_value_for_attr))
                setattr(update_model, attr, user_provided_value)
            else:
                # Always set current values of the resource in the update model if there is no request for change in
                # values
                setattr(update_model, attr, curr_value_for_attr)
    return update_model


def _get_retry_strategy():
    retry_strategy_builder = RetryStrategyBuilder(max_attempts_check=True, max_attempts=10,
                                                  retry_max_wait_between_calls_seconds=30,
                                                  retry_base_sleep_time_seconds=3,
                                                  backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE)
    retry_strategy_builder.add_service_error_check(
        service_error_retry_config={429: [], 400: ['QuotaExceeded', 'LimitExceeded']},
        service_error_retry_on_any_5xx=True)
    return retry_strategy_builder.get_retry_strategy()


def call_with_backoff(fn, **kwargs):
    if "retry_strategy" not in kwargs:
        kwargs['retry_strategy'] = _get_retry_strategy()
    try:
        return fn(**kwargs)
    except TypeError as te:
        if "unexpected keyword argument" in str(te):
            del kwargs["retry_strategy"]
            return fn(**kwargs)


def generic_hash(obj):
    """
    Compute a hash of all the fields in the object
    :param obj: Object whose hash needs to be computed
    :return: a hash value for the object
    """
    sum = 0
    for field in obj.attribute_map.keys():
        field_value = getattr(obj, field)
        if isinstance(field_value, list):
            for value in field_value:
                sum = sum + hash(value)
        elif isinstance(field_value, dict):
            for k, v in field_value.items():
                sum = sum + hash(hash(k) + hash(":") + hash(v))
        else:
            sum = sum + hash(getattr(obj, field))
    return sum


def generic_eq(s, other):
    if other is None:
        return False
    return s.__dict__ == other.__dict__


def generate_subclass(parent_class):
    """Make a class hash-able by generating a subclass with a __hash__ method that returns the sum of all fields within
    the parent class"""
    dict_of_method_in_subclass = {
        "__init__": parent_class.__init__,
        "__hash__": generic_hash,
        "__eq__": generic_eq
    }
    subclass_name = "GeneratedSub" + parent_class.__name__
    generated_sub_class = type(subclass_name, (parent_class,), dict_of_method_in_subclass)
    return generated_sub_class


def create_hashed_instance(class_type):
    hashed_class = generate_subclass(class_type)
    return hashed_class()


def get_hashed_object_list(class_type, object_with_values, attributes_class_type=None):
    if object_with_values is None:
        return None
    hashed_class_instances = []
    for object_with_value in object_with_values:
        hashed_class_instances.append(get_hashed_object(class_type, object_with_value, attributes_class_type))
    return hashed_class_instances


def get_hashed_object(class_type, object_with_value, attributes_class_type=None):
    """
    Convert any class instance into hashable so that the
    instances are eligible for various comparison
    operation available under set() object.
    :param class_type: Any class type whose instances needs to be hashable
    :param object_with_value: Instance of the class type with values which
     would be set in the resulting isinstance
    :return: A hashable instance with same state of the provided object_with_value
    """
    if object_with_value is None:
        return None
    HashedClass = generate_subclass(class_type)
    hashed_class_instance = HashedClass()
    for attribute in hashed_class_instance.attribute_map:
        attribute_value = getattr(object_with_value, attribute)
        if attributes_class_type:
            for attribute_class_type in attributes_class_type:
                if isinstance(attribute_value, attribute_class_type):
                    attribute_value = get_hashed_object(attribute_class_type, attribute_value)
        hashed_class_instance.__setattr__(attribute, attribute_value)
    return hashed_class_instance


def update_class_type_attr_difference(update_class_details, existing_instance,
                                      attr_name, attr_class, input_attr_value):
    """
    Checks the difference and updates an attribute which is represented by a class
    instance. Not aplicable if the attribute type is a primitive value.
    For example, if a class name is A with an attribute x, then if A.x = X(), then only
    this method works.
    :param update_class_details The instance which should be updated if there is change in
     attribute value
    :param existing_instance The instance  whose attribute value is compared with input
     attribute value
    :param attr_name Name of the attribute whose value should be compared
    :param attr_class Class type of the attribute
    :param input_attr_value The value of input attribute which should replaced the current
     value in case of mismatch
    :return: A boolean value indicating whether attribute value has been replaced
    """
    changed = False
    # Here existing attribute values is an instance
    existing_attr_value = get_hashed_object(attr_class, getattr(existing_instance, attr_name))
    if input_attr_value is None:
        update_class_details.__setattr__(attr_name, existing_attr_value)
    else:
        changed = not input_attr_value.__eq__(existing_attr_value)
        if changed:
            update_class_details.__setattr__(attr_name, input_attr_value)
        else:
            update_class_details.__setattr__(attr_name, existing_attr_value)

    return changed


def get_existing_resource(target_fn, module, **kwargs):
    """
    Returns the requested resource if it exists based on the input arguments.
    :param target_fn The function which should be used to find the requested resource
    :param module Instance of AnsibleModule attribute value
    :param kwargs A map of arguments consisting of values based on which requested resource should be searched
    :return: Instance of requested resource
    """
    existing_resource = None
    try:
        response = call_with_backoff(target_fn, **kwargs)
        existing_resource = response.data
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)

    return existing_resource


def get_attached_instance_info(config, lookup_attached_instance, list_attachments_fn, list_attachments_args):
    identity_client = IdentityClient(config)

    volume_attachments = []

    if lookup_attached_instance:
        # Get all the compartments in the tenancy
        compartments = to_dict(identity_client.list_compartments(config.get("tenancy")).data)
        # For each compartment, get the volume attachments for the compartment_id with the other args in
        # list_attachments_args.
        for compartment in compartments:
            list_attachments_args['compartment_id'] = compartment['id']
            try:
                volume_attachments += list_all_resources(list_attachments_fn,
                                                         **list_attachments_args)

            # Pass ServiceError due to authorization issue in accessing volume attachments of a compartment
            except ServiceError as ex:
                if ex.status == 404:
                    pass

    else:
        volume_attachments = list_all_resources(list_attachments_fn,
                                                **list_attachments_args)

    volume_attachments = to_dict(volume_attachments)
    # volume_attachments has attachments in DETACHING or DETACHED state. Return the volume attachment in ATTACHING or
    # ATTACHED state

    return next((volume_attachment for volume_attachment in volume_attachments
                 if volume_attachment['lifecycle_state'] in ["ATTACHING", "ATTACHED"]), None)


def check_mode(fn):
    def wrapper(*args, **kwargs):
        if os.environ.get('OCI_ANSIBLE_EXPERIMENTAL', None):
            return fn(*args, **kwargs)
        return None
    return wrapper
