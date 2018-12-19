#!/usr/bin/env python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""
Oracle Cloud Infrastructure(OCI) Inventory Script
=================================================
This script generates Ansible dynamic inventory for OCI by using the OCI Python SDK.

The order of precedence for reading parameters is command line arguments, then environment variables followed by options
in inventory settings file. The dynamic inventory settings file defaults to "./oci_inventory.ini" file.
The config file defaults to "~/.oci/config" file. The script reads "DEFAULT" profile from the config file if no profile
name is specified.

This script accepts following command line arguments:

usage: oci_inventory.py [-h] [--list] [--host HOST] [-config CONFIG_FILE]
                        [--profile PROFILE] [--compartment COMPARTMENT]
                        [--parent-compartment-ocid PARENT_COMPARTMENT_OCID]
                        [--fetch-hosts-from-subcompartments] [--refresh-cache]
                        [--debug] [--auth {api_key,instance_principal}]
                        [--enable-parallel-processing]
                        [--max-thread-count MAX_THREAD_COUNT]
                        [--freeform-tags FREEFORM_TAGS]
                        [--defined-tags DEFINED_TAGS]

optional arguments:
  -h, --help            show this help message and exit
  --list                List instances (default: True)
  --host HOST           Get all information about a compute instance
  -config CONFIG_FILE, --config-file CONFIG_FILE
                        OCI config file location
  --profile PROFILE     OCI config profile for connecting to OCI
  --compartment COMPARTMENT
                        Name of the compartment for which dynamic inventory must be generated. If you want to generate a
                        dynamic inventory for the root compartment of the tenancy, specify the tenancy name as the name
                        of the compartment.
  --parent-compartment-ocid
                        Only valid when --compartment is set. Parent compartment ocid of the specified compartment.
                        Defaults to tenancy ocid.
  --fetch-hosts-from-subcompartments
                        Only valid when --compartment is set. Default is false. When set to true, inventory
                        is built with the entire hierarchy of the given compartment.
  --refresh-cache, -r   Force refresh of cache by making API requests to OCI.
                        Use this option whenever you are building inventory
                        with new filter options to avoid reading cached
                        inventory. (default: False - use cache files)
  --debug               Send debug messages to STDERR
  --auth {api_key,instance_principal}
                        The type of authentication to use for making API
                        requests. By default, the API key in your config will
                        be used. Set this option to `instance_principal` to
                        use instance principal based authentication. This
                        value can also be provided in the
                        OCI_ANSIBLE_AUTH_TYPE environment variable.
  --enable-parallel-processing
                        Inventory generation for tenants with huge number of instances might take a long time.
                        When this flag is set, the inventory script uses thread pools to parallelise the
                        inventory generation.
  --max-thread-count
                        Only valid when --enable-parallel-processing is set. When set, this script uses threads to
                        improve the performance of building the inventory. This option specifies the maximum number of
                        threads to use. Defaults to 50. This value can also be provided in the settings config file.
  --freeform-tags FREEFORM_TAGS
                        Freeform tags provided as a string in valid JSON
                        format. Example: { "stage": "dev", "app": "demo"} Use
                        this option to build inventory of only those hosts
                        which are tagged with all the specified key-value
                        pairs.
  --defined-tags DEFINED_TAGS
                        Defined tags provided as a string in valid JSON
                        format. Example: {"namespace1": {"key1": "value1",
                        "key2": "value2"}, "namespace2": {"key": "value"}} Use
                        this option to build inventory of only those hosts
                        which are tagged with all the specified key-value
                        pairs.

The script reads following environment variables:
OCI_CONFIG_FILE,
OCI_INI_PATH,
OCI_CONFIG_PROFILE,
OCI_USER_ID,
OCI_USER_FINGERPRINT,
OCI_USER_KEY_FILE,
OCI_TENANCY,
OCI_REGION,
OCI_USER_KEY_PASS_PHRASE,
OCI_CACHE_DIR,
OCI_CACHE_MAX_AGE,
OCI_HOSTNAME_FORMAT
OCI_ANSIBLE_AUTH_TYPE

