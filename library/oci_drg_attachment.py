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
module: oci_drg_attachment
short_description: Manage Dynamic Routing Gateways(DRG) attachments in OCI
description:
    - This module allows the user to create, delete and update a dynamic routing gateway(DRG) attachment in OCI.
version_added: "2.5"
options:
    drg_id:
        description: The OCID of the DRG. Required when creating a DRG attachment with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    drg_attachment_id:
        description: The OCID of the DRG attachment. Required when deleting a DRG attachment with I(state=absent) or
                     updating a DRG attachment with I(state=present).
        required: false
        aliases: [ 'id' ]
    state:
        description: Create or update a DRG attachment with I(state=present). Use I(state=absent) to delete a DRG
                     attachment.
        required: false
        default: present
        choices: ['present', 'absent']
    vcn_id:
        description: The OCID of the VCN. Required when creating a DRG attachment with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
'''

EXAMPLES = '''
- name: Attach a DRG to a VCN
  oci_drg_attachment:
    drg_id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    name: sample-attachment

- name: Update the specified DRG attachment's display name
  oci_drg_attachment:
    id: ocid1.drgatttachment.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible-drg-attachment

- name: Delete DRG attachment to detach the corresponding DRG from the VCN
  oci_drg_attachment:
    id: ocid1.drgatttachment.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
'''

RETURN = '''
drg_attachment:
    description: Information about the DRG attachment
    returned: On successful operation
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible-drg-attachment",
            "drg_id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "id": "ocid1.drgatttachment.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "ATTACHED",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateDrgAttachmentDetails
    from oci.core.models import UpdateDrgAttachmentDetails
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_drg_attachment(virtual_network_client, module):
    result = oci_utils.delete_and_wait(resource_type="drg_attachment",
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_drg_attachment,
                                       kwargs_get={"drg_attachment_id": module.params["drg_attachment_id"]},
                                       delete_fn=virtual_network_client.delete_drg_attachment,
                                       kwargs_delete={"drg_attachment_id": module.params["drg_attachment_id"]},
                                       module=module
                                       )
    return result


def update_drg_attachment(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(resource_type="drg_attachment",
                                                 get_fn=virtual_network_client.get_drg_attachment,
                                                 kwargs_get={"drg_attachment_id": module.params["drg_attachment_id"]},
                                                 update_fn=virtual_network_client.update_drg_attachment,
                                                 primitive_params_update=['drg_attachment_id'],
                                                 kwargs_non_primitive_update={
                                                     UpdateDrgAttachmentDetails: "update_drg_attachment_details"},
                                                 module=module,
                                                 update_attributes=UpdateDrgAttachmentDetails().attribute_map.keys()
                                                 )
    return result


def create_drg_attachment(virtual_network_client, module):
    create_drg_attachment_details = CreateDrgAttachmentDetails()
    for attribute in create_drg_attachment_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_drg_attachment_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(resource_type="drg_attachment",
                                       create_fn=virtual_network_client.create_drg_attachment,
                                       kwargs_create={"create_drg_attachment_details": create_drg_attachment_details},
                                       client=virtual_network_client,
                                       get_fn=virtual_network_client.get_drg_attachment,
                                       get_param="drg_attachment_id",
                                       module=module
                                       )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(supports_create=True, supports_wait=True)
    module_args.update(dict(
        drg_attachment_id=dict(type='str', required=False, aliases=['id']),
        display_name=dict(type='str', required=False, aliases=['name']),
        state=dict(type='str', required=False, default='present', choices=['absent', 'present']),
        drg_id=dict(type='str', required=False),
        vcn_id=dict(type='str', required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ('state', 'absent', ['drg_attachment_id'])
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    virtual_network_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    exclude_attributes = {'display_name': True}
    state = module.params['state']

    if state == 'absent':
        result = delete_drg_attachment(virtual_network_client, module)

    else:
        drg_attachment_id = module.params['drg_attachment_id']
        if drg_attachment_id is not None:
            result = update_drg_attachment(virtual_network_client, module)
        else:
            # To list existing DRG attachments, compartment_id is required.
            # DRG attachment is created in same compartment as the VCN. Retrieve VCN details to get compartment_id.
            compartment_id = oci_utils.call_with_backoff(virtual_network_client.get_vcn,
                                                         vcn_id=module.params['vcn_id']
                                                         ).data.compartment_id

            result = oci_utils.check_and_create_resource(resource_type='drg_attachment',
                                                         create_fn=create_drg_attachment,
                                                         kwargs_create={
                                                             'virtual_network_client': virtual_network_client,
                                                             'module': module},
                                                         list_fn=virtual_network_client.list_drg_attachments,
                                                         kwargs_list={'compartment_id': compartment_id,
                                                                      'vcn_id': module.params['vcn_id'],
                                                                      'drg_id': module.params['drg_id']
                                                                      },
                                                         module=module,
                                                         model=CreateDrgAttachmentDetails(),
                                                         exclude_attributes=exclude_attributes)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
