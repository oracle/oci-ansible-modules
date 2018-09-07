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
module: oci_compartment_facts
short_description: Retrieve details of a compartment or all the compartments in a tenancy in OCI
description:
    - This module allows the user to retrieve details of a specific compartment in a tenancy or all the compartments in
      a tenancy in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: OCID of a compartment. Use OCID of a tenancy to get details of all the compartments in the
                     tenancy. Use OCID of a compartment in a tenancy to get details of the compartment.
        required: true
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
'''

EXAMPLES = '''
- name: Get details of all the compartments in a tenancy by specifying OCID of the tenancy
  oci_compartment_facts:
    compartment_id: 'ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaaaaaamx5hilztihors5wfsn2akuyty4'

- name: Get details of a compartment by specifying OCID of the compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get details of a compartment in a tenancy using the compartment's name
  oci_compartment_facts:
    compartment_id: 'ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaaaaaamx5hilztihors5wfsn2akuyty4'
    name: test_compartment
'''

RETURN = '''
compartments:
    description: List of compartment details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the tenancy containing the compartment
            returned: always
            type: string
            sample: ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaabcaamx5hilzhdwvds5wfsn2akuyty4
        id:
            description: The OCID of the compartment
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        description:
            description: The description assigned to the compartment
            returned: always
            type: string
            sample: Compartment for Project-A
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The compartment's current state
            returned: always
            type: string
            sample: ACTIVE
        name:
            description: The name assigned to the compartment
            returned: always
            type: string
            sample: "Project-A"
        time_created:
            description: Date and time the compartment was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: "2017-02-01T03:20:22.160000+00:00"
    sample: [{"compartment_id": "ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaabcaamx5hilzhdwvds5wfsn2akuyty4",
            "description": "Compartment for Project-Ansible",
            "id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "name": "Project-Ansible",
            "time_created": "2017-02-01T03:20:22.160000+00:00"
            }]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
    from oci.exceptions import ServiceError
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(dict(
        compartment_id=dict(type='str', required=True)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = module.params['compartment_id']
    tenancy = None

    try:
        tenancy = oci_utils.call_with_backoff(identity_client.get_tenancy,
                                              tenancy_id=compartment_id).data
    except ServiceError:
        pass

    # Check if the provided compartment_id is OCID of a tenancy(root compartment). If root compartment OCID is provided,
    # list all the compartments in the root compartment else retrieve information of the given compartment id.
    try:
        if tenancy is not None:
            result = to_dict(oci_utils.list_all_resources(identity_client.list_compartments,
                                                          compartment_id=compartment_id,
                                                          name=module.params['name']))
        else:
            result = [to_dict(oci_utils.call_with_backoff(identity_client.get_compartment,
                                                          compartment_id=compartment_id).data)]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(compartments=result)


if __name__ == '__main__':
    main()
