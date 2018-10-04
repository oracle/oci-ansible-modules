#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_vcn_facts
short_description: Retrieve facts of Virtual Cloud Networks(VCNs)
description:
    - This module retrieves information of a specified virtual cloud network(VCN) or lists all the VCNs in the
      specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the VCNs in the compartment.
        required: false
    vcn_id:
        description: The OCID of the VCN. I(vcn_id) is required to get a specific VCN's information.
        required: false
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
'''

EXAMPLES = '''
- name: Get all the VCNs in a compartment
  oci_vcn_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific VCN using its OCID
  oci_vcn_facts:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx

- name: Get VCNs in a compartment having the specified display name
  oci_vcn_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: 'oci_ansible_vcn'
'''

RETURN = '''
vcns:
    description: List of VCN details
    returned: always
    type: complex
    contains:
        cidr_block:
            description: The CIDR IP address block of the VCN.
            returned: always
            type: string
            sample: 10.0.0.0/16
        compartment_id:
            description: The OCID of the compartment containing the VCN.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        default_dhcp_options_id:
            description: The OCID for the VCN's default set of DHCP options.
            returned: always
            type: string
            sample: ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx
        default_route_table_id:
            description: The OCID for the VCN's default route table.
            returned: always
            type: string
            sample: ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx
        default_security_list_id:
            description: The OCID for the VCN's default security list.
            returned: always
            type: string
            sample: ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the VCN.
            returned: always
            type: string
            sample: ansible_vcn
        dns_label:
            description: A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS \
                        label to form a fully qualified domain name (FQDN) for each VNIC within this subnet.
            returned: always
            type: string
            sample: ansiblevcn
        id:
            description: OCID of the VCN.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: Current state of the VCN.
            returned: always
            type: string
            sample: AVAILABLE
        time_created:
            description: The date and time the VCN was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        vcn_domain_name:
            description: The VCN's domain name, which consists of the VCN's DNS label, and the oraclevcn.com domain.
            returned: always
            type: string
            sample: ansiblevcn.oraclevcn.com
    sample: [{
            "cidr_block": "10.0.0.0/16",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "default_dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
            "default_security_list_id": "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
            "display_name": "ansible_vcn",
            "dns_label": "ansiblevcn",
            "id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_domain_name": "ansiblevcn.oraclevcn.com"
        }]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        vcn_id=dict(type='str', required=False),
        lifecycle_state=dict(type='str', required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    virtual_network_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    vcn_id = module.params['vcn_id']
    compartment_id = module.params['compartment_id']
    result = []

    if vcn_id is not None:
        try:
            result = [to_dict(oci_utils.call_with_backoff(virtual_network_client.get_vcn, vcn_id=vcn_id).data)]
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    elif compartment_id is not None:
        try:
            optional_list_method_params = ['display_name', 'lifecycle_state']
            optional_kwargs = {param: module.params[param] for param in optional_list_method_params
                               if module.params.get(param) is not None}
            result = to_dict(oci_utils.list_all_resources(virtual_network_client.list_vcns,
                                                          compartment_id=compartment_id, **optional_kwargs))
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    else:
        module.fail_json(msg="Specify a compartment_id to get all the VCNs in the compartment or a vcn_id to retrieve \
                            a specific VCN")

    module.exit_json(vcns=result)


if __name__ == '__main__':
    main()
