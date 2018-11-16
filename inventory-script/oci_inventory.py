#!/usr/bin/env python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

'''
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
                        [--refresh-cache] [--debug]
                        [--auth {api_key,instance_principal}]

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
  --refresh-cache, -r   Force refresh of cache by making API requests to OCI
                        (default: False - use cache files)
  --debug               Send debug messages to STDERR
  --auth {api_key,instance_principal}
                        The type of authentication to use for making API
                        requests. By default, the API key in your config will
                        be used. Set this option to `instance_principal` to
                        use instance principal based authentication. This
                        value can also be provided in the
                        OCI_ANSIBLE_AUTH_TYPE environment variable.

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
names are replaced with an UNDERSCORE(_) when the inventory is generated, so that the names can be used as Ansible
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
'''

from __future__ import print_function
import argparse
import json
import os
import re
import sys
from time import time
from six.moves import configparser

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

__version__ = '1.3.0'


def _get_retry_strategy():
    retry_strategy_builder = RetryStrategyBuilder(max_attempts_check=True, max_attempts=10,
                                                  retry_max_wait_between_calls_seconds=30,
                                                  retry_base_sleep_time_seconds=3,
                                                  backoff_type=oci.retry.BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE)
    retry_strategy_builder.add_service_error_check(
        service_error_retry_config={429: [], 400: ['QuotaExceeded', 'LimitExceeded']},
        service_error_retry_on_any_5xx=True)
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
        kwargs['retry_strategy'] = _get_retry_strategy()
    try:
        return fn(**kwargs)
    except TypeError as te:
        if "unexpected keyword argument" in str(te):
            del kwargs["retry_strategy"]
            return fn(**kwargs)


def _is_instance_principal_auth(params):
    # check if auth is set to `instance_principal`.
    return params['auth'] == "instance_principal"


def create_service_client(params, service_client_class):
    kwargs = {}
    if _is_instance_principal_auth(params):
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        except Exception as ex:
            message = "Failed retrieving certificates from localhost. Instance principal based authentication is only" \
                      "possible from within OCI compute instances. Exception: {0}".format(str(ex))
            OCIInventory().log(message)
            sys.exit()
        kwargs['signer'] = signer

    # Create service client class with the signer
    client = service_client_class(params, **kwargs)

    return client


