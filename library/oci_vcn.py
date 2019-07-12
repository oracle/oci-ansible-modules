#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_vcn
short_description: Manage Virtual Cloud Networks(VCN) in OCI
description:
    - This module allows the user to create, delete and update virtual cloud networks(VCNs) in OCI.
version_added: "2.5"
options:
    cidr_block:
        description: The CIDR IP address block of the VCN. Required when creating a VCN with I(state=present).
        required: false
    compartment_id:
        description: The OCID of the compartment to contain the VCN. Required when creating a VCN with I(state=present).
                     This option is mutually exclusive with I(vcn_id).
        type: str
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        type: str
        aliases: [ 'name' ]
    dns_label:
        description: A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to
                     form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example,
                     bminstance-1.subnet123.vcn1.oraclevcn.com). Not required to be unique, but it's a best practice
                     to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins
                     with a letter. The value cannot be changed.
        type: str
    state:
        description: Create or update a VCN with I(state=present). Use I(state=absent) to delete a VCN.
        type: str
        default: present
        choices: ['present', 'absent']
    vcn_id:
        description: The OCID of the VCN. Required when deleting a VCN with I(state=absent) or updating a VCN
                     with I(state=present). This option is mutually exclusive with I(compartment_id).
        type: str
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a VCN
  oci_vcn:
    cidr_block: '10.0.0.0/16'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_vcn
    dns_label: ansiblevcn

- name: Updates the specified VCN's display name
  oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_vcn

- name: Delete the specified VCN
  oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
vcn:
    description: Information about the VCN
    returned: On successful create and update operation
    type: dict
    sample: {
            "cidr_block": "10.0.0.0/16",
            compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "default_dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_security_list_id": "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
            "display_name": "ansible_vcn",
            "dns_label": "ansiblevcn",
            "id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_domain_name": "ansiblevcn.oraclevcn.com"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateVcnDetails
    from oci.core.models import UpdateVcnDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VcnHelperGen(OCIResourceHelperBase):
    @staticmethod
    def get_module_resource_id_param():
        return "vcn_id"

    def get_module_resource_id(self):
        return self.module.params.get("vcn_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn, vcn_id=self.module.params.get("vcn_id")
        )

    def list_resources(self):
        return oci_utils.list_all_resources(
            self.client.list_vcns,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_create_model(self):
        create_vcn_details = CreateVcnDetails()
        for attr in create_vcn_details.attribute_map:
            if self.module.params.get(attr) is not None:
                setattr(create_vcn_details, attr, self.module.params[attr])
        return create_vcn_details

    def create_resource(self):
        create_vcn_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.create_vcn, create_vcn_details=create_vcn_details
        )

    def get_update_model(self):
        update_vcn_details = UpdateVcnDetails()
        for attr in update_vcn_details.attribute_map:
            if self.module.params.get(attr) is not None:
                setattr(update_vcn_details, attr, self.module.params[attr])
        return update_vcn_details

    def update_resource(self):
        update_vcn_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_vcn,
            vcn_id=self.module.params.get("vcn_id"),
            update_vcn_details=update_vcn_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_vcn, vcn_id=self.module.params.get("vcn_id")
        )


VcnHelperCustom = get_custom_class("VcnHelperCustom")


class ResourceHelper(VcnHelperCustom, VcnHelperGen):
    pass


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            cidr_block=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            dns_label=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            vcn_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[["compartment_id", "vcn_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="vcn", service_client_class=VirtualNetworkClient
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()
    elif resource_helper.is_action():
        result = resource_helper.perform_action(module.params.get("state"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
