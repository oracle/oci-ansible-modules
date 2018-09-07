#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: oci_tag
short_description: Create, retire and reactivate tag key definitions in OCI
description:
    - This module allows the user to create, retire and reactivate tag key definitions in OCI. A key definition defines
      the schema of a tag and includes a namespace, tag key, and tag value type. Currently the only tag value type
      supported is "string", and hence is not specified during creation. Defined tag keys are case insensitive. However
      note that defined tag values are case sensitive.
version_added: "2.5"
options:
    tag_namespace_id:
        description: The OCID of the tag namespace that will contain this tag key definition.
        required: true
    tag_name:
        description: The name assigned to the tag key definition during creation. It must be unique across all tags
                     in the specified tag namespace and cannot be changed. All ascii characters are allowed except
                     spaces and dots. Note that names are case insenstive, that means you can not have two different
                     tags with same name but with different casing in one tag namespace.
        required: true
        aliases: ['name']
    description:
        description: A description to be associated with the tag definition during creation. This does not have to be
                     unique, and can be changed later. Required when creating a tag definition with I(state=present)
                     The length of the description must be between 1 and 400 characters.
        required: false
    reactivate:
        description: Whether a retired tag definition needs to be reactivated
        required: false
        default: False
        type: bool
    state:
        description: The state of the tag key definition that must be asserted to. When I(state=present), and the
                     tag definition doesn't exist, the tag definition is created. When I(state=absent), the tag
                     namespace is retired. To reactivate a retired tag key definition, use I(reactivate=yes).
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
- name: Create a new tag key definition
  oci_tag:
    tag_namespace_id: "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx"
    name: "CostCenter"
    description: "This tag will show the cost center that will be used for billing of resources."

- name: Update the description of a tag definition
  oci_tag:
    tag_namespace_id: "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx"
    name: "CostCenter"
    description: "Tags used for cost center"

- name: Retire a tag key definition
  oci_tag:
    tag_namespace_id: "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx"
    name: "CostCenter"
    state: "absent"

- name: To reactivate a retired namespace
  oci_tag:
    tag_namespace_id: "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx"
    name: "CostCenter"
    reactivate: "yes"
'''

RETURN = '''
tag:
    description: Details of the tag key definition
    returned: On successful create or update of a tag key definition
    type: dict
    sample: {
            "compartment_id": null,
            "defined_tags": {},
            "description": "This tag will show the cost center that will be used for billing of resources.",
            "freeform_tags": {},
            "id": "ocid1.tagdefinition.oc1..xxxxxEXAMPLExxxxx",
            "is_retired": false,
            "name": "CostCenter",
            "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx",
            "tag_namespace_name": null,
            "time_created": "2018-01-16T04:55:22.600000+00:00"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateTagDetails, UpdateTagDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def set_logger(provided_logger):
    global logger
    logger = provided_logger


def get_logger():
    return logger


def _get_tag_definition_from_id(identity_client, tag_namespace_id, tag_name):
    try:
        resp = oci_utils.call_with_backoff(identity_client.get_tag, tag_namespace_id=tag_namespace_id,
                                           tag_name=tag_name)
        return resp.data
    except ServiceError:
        # ignore
        return None


def update_tag_definition_state(identity_client, tag_namespace_id, tag_name, module, description, is_retired):
    try:
        utd = UpdateTagDetails()
        utd.is_retired = is_retired
        # even though only retired state needs to be updated, the
        # details model class requires a valid description and so we
        # pass in the old description of the tag
        utd.description = description

        updated_tag = oci_utils.call_with_backoff(identity_client.update_tag, tag_namespace_id=tag_namespace_id,
                                                  tag_name=tag_name, update_tag_details=utd).data

        get_logger().info("Retired tag definition %s", tag_name)
        return updated_tag, True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def update_tag_namespace_description(identity_client, tag_namespace_id, tag_name, description, module):
    try:
        utd = UpdateTagDetails()
        utd.description = description

        updated_tag = oci_utils.call_with_backoff(identity_client.update_tag, tag_namespace_id=tag_namespace_id,
                                                  tag_name=tag_name, update_tag_details=utd).data

        get_logger().info("Updated tag definition %s", to_dict(updated_tag))
        return updated_tag, True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def create_tag(identity_client, tag_namespace_id, name, description, module):
    result = {}
    try:
        ctd = CreateTagDetails()
        ctd.name = name
        ctd.description = description

        create_response = oci_utils.call_with_backoff(identity_client.create_tag, tag_namespace_id=tag_namespace_id,
                                                      create_tag_details=ctd)
        get_logger().info("Created tag definition %s", to_dict(create_response.data))

        result['tag'] = to_dict(create_response.data)
        result['changed'] = True
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def main():
    set_logger(oci_utils.get_logger("oci_tag"))

    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(
        tag_namespace_id=dict(type='str', required=True),
        tag_name=dict(type='str', required=True, aliases=['name']),
        description=dict(type='str', required=False),
        reactivate=dict(type='bool', required=False),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params['state']

    result = dict(changed=False)

    tag_namespace_id = module.params.get("tag_namespace_id", None)
    tag_name = module.params.get("tag_name", None)
    name = module.params.get('name', None)
    description = module.params.get('description', None)

    get_logger().debug("tag key definition name is " + str(tag_name))

    tag = _get_tag_definition_from_id(identity_client, tag_namespace_id, tag_name)

    if state == 'absent':
        get_logger().debug("Retire tag key definition %s requested", tag_name)
        if tag is not None:
            retired = False
            if not tag.is_retired:
                get_logger().debug("Retiring %s", tag.id)
                tag, retired = update_tag_definition_state(identity_client, tag_namespace_id, tag_name, module,
                                                           description=tag.description, is_retired=True)

            result['changed'] = retired
            result['tag'] = to_dict(tag)
    # if the Tag doesn't exist, it is already deleted and so we return the default dict with changed as False
    elif state == 'present':
        if tag is not None:
            desc_changed = False
            reactivated = False

            if tag.description != description:
                tag, desc_changed = update_tag_namespace_description(identity_client, tag_namespace_id, tag_name,
                                                                     description, module)

            reactivate = module.params.get('reactivate', None)
            if reactivate:
                get_logger().debug("Reactivate tag definition %s requested", tag_name)
                if tag.is_retired:
                    tag, reactivated = update_tag_definition_state(identity_client, tag_namespace_id, tag_name, module,
                                                                   description=tag.description,
                                                                   is_retired=False)

            result['changed'] = desc_changed or reactivated
            result['tag'] = to_dict(tag)
        else:
            # Unlike other OCI resources, if a user has provided `tag_namespace_id` and `name`, and the Tag is not
            # present already, we will attempt to create the Tag. This is because there is no special way to
            # differentiate a "create" from a "update" through the absence of a "tag" "id" option for OCI Tags.
            # Therefore, also, oci_tag doesn't include oracle_creatable_resource documentation fragment and options.
            result = create_tag(identity_client, tag_namespace_id, name, description, module)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
