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
module: oci_compartment
short_description: Manage compartments in OCI
description:
    - This module allows the user to create and update a compartment in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the tenancy in which the compartment has to be created or the OCID of the compartment
                     to be updated.
        required: true
    description:
        description: The description to be assigned to the compartment. Required when creating a compartment with
                     I(state=present). I(description) should be minimum 1 character and maximum 100 characters long.
                     Does not have to be unique, and it's changeable.
        required: false
    name:
        description: Name of the compartment. The name must be unique across all compartments in the tenancy. Required
                     when creating a compartment with I(state=present).
        required: false
    state:
        description: Create or update a compartment with I(state=present).
        required: false
        default: present
        choices: ['present']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_tags, oracle_wait_options ]
'''

EXAMPLES = '''
- name: Create a compartment
  oci_compartment:
    compartment_id: 'ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaabcaamx5hilzhdwvds5wfsn2akuyty4'
    name: Project-A
    description: Compartment for Project-A

- name: Update name and description of a compartment
  oci_compartment:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    name: Project-Ansible
    description: Compartment for Project-Ansible
'''

RETURN = '''
compartment:
    description: Information about the compartment
    returned: On successful operation
    type: dict
    sample: {"compartment_id": "ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx:aaaabcaamx5hilzhdwvds5wfsn2akuyty4",
            "description": "Compartment for Project-Ansible",
            "id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "name": "Project-Ansible",
            "time_created": "2017-02-01T03:20:22.160000+00:00"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError
    from oci.identity.models import CreateCompartmentDetails
    from oci.identity.models import UpdateCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_compartment(identity_client, module):
    create_compartment_details = CreateCompartmentDetails()
    for attribute in create_compartment_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_compartment_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(resource_type="compartment",
                                       create_fn=identity_client.create_compartment,
                                       kwargs_create={"create_compartment_details": create_compartment_details},
                                       client=identity_client,
                                       get_fn=identity_client.get_compartment,
                                       get_param="compartment_id",
                                       module=module
                                       )
    return result


def update_compartment(identity_client, module):
    result = oci_utils.check_and_update_resource(resource_type="compartment",
                                                 get_fn=identity_client.get_compartment,
                                                 kwargs_get={"compartment_id": module.params["compartment_id"]},
                                                 update_fn=identity_client.update_compartment,
                                                 primitive_params_update=['compartment_id'],
                                                 kwargs_non_primitive_update={
                                                     UpdateCompartmentDetails: "update_compartment_details"},
                                                 module=module,
                                                 update_attributes=UpdateCompartmentDetails().attribute_map.keys()
                                                 )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(dict(
        compartment_id=dict(type='str', required=True),
        name=dict(type='str', required=False),
        description=dict(type='str', required=False),
        state=dict(type='str', required=False, default='present', choices=['present'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = module.params['compartment_id']

    # Check if the provided compartment_id is OCID of a tenancy(root compartment). If tenancy OCID is provided, it's
    # supposed to be a call to create compartment in the tenancy else it's a call to update compartment.
    tenancy = None
    try:
        tenancy = oci_utils.call_with_backoff(identity_client.get_tenancy,
                                              tenancy_id=compartment_id).data
    except ServiceError as se:
        if se.status == 404 and se.code == "TenantNotFound":
            # the user has provided a compartment ocid, try to find a compartment with the provided value
            try:
                oci_utils.call_with_backoff(identity_client.get_compartment, compartment_id=compartment_id).data
            except ServiceError as serr:
                if serr.status == 404 and serr.code == "CompartmentNotFound":
                    # If there exists no compartment, then it is likely a user error (an invalid compartment or tenancy
                    # id)
                    module.fail_json(msg="The provided compartment_id is an invalid tenancy or compartment ocid. Please"
                                         "check the provided compartment_id")
                else:
                    # some other ServiceError trying to get compartment information
                    module.fail_json(msg=se.message)
        else:
            # Some other ServiceError trying to get tenancy information
            module.fail_json(msg=se.message)

    if tenancy is not None:
        result = oci_utils.check_and_create_resource(resource_type='compartment',
                                                     create_fn=create_compartment,
                                                     kwargs_create={
                                                         'identity_client': identity_client,
                                                         'module': module},
                                                     list_fn=identity_client.list_compartments,
                                                     kwargs_list={"compartment_id": module.params['compartment_id']
                                                                  },
                                                     module=module,
                                                     model=CreateCompartmentDetails()
                                                     )
    else:
        result = update_compartment(identity_client, module)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
