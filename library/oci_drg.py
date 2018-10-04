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
module: oci_drg
short_description: Manage Dynamic Routing Gateways(DRGs) in OCI
description:
    - This module allows the user to create, delete and update a dynamic routing gateway(DRG) in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment to contain the DRG. Required when creating a DRG with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: [ 'name' ]
    state:
        description: Create or update a DRG with I(state=present). Use I(state=absent) to delete a DRG.
        required: false
        default: present
        choices: ['present', 'absent']
    drg_id:
        description: The OCID of the DRG. Required when deleting a DRG with I(state=absent) or updating a DRG with
                     I(state=present).
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
'''

EXAMPLES = '''
- name: Create a DRG
  oci_drg:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_drg

- name: Update the specified DRG's display name
  oci_drg:
    drg_id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_drg

- name: Delete the specified DRG
  oci_drg:
    id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
'''

RETURN = '''
drg:
    description: Information about the DRG
    returned: On successful operation
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_drg",
            "freeform_tags": {},
            "id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "time_created": "2017-11-13T20:22:40.626000+00:00"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateDrgDetails
    from oci.core.models import UpdateDrgDetails
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_drg(virtual_network_client, module):
    result = oci_utils.delete_and_wait(resource_type="drg",
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_drg,
                                       kwargs_get={"drg_id": module.params["drg_id"]},
                                       delete_fn=virtual_network_client.delete_drg,
                                       kwargs_delete={"drg_id": module.params["drg_id"]},
                                       module=module
                                       )
    return result


def update_drg(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(resource_type="drg",
                                                 get_fn=virtual_network_client.get_drg,
                                                 kwargs_get={"drg_id": module.params["drg_id"]},
                                                 update_fn=virtual_network_client.update_drg,
                                                 primitive_params_update=['drg_id'],
                                                 kwargs_non_primitive_update={
                                                     UpdateDrgDetails: "update_drg_details"},
                                                 module=module,
                                                 update_attributes=UpdateDrgDetails().attribute_map.keys()
                                                 )
    return result


def create_drg(virtual_network_client, module):
    create_drg_details = CreateDrgDetails()
    for attribute in create_drg_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_drg_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(resource_type="drg",
                                       create_fn=virtual_network_client.create_drg,
                                       kwargs_create={"create_drg_details": create_drg_details},
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_drg,
                                       get_param="drg_id",
                                       module=module
                                       )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_create=True, supports_wait=True)
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        display_name=dict(type='str', required=False, aliases=['name']),
        state=dict(type='str', required=False, default='present', choices=['absent', 'present']),
        drg_id=dict(type='str', required=False, aliases=['id'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ('state', 'absent', ['drg_id'])
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    virtual_network_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    exclude_attributes = {'display_name': True}
    state = module.params['state']

    if state == 'absent':
        result = delete_drg(virtual_network_client, module)

    else:
        drg_id = module.params['drg_id']
        if drg_id is not None:
            result = update_drg(virtual_network_client, module)
        else:
            result = oci_utils.check_and_create_resource(resource_type='drg',
                                                         create_fn=create_drg,
                                                         kwargs_create={
                                                             'virtual_network_client': virtual_network_client,
                                                             'module': module},
                                                         list_fn=virtual_network_client.list_drgs,
                                                         kwargs_list={'compartment_id': module.params['compartment_id']
                                                                      },
                                                         module=module,
                                                         model=CreateDrgDetails(),
                                                         exclude_attributes=exclude_attributes)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