The inventory generated is by default grouped by each of the following:
region
compartment_name
availability domain
vcn_id
subnet_id
security_list_id
image_id when the instance is launched using an image
instance shape
freeform tags with group name as "tag_key=value"
defined tags with group name as "namespace#key=value"
metadata (key, value) with group name as "key=value"
extended metadata (key, value) with group name as "key=value"

By default, all non-alphanumeric characters except HASH(#), EQUALS(=), PERIOD(.) and DASH(-) in group names and host
names are replaced with an UNDERSCORE when the inventory is generated, so that the names can be used as Ansible
groups. To disable this replacement, set sanitize_names to False in the dynamic inventory settings file(default
./oci_inventory.ini). To also replace DASH(-) when sanitize_names is True, set replace_dash_in_names to True in
the settings file.

When run for a specific host using the --host option, this script returns the following variables:
{
    "availability_domain": "IwGV:US-ASHBURN-AD-1",
    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
    "defined_tags": {},
    "display_name": "ansible-test-instance-448",
    "extended_metadata": {},
    "freeform_tags": {},
    "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
    "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
    "ipxe_script": null,
    "launch_mode": "CUSTOM",
    "launch_options": {
      "boot_volume_type": "ISCSI",
      "firmware": "UEFI_64",
      "network_type": "VFIO",
      "remote_data_volume_type": "ISCSI"
    },
    "lifecycle_state": "AVAILABLE",
    "metadata": {
      "baz": "quux",
      "foo": "bar"
    },
    "region": "iad",
    "shape": "VM.Standard1.1",
    "source_details": {
      "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
      "source_type": "image"
    },
    "time_created": "2018-01-16T12:13:35.336000+00:00"
}

author: "Rohit Chaware (@rohitChaware)"
        "Manoj Meda (@manojmeda)"
"""

from __future__ import print_function
import argparse
import json
import os
import re
import sys
from time import time
from ansible.module_utils.six.moves import configparser
from collections import deque
from multiprocessing.pool import ThreadPool
from contextlib import contextmanager

try:
    import oci
    from oci._vendor import requests
    from oci.retry import RetryStrategyBuilder
    from oci.constants import HEADER_NEXT_PAGE
    from oci.core.compute_client import ComputeClient
    from oci.identity.identity_client import IdentityClient
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

__version__ = "1.4.0"


def _get_retry_strategy():
    retry_strategy_builder = RetryStrategyBuilder(
        max_attempts_check=True,
        max_attempts=10,
        retry_max_wait_between_calls_seconds=30,
        retry_base_sleep_time_seconds=3,
        backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE,
    )
    retry_strategy_builder.add_service_error_check(
        service_error_retry_config={429: [], 400: ["QuotaExceeded", "LimitExceeded"]},
        service_error_retry_on_any_5xx=True,
    )
    return retry_strategy_builder.get_retry_strategy()


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


def call_with_backoff(fn, **kwargs):
    if "retry_strategy" not in kwargs:
        kwargs["retry_strategy"] = _get_retry_strategy()
    try:
        return fn(**kwargs)
    except TypeError as te:
        if "unexpected keyword argument" in str(te):
            del kwargs["retry_strategy"]
            return fn(**kwargs)


def _is_instance_principal_auth(params):
    # check if auth is set to `instance_principal`.
    return params["auth"] == "instance_principal"


def create_service_client(params, service_client_class):
    kwargs = {}
    if _is_instance_principal_auth(params):
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        except Exception as ex:
            message = (
                "Failed retrieving certificates from localhost. Instance principal based authentication is only"
                "possible from within OCI compute instances. Exception: {0}".format(
                    str(ex)
                )
            )
            OCIInventory().log(message)
            sys.exit()
        kwargs["signer"] = signer

    # Create service client class with the signer.
    client = service_client_class(params, **kwargs)

    return client


class OCIInventory:

    LIFECYCLE_ACTIVE_STATE = "ACTIVE"
    LIFECYCLE_RUNNING_STATE = "RUNNING"
    LIFECYCLE_ATTACHED_STATE = "ATTACHED"

    def __init__(self):
        self.inventory = {"all": {"hosts": [], "vars": {}}, "_meta": {"hostvars": {}}}
        self.config = {}
        self.params = {
            "ini_file": os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "oci_inventory.ini"
            ),
            "config_file": os.path.join(os.path.expanduser("~"), ".oci", "config"),
            "profile": "DEFAULT",
            "user": None,
            "fingerprint": None,
            "key_file": None,
            "tenancy": None,
            "region": None,
            "pass_phrase": None,
            "cache_dir": ".",
            "cache_max_age": 300,
            "cache_file": "./ansible-oci.cache",
            "compartment": None,
            "parent_compartment_ocid": None,
            "fetch_hosts_from_subcompartments": False,
            "debug": False,
            "hostname_format": "public_ip",
            "sanitize_names": True,
            "replace_dash_in_names": False,
            "auth": "api_key",
            "enable_parallel_processing": False,
            "max_thread_count": 50,
            "freeform_tags": None,
            "defined_tags": None,
        }
        boolean_options = ["sanitize_names", "replace_dash_in_names"]
        dict_options = ["freeform_tags", "defined_tags"]

        self.parse_cli_args()

        if self.args.debug:
            self.params["debug"] = True
            self.log("Executing in debug mode.")

        if "OCI_INI_PATH" in os.environ:
            oci_ini_file_path = os.path.expanduser(
                os.path.expandvars(os.environ.get("OCI_INI_PATH"))
            )
            if os.path.isfile(oci_ini_file_path):
                self.params["ini_file"] = oci_ini_file_path

        self.settings_config = configparser.ConfigParser()
        self.settings_config.read(self.params["ini_file"])

        # Preference order: CLI args > environment variable > settings from config file.
        if "config_file" in self.args and getattr(self.args, "config_file") is not None:
            self.params["config_file"] = os.path.expanduser(self.args.config_file)
        elif "OCI_CONFIG_FILE" in os.environ:
            self.params["config_file"] = os.path.expanduser(
                os.path.expandvars(os.environ.get("OCI_CONFIG_FILE"))
            )
        elif self.settings_config.has_option("oci", "config_file"):
            self.params["config_file"] = os.path.expanduser(
                self.settings_config.get("oci", "config_file")
            )

        if "profile" in self.args and getattr(self.args, "profile") is not None:
            self.params["profile"] = self.args.profile
        elif "OCI_CONFIG_PROFILE" in os.environ:
            self.params["profile"] = os.environ.get("OCI_CONFIG_PROFILE")
        elif self.settings_config.has_option("oci", "profile"):
            self.params["profile"] = self.settings_config.get("oci", "profile")

        self.read_config()
        self.read_settings_config(boolean_options, dict_options)
        self.read_env_vars()
        self.read_cli_args(dict_options)

        self.log("Using following parameters for OCI dynamic inventory:")
        self.log(self.params)
        self.compute_client = create_service_client(self.params, ComputeClient)
        self.identity_client = create_service_client(self.params, IdentityClient)
        self.virtual_nw_client = create_service_client(
            self.params, VirtualNetworkClient
        )

        # For the case, when auth="instance_principal", tenancy_id is not available.
        if self.params["auth"] == "instance_principal":
            self.params["tenancy"] = self.get_tenancy_id()

        self.params["cache_file"] = os.path.join(
            self.params["cache_dir"], "ansible-oci.cache"
        )

        if not self.args.refresh_cache and self.is_cache_valid():
            self.log("Reading inventory from cache.")
            self.inventory = self.read_from_cache()
        else:
            self.build_inventory()
            self.write_to_cache(self.inventory)

        if self.args.host:
            if self.args.host in self.inventory["_meta"]["hostvars"]:
                print(
                    json.dumps(
                        self.inventory["_meta"]["hostvars"][self.args.host],
                        sort_keys=True,
                        indent=2,
                    )
                )
            else:
                self.log(
                    "Either the specified host does not exist or its facts cannot be retrieved."
                )
                print({})

        else:
            print(json.dumps(self.inventory, sort_keys=True, indent=2))

    def log(self, *args, **kwargs):
        if self.params["debug"]:
            print(*args, file=sys.stderr, **kwargs)

    def get_tenancy_id(self):
        # Get the instance metadata using the HTTP endpoint.
        GET_TENANCY_ID_URL = "http://169.254.169.254/opc/v1/instance/compartmentId"
        response = requests.get(GET_TENANCY_ID_URL)
        compartment_id = response.text
        compartment = call_with_backoff(
            self.identity_client.get_compartment, compartment_id=compartment_id
        ).data
        while compartment.compartment_id:
            compartment = call_with_backoff(
                self.identity_client.get_compartment,
                compartment_id=compartment.compartment_id,
            ).data
        return compartment.id

    def read_config(self):
        if os.path.isfile(self.params["config_file"]):
            self.config = oci.config.from_file(
                file_location=self.params["config_file"],
                profile_name=self.params["profile"],
            )

        self.config["additional_user_agent"] = "Oracle-Ansible/{0}".format(__version__)

        for setting in self.config:
            self.params[setting] = self.config[setting]

    def read_env_vars(self):
        EnvParamsMapping = dict(
            OCI_CONFIG_FILE="config_file",
            OCI_INI_PATH="ini_path",
            OCI_TENANCY="tenancy",
            OCI_REGION="region",
            OCI_CACHE_DIR="cache_dir",
            OCI_CACHE_MAX_AGE="cache_max_age",
            OCI_HOSTNAME_FORMAT="hostname_format",
            OCI_USER_ID="user",
            OCI_USER_FINGERPRINT="fingerprint",
            OCI_USER_KEY_FILE="key_file",
            OCI_USER_KEY_PASS_PHRASE="pass_phrase",
            OCI_CONFIG_PROFILE="profile",
            OCI_ANSIBLE_AUTH_TYPE="auth",
        )

        for env_var in os.environ:
            if env_var in EnvParamsMapping:
                self.params[EnvParamsMapping[env_var]] = os.environ.get(env_var)

    def read_cli_args(self, dict_options):
        for setting in vars(self.args):
            if getattr(self.args, setting) is not None:
                if setting in dict_options:
                    self.params[setting] = json.loads(getattr(self.args, setting))
                    if type(self.params[setting]) != dict:
                        self.fail(message="Invalid JSON input for {0}.".format(setting))
                else:
                    self.params[setting] = getattr(self.args, setting)

    def is_cache_valid(self):
        if os.path.isfile(self.params["cache_file"]):
            mod_time = os.path.getmtime(self.params["cache_file"])
            current_time = time()
            if (mod_time + float(self.params["cache_max_age"])) > current_time:
                return True
            else:
                self.log("Cache is outdated.")
        else:
            self.log("Cache file is invalid.")
        return False

    def read_from_cache(self):
        with open(self.params["cache_file"], "r") as cache:
            return json.loads(cache.read())

    def write_to_cache(self, data):
        json_data = json.dumps(data, sort_keys=True, indent=2)
        with open(self.params["cache_file"], "w") as f:
            f.write(json_data)

    def get_compartments(
        self,
        parent_compartment_ocid=None,
        compartment_name=None,
        fetch_hosts_from_subcompartments=False,
    ):
        """
        Get the compartments based on the parameters passed. When compartment_name is None, all the compartments
        including the root compartment is returned.

        When compartment_name is passed, the compartment with that name and its hierarchy of compartments are returned
        if fetch_hosts_from_subcompartments is true.

        The tenancy is returned when compartment_name is the tenancy name.

        :param str parent_compartment_ocid: (optional)
            OCID of the parent compartment. If None, root compartment is assumed to be parent.
        :param str compartment_name: (optional)
            Name of the compartment. If None, all the compartments including the root compartment are returned.
        :param str fetch_hosts_from_subcompartments: (optional)
            Only applicable when compartment_name is specified. When set to true, the entire hierarchy of compartments
            of the given compartment is returned.
        :raises ServiceError: When the Service returned an Error response
        :raises MaximumWaitTimeExceededError: When maximum wait time is exceeded while invoking target_fn
        :return: list of :class:`~oci.identity.models.Compartment`
        """
        tenancy = call_with_backoff(
            self.identity_client.get_compartment, compartment_id=self.params["tenancy"]
        ).data
        all_compartments = [tenancy] + [
            compartment
            for compartment in list_all_resources(
                target_fn=self.identity_client.list_compartments,
                compartment_id=self.params["tenancy"],
                compartment_id_in_subtree=True,
            )
            if self.filter_resource(
                compartment, lifecycle_state=self.LIFECYCLE_ACTIVE_STATE
            )
        ]
        compartments = []

        # return all the compartments if compartment_name is not passed
        if not compartment_name:
            return all_compartments

        if compartment_name == tenancy.name:
            # return all the compartments when fetch_hosts_from_subcompartments is true
            if fetch_hosts_from_subcompartments:
                return all_compartments
            else:
                return [tenancy]

        compartment_with_name = None
        if not parent_compartment_ocid:
            parent_compartment_ocid = tenancy.id

        for compartment in all_compartments:
            if (
                compartment.name == compartment_name
                and compartment.compartment_id == parent_compartment_ocid
            ):
                compartment_with_name = compartment
                break

        if compartment_with_name:
            if fetch_hosts_from_subcompartments:
                # OCI SDK does not support fetching sub-compartments for non root compartments
                # So traverse the compartment tree to fetch all the sub compartments
                queue = deque()
                queue.append(compartment_with_name)
                while len(queue) > 0:
                    parent_compartment = queue.popleft()
                    compartments.append(parent_compartment)
                    child_compartments = [
                        compartment
                        for compartment in list_all_resources(
                            target_fn=self.identity_client.list_compartments,
                            compartment_id=parent_compartment.id,
                        )
                        if self.filter_resource(
                            compartment, lifecycle_state=self.LIFECYCLE_ACTIVE_STATE
                        )
                    ]
                    for child_compartment in child_compartments:
                        queue.append(child_compartment)
            else:
                compartments = [compartment_with_name]

        return compartments

    @staticmethod
    def filter_resource(resource, **kwargs):
        for key, val in kwargs.items():
            if getattr(resource, key, None) != val:
                return False
        return True

    def get_instances(self, compartment_ocids):

        instances = []

        if self.params["enable_parallel_processing"]:
            num_threads = min(len(compartment_ocids), self.params["max_thread_count"])
            self.log(
                "Parallel processing enabled. Getting instances from compartments in {0} threads.".format(
                    num_threads
                )
            )

            with self.pool(processes=num_threads) as pool:
                lists_of_instances = pool.map(
                    self.get_filtered_instances, compartment_ocids
                )
            for sublist in lists_of_instances:
                instances.extend(sublist)

        else:
            for compartment_ocid in compartment_ocids:
                instances.extend(self.get_filtered_instances(compartment_ocid))

        return instances

    def get_filtered_instances(self, compartment_ocid):
        try:
            self.log(
                "Listing all RUNNING instances from compartment:", compartment_ocid
            )
            instances = list_all_resources(
                target_fn=self.compute_client.list_instances,
                compartment_id=compartment_ocid,
                lifecycle_state="RUNNING",
            )
            self.log(
                "All RUNNING instances from compartment {0}:{1}".format(
                    compartment_ocid, instances
                )
            )
            if self.params["freeform_tags"]:
                instances = [
                    instance
                    for instance in instances
                    if all(
                        instance.freeform_tags.get(key) == value
                        for key, value in self.params["freeform_tags"].items()
                    )
                ]
                self.log(
                    "Instances in compartment {0} which match all the freeform tags: {1}".format(
                        compartment_ocid, instances
                    )
                )
            if self.params["defined_tags"]:
                instances = [
                    instance
                    for instance in instances
                    if all(
                        (instance.defined_tags.get(namespace, {})).get(key) == value
                        for namespace in self.params["defined_tags"]
                        for key, value in self.params["defined_tags"][namespace].items()
                    )
                ]
                self.log(
                    "Instances in compartment {0} which match all the freeform & defined tags: {1}".format(
                        compartment_ocid, instances
                    )
                )
            return instances
        except ServiceError as ex:
            if ex.status == 401:
                self.log(ex)
                raise
            self.log(ex)
            return []

    def get_host_name(self, vnic):
        if self.params["hostname_format"] == "fqdn":
            subnet = call_with_backoff(
                self.virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
            ).data
            vcn = call_with_backoff(
                self.virtual_nw_client.get_vcn, vcn_id=subnet.vcn_id
            ).data

            oraclevcn_domain_name = ".oraclevcn.com"
            fqdn = (
                vnic.hostname_label
                + "."
                + subnet.dns_label
                + "."
                + vcn.dns_label
                + oraclevcn_domain_name
            )
            self.log("FQDN for VNIC: {0} is {1}.".format(vnic.id, fqdn))
            return fqdn

        elif self.params["hostname_format"] == "private_ip":
            self.log(
                "Private IP for VNIC: {0} is {1}.".format(vnic.id, vnic.private_ip)
            )
            return vnic.private_ip

        self.log("Public IP for VNIC: {0} is {1}.".format(vnic.id, vnic.public_ip))
        return vnic.public_ip

    def build_inventory_for_instance(self, instance):
        """Build and return inventory for an instance"""
        try:
            self.log("Building inventory for instance {0}".format(instance.id))
            instance_inventory = {}
            compartment = self.compartments[instance.compartment_id]

            instance_vars = to_dict(instance)

            common_groups = {"all"}
            # Group by availability domain
            ad = self.sanitize(instance.availability_domain)
            common_groups.add(ad)

            # Group by compartments
            compartment_name = self.sanitize(compartment.name)
            common_groups.add(compartment_name)

            # Group by region
            region_grp = self.sanitize("region_" + instance.region)
            common_groups.add(region_grp)

            # Group by image OCID
            if hasattr(instance.source_details, "image_id"):
                common_groups.add(instance.source_details.image_id)

            # Group by instance shape
            shape_name = self.sanitize(instance.shape)
            common_groups.add(shape_name)

            # Group by freeform tags tag_key=value
            for key in instance.freeform_tags:
                tag_group_name = self.sanitize(
                    "tag_" + key + "=" + instance.freeform_tags[key]
                )
                common_groups.add(tag_group_name)

            # Group by defined tags
            for namespace in instance.defined_tags:
                for key in instance.defined_tags[namespace]:
                    defined_tag_group_name = self.sanitize(
                        namespace
                        + "#"
                        + key
                        + "="
                        + instance.defined_tags[namespace][key]
                    )
                    common_groups.add(defined_tag_group_name)

            # Group by metadata
            for key in instance.metadata:
                # Group using only custom metadata keys.
                if key not in ["ssh_authorized_keys", "user_data"]:
                    group_name = self.sanitize(key + "=" + instance.metadata[key])
                    common_groups.add(group_name)

            # Group by extended metadata
            for key in instance.extended_metadata:
                if key not in ["ssh_authorized_keys", "user_data"]:
                    ext_metadata_grp_name = self.sanitize(
                        key + "=" + str(instance.extended_metadata[key])
                    )
                    common_groups.add(ext_metadata_grp_name)

            vnic_attachments = [
                vnic_attachment
                for vnic_attachment in list_all_resources(
                    target_fn=self.compute_client.list_vnic_attachments,
                    compartment_id=compartment.id,
                    instance_id=instance.id,
                )
                if self.filter_resource(
                    vnic_attachment, lifecycle_state=self.LIFECYCLE_ATTACHED_STATE
                )
            ]

            for vnic_attachment in vnic_attachments:

                vnic = call_with_backoff(
                    self.virtual_nw_client.get_vnic, vnic_id=vnic_attachment.vnic_id
                ).data
                self.log(
                    "VNIC {0} is attached to instance {1}.".format(
                        vnic.id, vnic_attachment.instance_id
                    )
                )

                host_name = self.get_host_name(vnic)

                # Skip host which is not addressable using hostname_format
                if not host_name:
                    self.log(
                        "Skipped instance with OCID:" + vnic_attachment.instance_id
                    )
                    return None

                if self.args.host and self.args.host != host_name:
                    self.log("Skipped instance with hostname:" + host_name)
                    continue

                host_name = self.sanitize(host_name)

                groups = set(common_groups)

                subnet = call_with_backoff(
                    self.virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
                ).data
                groups.add(subnet.id)
                groups.add(subnet.vcn_id)

                # Group by security list
                for sec_list_id in subnet.security_list_ids:
                    groups.add(sec_list_id)

                self.log("Creating inventory for host {0}.".format(host_name))
                self.create_instance_inventory_for_host(
                    instance_inventory,
                    host_name,
                    vars=instance_vars,
                    groups=groups,
                    parents=[ad, subnet.vcn_id, region_grp, region_grp],
                    children=[subnet.id, subnet.id, ad, subnet.vcn_id],
                )

            return instance_inventory

        except ServiceError as ex:
            if ex.status == 401:
                self.log(ex)
                raise
            self.log(ex)

    @staticmethod
    def create_instance_inventory_for_host(
        instance_inventory, host_name, vars, groups, parents, children
    ):
        instance_inventory.setdefault(host_name, {"groups": {}, "vars": {}})
        instance_inventory[host_name]["vars"] = vars
        for group in groups:
            instance_inventory[host_name]["groups"].setdefault(group, {"children": []})
        for parent, child in zip(parents, children):
            instance_inventory[host_name]["groups"][parent]["children"].append(child)
        return instance_inventory

    def merge_instance_inventories(self, instance_inventories):
        """Merge all instance inventories into the main inventory"""
        for instance_inventory in instance_inventories:
            if instance_inventory:
                for host_name, host_inventory in instance_inventory.items():
                    self.add_host(
                        host_name,
                        vars=host_inventory["vars"],
                        groups=host_inventory["groups"],
                    )

    @contextmanager
    def pool(self, **kwargs):
        pool = ThreadPool(**kwargs)
        try:
            yield pool
        finally:
            pool.close()
            # wait for all the instances to be processed
            pool.join()
            # terminate the pool
            pool.terminate()

    def build_inventory(self):
        self.log("Building inventory.")

        try:
            # Compartments(including the root compartment) from which the instances are to be retrieved.
            self.compartments = {
                compartment.id: compartment
                for compartment in self.get_compartments(
                    parent_compartment_ocid=self.params["parent_compartment_ocid"],
                    compartment_name=self.params["compartment"],
                    fetch_hosts_from_subcompartments=self.params[
                        "fetch_hosts_from_subcompartments"
                    ],
                )
            }

            if not self.compartments:
                self.log("No compartments matching the criteria.")
                return

            self.log(
                "Building inventory for compartments {0}".format(self.compartments)
            )

            instances = self.get_instances(self.compartments)
            if not instances:
                self.log("No instances matching the criteria.")
                return

            self.log("Building inventory for instances {0}".format(instances))

            instance_inventories = []

            if self.params["enable_parallel_processing"]:
                num_threads = min(len(instances), self.params["max_thread_count"])
                self.log(
                    "Parallel processing enabled. Building individual instance inventories {0} threads.".format(
                        num_threads
                    )
                )
                with self.pool(processes=num_threads) as pool:
                    instance_inventories = pool.map(
                        self.build_inventory_for_instance, instances
                    )

            else:
                instance_inventories = [
                    self.build_inventory_for_instance(instance)
                    for instance in instances
                ]

            self.log("Instance inventories: {0}".format(instance_inventories))
            self.log("Merging instance inventories.")

            self.merge_instance_inventories(instance_inventories)

        except ServiceError as ex:
            if ex.status == 401:
                self.log(ex)
                self.fail(exit_code=1)
            self.log(ex)

    def fail(self, exit_code=1, message=None):
        if message:
            print(message)
        sys.exit(exit_code)

    def parse_cli_args(self):
        parser = argparse.ArgumentParser(
            description="Produce an Ansible Inventory file based on OCI"
        )

        parser.add_argument(
            "--list",
            action="store_true",
            default=True,
            help="List instances (default: True)",
        )

        parser.add_argument(
            "--host",
            action="store",
            help="Get all information about a compute instance",
        )

        parser.add_argument(
            "-config",
            "--config-file",
            action="store",
            dest="config_file",
            help="OCI config file location",
        )

        parser.add_argument(
            "--profile",
            action="store",
            dest="profile",
            help="OCI config profile for connecting to OCI",
        )

        parser.add_argument(
            "--compartment",
            action="store",
            help="Name of the compartment for which dynamic inventory must be generated. If you want "
            "to generate a dynamic inventory for the root compartment of the tenancy, specify the "
            "tenancy name as the name of the compartment.",
        )

        parser.add_argument(
            "--parent-compartment-ocid",
            action="store",
            help="Only valid when --compartment is set. Parent compartment ocid of the specified compartment."
            "Defaults to tenancy ocid.",
        )

        parser.add_argument(
            "--fetch-hosts-from-subcompartments",
            action="store_true",
            default=False,
            help="Only valid when --compartment is set. Default is false. When set to true, inventory "
            "is built with the entire hierarchy of the given compartment.",
        )

        parser.add_argument(
            "--refresh-cache",
            "-r",
            action="store_true",
            default=False,
            help="Force refresh of cache by making API requests to OCI. Use this option whenever you are "
            "building inventory with new filter options to avoid reading cached inventory. "
            "(default: False - use cache files)",
        )

        parser.add_argument(
            "--debug",
            action="store_true",
            default=False,
            help="Send debug messages to STDERR",
        )

        parser.add_argument(
            "--auth",
            action="store",
            choices=["api_key", "instance_principal"],
            help="The type of authentication to use for making API requests. By default, the API key "
            "in your config will be used. Set this option to `instance_principal` to use instance "
            "principal based authentication. This value can also be provided in the "
            "OCI_ANSIBLE_AUTH_TYPE environment variable.",
        )

        parser.add_argument(
            "--enable-parallel-processing",
            action="store_true",
            help="Inventory generation for tenants with huge number of instances might take a long time."
            "When this flag is set, the inventory script uses thread pools to parallelise the "
            "inventory generation.",
        )

        parser.add_argument(
            "--max-thread-count",
            action="store",
            type=int,
            help="Only valid when --enable-parallel-processing is set. When set, this script uses threads to "
            "improve the performance of building the inventory. This option specifies the maximum number of "
            "threads to use. Defaults to 50. This value can also be provided in the settings config file.",
        )

        parser.add_argument(
            "--freeform-tags",
            action="store",
            help='Freeform tags provided as a string in valid JSON format. Example: { "stage":  "dev", "app": "demo"} '
            "Use this option to build inventory of only those hosts which are tagged with all the specified "
            "key-value pairs.",
        )

        parser.add_argument(
            "--defined-tags",
            action="store",
            help="Defined tags provided as a string in valid JSON format. "
            'Example: {"namespace1": {"key1": "value1", "key2": "value2"}, "namespace2": {"key": "value"}} '
            "Use this option to build inventory of only those hosts which are tagged with all the specified "
            "key-value pairs.",
        )

        self.args = parser.parse_args()

    def read_settings_config(self, boolean_options, dict_options):
        if self.settings_config.has_section("oci"):
            for option in self.settings_config.options("oci"):
                if option in boolean_options:
                    self.params[option] = self.settings_config.getboolean("oci", option)
                elif option in dict_options:
                    self.params[option] = json.loads(
                        self.settings_config.get("oci", option)
                    )
                else:
                    self.params[option] = self.settings_config.get("oci", option)

    def sanitize(self, word):
        # regex represents an invalid non-alphanumeric character except UNDERSCORE, HASH, EQUALS and DOT
        regex = r"[^A-Za-z0-9_#=."
        if self.params["sanitize_names"]:
            if not self.params["replace_dash_in_names"]:
                # Add DASH as a valid character in regex.
                regex += r"-"

            # Replace all invalid characters with UNDERSCORE
            return re.sub(regex + "]", "_", word)
        return word

    def add_host(self, host, groups=None, vars=None):
        """Add host to the inventory"""
        if not groups:
            groups = {"all"}
        for group in groups:
            self.add_group(group, children=groups[group].setdefault("children", []))
            if host not in self.inventory[group]["hosts"]:
                self.inventory[group]["hosts"].append(host)
        if vars:
            self.add_host_vars(host, vars)

    def add_host_vars(self, host, vars):
        """Add vars to the host in inventory"""
        self.inventory["_meta"]["hostvars"][host] = vars

    def add_group(self, group, children=None):
        """Add group to the inventory"""
        self.inventory.setdefault(group, {"hosts": []})
        if children:
            for child in children:
                self.add_child_group(group, child)

    def add_child_group(self, parent, child):
        """Add child group to the inventory"""
        self.add_group(parent)
        children = self.inventory[parent].setdefault("children", [])
        if child not in children:
            children.append(child)


if __name__ == "__main__":
    if not HAS_OCI_PY_SDK:
        sys.exit(
            "OCI Python SDK is not installed. Try `pip install oci` to install OCI Python SDK."
        )
    OCIInventory()