class OCIInventory:
    def __init__(self):
        self.inventory = {}  # Ansible Inventory
        self.config = {}

        self.params = {
            "ini_file": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'oci_inventory.ini'),
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
            "debug": False,
            "hostname_format": "public_ip",
            "sanitize_names": True,
            "replace_dash_in_names": False,
            "auth": "api_key"
        }
        self.parse_cli_args()

        if self.args.debug:
            self.params["debug"] = True
            self.log("Executing in debug mode.")

        if 'OCI_INI_PATH' in os.environ:
            oci_ini_file_path = os.path.expanduser(os.path.expandvars(os.environ.get('OCI_INI_PATH')))
            if os.path.isfile(oci_ini_file_path):
                self.params["ini_file"] = oci_ini_file_path

        self.settings_config = configparser.ConfigParser()
        self.settings_config.read(self.params["ini_file"])

        # Preference order: CLI args > environment variable > settings from config file.
        if "config_file" in self.args and getattr(self.args, "config_file") is not None:
            self.params['config_file'] = os.path.expanduser(self.args.config_file)
        elif 'OCI_CONFIG_FILE' in os.environ:
            self.params['config_file'] = os.path.expanduser(os.path.expandvars(os.environ.get('OCI_CONFIG_FILE')))
        elif self.settings_config.has_option('oci', 'config_file'):
            self.params['config_file'] = os.path.expanduser(self.settings_config.get('oci', 'config_file'))

        if "profile" in self.args and getattr(self.args, "profile") is not None:
            self.params['profile'] = self.args.profile
        elif 'OCI_CONFIG_PROFILE' in os.environ:
            self.params['profile'] = os.environ.get('OCI_CONFIG_PROFILE')
        elif self.settings_config.has_option('oci', 'profile'):
            self.params['profile'] = self.settings_config.get('oci', 'profile')

        self.read_config()
        self.read_settings_config()
        self.read_env_vars()
        self.read_cli_args()

        self.log("Using following parameters for OCI dynamic inventory:")
        self.log(self.params)

        self.compute_client = create_service_client(self.params, ComputeClient)
        self.identity_client = create_service_client(self.params, IdentityClient)
        self.virtual_nw_client = create_service_client(self.params, VirtualNetworkClient)

        # For the case, when auth="instance_principal", tenancy_id is not available.
        if self.params['auth'] == "instance_principal":
            self.params['tenancy'] = self.get_tenancy_id()

        self.params['cache_file'] = os.path.join(self.params['cache_dir'], "ansible-oci.cache")

        if not self.args.refresh_cache and self.is_cache_valid():
            self.log("Reading inventory from cache.")
            self.inventory = self.read_from_cache()
        else:
            self.build_inventory()
            self.write_to_cache(self.inventory)

        if self.args.host:
            if self.args.host in self.inventory['_meta']['hostvars']:
                print(json.dumps(self.inventory['_meta']['hostvars'][self.args.host], sort_keys=True, indent=2))
            else:
                self.log("Either the specified host does not exist or its facts cannot be retrieved.")
                print({})

        else:
            print(json.dumps(self.inventory, sort_keys=True, indent=2))

    def log(self, *args, **kwargs):
        if self.params["debug"]:
            print(*args, file=sys.stderr, **kwargs)

    def get_tenancy_id(self):
        # Get the instance metadata using the HTTP endpoint.
        GET_TENANCY_ID_URL = 'http://169.254.169.254/opc/v1/instance/compartmentId'
        response = requests.get(GET_TENANCY_ID_URL)
        compartment_id = response.text
        # In case of nested compartments, the immediate compartment may not be the root compartment.
        tenancy_id = call_with_backoff(self.identity_client.get_compartment,
                                       compartment_id=compartment_id).data.compartment_id
        return tenancy_id

    def read_config(self):
        if os.path.isfile(self.params['config_file']):
            self.config = oci.config.from_file(file_location=self.params['config_file'],
                                               profile_name=self.params['profile'])

        self.config["additional_user_agent"] = "Oracle-Ansible/{0}".format(__version__)

        for setting in self.config:
            self.params[setting] = self.config[setting]

    def read_env_vars(self):
        EnvParamsMapping = dict(
            OCI_CONFIG_FILE='config_file',
            OCI_INI_PATH='ini_path',
            OCI_TENANCY='tenancy',
            OCI_REGION='region',
            OCI_CACHE_DIR='cache_dir',
            OCI_CACHE_MAX_AGE='cache_max_age',
            OCI_HOSTNAME_FORMAT='hostname_format',
            OCI_USER_ID='user',
            OCI_USER_FINGERPRINT='fingerprint',
            OCI_USER_KEY_FILE='key_file',
            OCI_USER_KEY_PASS_PHRASE='pass_phrase',
            OCI_CONFIG_PROFILE='profile',
            OCI_ANSIBLE_AUTH_TYPE='auth'
        )

        for env_var in os.environ:
            if env_var in EnvParamsMapping:
                self.params[EnvParamsMapping[env_var]] = os.environ.get(env_var)

    def read_cli_args(self):
        for setting in vars(self.args):
            if getattr(self.args, setting) is not None:
                self.params[setting] = getattr(self.args, setting)

    def is_cache_valid(self):
        if os.path.isfile(self.params['cache_file']):
            mod_time = os.path.getmtime(self.params['cache_file'])
            current_time = time()
            if (mod_time + float(self.params['cache_max_age'])) > current_time:
                return True
            else:
                self.log("Cache is outdated.")
        else:
            self.log("Cache file is invalid.")
        return False

    def read_from_cache(self):
        with open(self.params['cache_file'], 'r') as cache:
            return json.loads(cache.read())

    def write_to_cache(self, data):
        json_data = json.dumps(data, sort_keys=True, indent=2)
        with open(self.params['cache_file'], 'w') as f:
            f.write(json_data)

    def get_compartment(self, compartment_name):
        compartments = list_all_resources(target_fn=self.identity_client.list_compartments,
                                          compartment_id=self.params['tenancy'])
        for compartment in compartments:
            if compartment.name == compartment_name:
                return compartment
        return None

    def get_host_name(self, vnic):
        if self.params['hostname_format'] == 'fqdn':
            subnet = self.subnets.setdefault(vnic.subnet_id,
                                             call_with_backoff(self.virtual_nw_client.get_subnet,
                                                               subnet_id=vnic.subnet_id).data)

            vcn = self.vcns.setdefault(subnet.vcn_id,
                                       call_with_backoff(self.virtual_nw_client.get_vcn,
                                                         vcn_id=subnet.vcn_id).data)
            oraclevcn_domain_name = ".oraclevcn.com"
            fqdn = vnic.hostname_label + "." + subnet.dns_label + "." + vcn.dns_label + oraclevcn_domain_name
            self.log("FQDN for VNIC: {0} is {1}.".format(vnic.id, fqdn))
            return fqdn

        elif self.params['hostname_format'] == 'private_ip':
            self.log("Private IP for VNIC: {0} is {1}.".format(vnic.id, vnic.private_ip))
            return vnic.private_ip

        self.log("Public IP for VNIC: {0} is {1}.".format(vnic.id, vnic.public_ip))
        return vnic.public_ip

    def build_inventory(self):
        self.log("Building inventory.")
        self.inventory = {
            'all': {
                'hosts': [],
                'vars': {}
            },
            '_meta': {'hostvars': {}}
        }

        # Maps to store vcn & subnet information keyed by OCID. This serves to reduce API calls.
        self.vcns = {}
        self.subnets = {}

        # Compartments(including the root compartment) from which the instances are to be retrieved.
        compartments = []
        tenancy = call_with_backoff(self.identity_client.get_tenancy,
                                    tenancy_id=self.params['tenancy']).data
        # If compartment name is specified.
        if self.params['compartment'] is not None:
            # Check if the specified compartment name is same as tenancy's name.
            if self.params['compartment'] == tenancy.name:
                compartments = [tenancy]
            else:
                # Get compartment with the specified name.
                compartment = self.get_compartment(self.params['compartment'])
                if compartment is not None:
                    compartments = [compartment]

        else:
            compartments = list_all_resources(target_fn=self.identity_client.list_compartments,
                                              compartment_id=self.params['tenancy'])
            # Add root compartment to the compartment list as instance can also be launched in the root compartment.
            compartments.append(tenancy)

        for compartment in compartments:
            try:
                vnic_attachments = list_all_resources(target_fn=self.compute_client.list_vnic_attachments,
                                                      compartment_id=compartment.id)

                for vnic_attachment in vnic_attachments:
                    if vnic_attachment.lifecycle_state in ["ATTACHED"]:

                        vnic = call_with_backoff(self.virtual_nw_client.get_vnic,
                                                 vnic_id=vnic_attachment.vnic_id).data
                        self.log("VNIC {0} is attached to instance {1}.".format(vnic.id, vnic_attachment.instance_id))

                        host_name = self.get_host_name(vnic)

                        # Skip host which is not addressable using hostname_format
                        if not host_name:
                            self.log("Skipped instance with OCID:" + vnic_attachment.instance_id)
                            continue

                        host_name = self.sanitize(host_name)

                        self.inventory['all']['hosts'].append(host_name)

                        # Group by availability domain
                        ad = self.sanitize(vnic_attachment.availability_domain)
                        self.inventory.setdefault(ad, {"hosts": []})
                        self.inventory[ad]["hosts"].append(host_name)

                        # Group by compartments
                        compartment_name = self.sanitize(compartment.name)
                        self.inventory.setdefault(compartment_name, {"hosts": []})
                        self.inventory[compartment_name]["hosts"].append(host_name)

                        # Group by subnet
                        subnet = self.subnets.setdefault(vnic.subnet_id,
                                                         call_with_backoff(self.virtual_nw_client.get_subnet,
                                                                           subnet_id=vnic.subnet_id).data)
                        self.inventory.setdefault(subnet.id, {"hosts": []})
                        self.inventory[subnet.id]["hosts"].append(host_name)
                        self.add_child_group(ad, subnet.id)

                        # Group by vcn
                        vcn = self.vcns.setdefault(subnet.vcn_id,
                                                   call_with_backoff(self.virtual_nw_client.get_vcn,
                                                                     vcn_id=subnet.vcn_id).data)
                        self.inventory.setdefault(vcn.id, {"hosts": []})
                        self.inventory[vcn.id]["hosts"].append(host_name)
                        self.add_child_group(vcn.id, subnet.id)

                        # Group by security list
                        for sec_list_id in subnet.security_list_ids:
                            self.inventory.setdefault(sec_list_id, {"hosts": []})
                            self.inventory[sec_list_id]["hosts"].append(host_name)

                        # Group by region
                        instance = call_with_backoff(self.compute_client.get_instance,
                                                     instance_id=vnic_attachment.instance_id).data
                        region_grp = self.sanitize("region_" + instance.region)
                        self.inventory.setdefault(region_grp, {"hosts": []})
                        self.inventory[region_grp]["hosts"].append(host_name)

                        self.add_child_group(region_grp, ad)
                        self.add_child_group(region_grp, vcn.id)

                        # Group by image OCID
                        if hasattr(instance.source_details, "image_id"):
                            self.inventory.setdefault(instance.source_details.image_id, {"hosts": []})
                            self.inventory[instance.source_details.image_id]["hosts"].append(host_name)

                        # Group by instance shape
                        shape_name = self.sanitize(instance.shape)
                        self.inventory.setdefault(shape_name, {"hosts": []})
                        self.inventory[shape_name]["hosts"].append(host_name)

                        # Group by freeform tags tag_key=value
                        for key in instance.freeform_tags:
                            tag_group_name = self.sanitize("tag_" + key + "=" + instance.freeform_tags[key])
                            self.inventory.setdefault(tag_group_name, {"hosts": []})
                            self.inventory[tag_group_name]["hosts"].append(host_name)

                        # Group by defined tags
                        for namespace in instance.defined_tags:
                            for key in instance.defined_tags[namespace]:
                                defined_tag_group_name = self.sanitize(namespace + "#" + key + "=" +
                                                                       instance.defined_tags[namespace][key])
                                self.inventory.setdefault(defined_tag_group_name, {"hosts": []})
                                self.inventory[defined_tag_group_name]["hosts"].append(host_name)

                        # Group by metadata
                        for key in instance.metadata:
                            # Group using only custom metadata keys.
                            if key not in ["ssh_authorized_keys", "user_data"]:
                                group_name = self.sanitize(key + "=" + instance.metadata[key])
                                self.inventory.setdefault(group_name, {"hosts": []})
                                self.inventory[group_name]["hosts"].append(host_name)

                        # Group by extended metadata
                        for key in instance.extended_metadata:
                            ext_metadata_grp_name = self.sanitize(key + "=" + str(instance.extended_metadata[key]))
                            self.inventory.setdefault(ext_metadata_grp_name, {"hosts": []})
                            self.inventory[ext_metadata_grp_name]["hosts"].append(host_name)

                        self.inventory['_meta']['hostvars'][host_name] = to_dict(instance)

            except ServiceError as ex:
                if ex.status == 401:
                    self.log(ex)
                    sys.exit()
                self.log(ex)

    def parse_cli_args(self):
        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file based on OCI')

        parser.add_argument('--list',
                            action='store_true',
                            default=True,
                            help='List instances (default: True)')

        parser.add_argument('--host',
                            action='store',
                            help='Get all information about a compute instance')

        parser.add_argument('-config',
                            '--config-file',
                            action='store',
                            dest='config_file',
                            help='OCI config file location')

        parser.add_argument('--profile',
                            action='store',
                            dest='profile',
                            help='OCI config profile for connecting to OCI')

        parser.add_argument('--compartment',
                            action='store',
                            help='Name of the compartment for which dynamic inventory must be generated. If you want '
                                 'to generate a dynamic inventory for the root compartment of the tenancy, specify the '
                                 'tenancy name as the name of the compartment.')

        parser.add_argument('--refresh-cache',
                            '-r',
                            action='store_true',
                            default=False,
                            help='Force refresh of cache by making API requests to OCI (default: False - use cache '
                                 'files)')

        parser.add_argument('--debug',
                            action='store_true',
                            default=False,
                            help='Send debug messages to STDERR')

        parser.add_argument('--auth',
                            action='store',
                            choices=['api_key', 'instance_principal'],
                            help='The type of authentication to use for making API requests. By default, the API key '
                                 'in your config will be used. Set this option to `instance_principal` to use instance '
                                 'principal based authentication. This value can also be provided in the '
                                 'OCI_ANSIBLE_AUTH_TYPE environment variable.')

        self.args = parser.parse_args()

    def read_settings_config(self):
        boolean_options = ["sanitize_names", "replace_dash_in_names"]
        if self.settings_config.has_section('oci'):
            for option in self.settings_config.options('oci'):
                if option in boolean_options:
                    self.params[option] = self.settings_config.getboolean('oci', option)
                else:
                    self.params[option] = self.settings_config.get('oci', option)

    def add_child_group(self, parent, child):
        children = self.inventory[parent].setdefault('children', [])
        if child not in children:
            children.append(child)

    def sanitize(self, word):
        # regex represents an invalid non-alphanumeric character except UNDERSCORE, HASH, EQUALS and DOT
        regex = r"[^A-Za-z0-9_#=."
        if self.params['sanitize_names']:
            if not self.params['replace_dash_in_names']:
                # Add DASH as a valid character in regex.
                regex += r"-"

            # Replace all invalid characters with UNDERSCORE
            return re.sub(regex + "]", "_", word)
        return word


if __name__ == '__main__':
    if not HAS_OCI_PY_SDK:
        sys.exit('OCI Python SDK is not installed. Try `pip install oci` to install OCI Python SDK.')
    OCIInventory()
