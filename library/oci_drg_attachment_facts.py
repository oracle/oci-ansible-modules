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
module: oci_drg_attachment_facts
short_description: Retrieve facts of Dynamic Routing Gateway(DRG) attachments
description:
    - This module retrieves information of the specified dynamic routing gateway(DRG) attachment or lists all the DRG
      attachments in the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the DRG attachments in the
                     compartment.
        required: false
    drg_attachment_id:
        description: The OCID of the DRG attachment. I(drg_attachment_id) is required to get a specific DRG attachment's
                     information.
        required: false
        aliases: [ 'id' ]
    vcn_id:
        description: The OCID of the VCN. Use I(vcn_id) with I(compartment_id) to filter DRG attachments by VCN.
        required: false
    drg_id:
        description: The OCID of the DRG. Use I(drg_id) with I(compartment_id) to filter DRG attachments by DRG.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
'''

EXAMPLES = '''
- name: Get all the DRG attachments in a compartment
  oci_drg_attachment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific DRG_attachment using its OCID
  oci_drg_attachment_facts:
    drg_attachment_id: ocid1.drgattachment.oc1.phx.xxxxxEXAMPLExxxxx

- name: Get DRG attachment attached to a VCN in a compartment
  oci_drg_attachment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx'
'''

RETURN = '''
drg_attachments:
    description: List of DRG attachment details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the DRG attachment.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the DRG attachment.
            returned: always
            type: string
            sample: ansible_drg_attachment
        drg_id:
            description: The OCID of the DRG.
            returned: always
            type: string
            sample: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
        id:
            description: OCID of the DRG attachment.
            returned: always
            type: string
            sample: ocid1.drgattachment.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: Current state of the DRG attachment.
            returned: always
            type: string
            sample: ATTACHED
        time_created:
            description: The date and time the DRG_attachment was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        vcn_id:
            description: The OCID of the VCN.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible-drg-attachment",
            "drg_id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "id": "ocid1.drgatttachment.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "ATTACHED",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
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
        drg_attachment_id=dict(type='str', required=False, aliases=['id']),
        drg_id=dict(type='str', required=False),
        vcn_id=dict(type='str', required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[
            ['compartment_id', 'drg_attachment_id']
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    virtual_network_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    drg_attachment_id = module.params['drg_attachment_id']
    result = []

    try:
        if drg_attachment_id is not None:
            result = [to_dict(oci_utils.call_with_backoff(virtual_network_client.get_drg_attachment,
                                                          drg_attachment_id=drg_attachment_id).data)]
        else:
            compartment_id = module.params['compartment_id']
            result = to_dict(oci_utils.list_all_resources(virtual_network_client.list_drg_attachments,
                                                          vcn_id=module.params['vcn_id'],
                                                          drg_id=module.params['drg_id'],
                                                          display_name=module.params['display_name'],
                                                          compartment_id=compartment_id))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(drg_attachments=result)


if __name__ == '__main__':
    main()
