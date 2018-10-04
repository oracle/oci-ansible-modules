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
module: oci_cpe
short_description: Manage Customer-Premises Equipments(CPEs) in OCI
description:
    - This module allows the user to create, delete and update a customer-premises equipment(CPE) in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment to contain the CPE. Required when creating a CPE with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: [ 'name' ]
    state:
        description: Create or update a CPE with I(state=present). Use I(state=absent) to delete a CPE.
        required: false
        default: present
        choices: ['present', 'absent']
    cpe_id:
        description: The OCID of the CPE. Required when deleting a CPE with I(state=absent) or updating a CPE with
                     I(state=present).
        required: false
        aliases: [ 'id' ]
    ip_address:
        description: The public IP address of the on-premises router. Required to create a CPE with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_tags ]
'''

EXAMPLES = '''
- name: Create a CPE
  oci_cpe:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_cpe
    ip_address: "143.19.23.16"

- name: Update the specified CPE's display name
  oci_cpe:
    cpe_id: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_cpe

- name: Delete the specified CPE
  oci_cpe:
    id: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
'''

RETURN = '''
cpe:
    description: Information about the CPE
    returned: On successful operation
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_cpe",
            "freeform_tags": {},
            "id": "ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx",
            "ip_address": "143.19.23.16",
            "time_created": "2017-11-13T20:22:40.626000+00:00"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateCpeDetails
    from oci.core.models import UpdateCpeDetails
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_cpe(virtual_network_client, module):
    result = oci_utils.delete_and_wait(resource_type="cpe",
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_cpe,
                                       kwargs_get={"cpe_id": module.params["cpe_id"]},
                                       delete_fn=virtual_network_client.delete_cpe,
                                       kwargs_delete={"cpe_id": module.params["cpe_id"]},
                                       module=module,
                                       wait_applicable=False
                                       )
    return result


def update_cpe(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(resource_type="cpe",
                                                 get_fn=virtual_network_client.get_cpe,
                                                 kwargs_get={"cpe_id": module.params["cpe_id"]},
                                                 update_fn=virtual_network_client.update_cpe,
                                                 primitive_params_update=['cpe_id'],
                                                 kwargs_non_primitive_update={
                                                     UpdateCpeDetails: "update_cpe_details"},
                                                 module=module,
                                                 update_attributes=UpdateCpeDetails().attribute_map.keys()
                                                 )
    return result


def create_cpe(virtual_network_client, module):
    create_cpe_details = CreateCpeDetails()
    for attribute in create_cpe_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_cpe_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(resource_type="cpe",
                                       create_fn=virtual_network_client.create_cpe,
                                       kwargs_create={"create_cpe_details": create_cpe_details},
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_cpe,
                                       get_param="cpe_id",
                                       module=module,
                                       wait_applicable=False
                                       )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_create=True)
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        display_name=dict(type='str', required=False, aliases=['name']),
        state=dict(type='str', required=False, default='present', choices=['absent', 'present']),
        cpe_id=dict(type='str', required=False, aliases=['id']),
        ip_address=dict(type='str', required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ('state', 'absent', ['cpe_id'])
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    virtual_network_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    exclude_attributes = {'display_name': True}
    state = module.params['state']

    if state == 'absent':
        result = delete_cpe(virtual_network_client, module)

    else:
        cpe_id = module.params['cpe_id']
        if cpe_id is not None:
            result = update_cpe(virtual_network_client, module)
        else:
            result = oci_utils.check_and_create_resource(resource_type='cpe',
                                                         create_fn=create_cpe,
                                                         kwargs_create={
                                                             'virtual_network_client': virtual_network_client,
                                                             'module': module},
                                                         list_fn=virtual_network_client.list_cpes,
                                                         kwargs_list={'compartment_id': module.params['compartment_id']
                                                                      },
                                                         module=module,
                                                         model=CreateCpeDetails(),
                                                         exclude_attributes=exclude_attributes)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
