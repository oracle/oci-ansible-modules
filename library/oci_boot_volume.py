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
module: oci_boot_volume
short_description: Manage boot volumes in OCI Block Volume service
description:
    - This module allows the user to perform delete & update operations on boot volumes in OCI Block Volume service.
version_added: "2.x"
options:
    lookup_attached_instance:
        description: Whether to fetch information of the compute instance attached to this boot volume from all the
                     compartments in the tenancy.Fetching this information requires traversing through all the
                     compartments in the  Tenancy and therefore can potentially take a long time. This option is only
                     supported in experimental mode.

                     When I(lookup_all_attached_instances=False), only an attached compute instance belonging to this
                     boot volume's compartment, is returned. This is useful when the boot volume is used within
                     a single compartment. When I(lookup_all_attached_instances=True), all the compartments in the
                     tenancy are searched to find out the compute instance that is attached to this boot volume.
                     Fetching information about compute instances attached to this boot volume is an experimental
                     feature (ie, this may or may not be supported in future releases). To use such experimental
                     features, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        required: false
        default: no
        type: bool
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    state:
        description: Update a boot volume with I(state=present). Delete a boot volume with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
    boot_volume_id:
        description: The OCID of the boot volume.
        required: true
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
'''

EXAMPLES = '''
- name: Update name of a boot volume
  oci_boot_volume:
    name: ansible_boot_volume
    boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx

- name: Delete a boot volume
  oci_boot_volume:
    boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
    state: 'absent'
'''

RETURN = '''
boot_volume:
    description: Information about the boot volume
    returned: On successful update and delete operation
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the boot volume.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-2
        compartment_id:
            description: The OCID of the compartment that contains the boot volume.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the boot volume.
            returned: always
            type: string
            sample: ansible_boot_volume
        id:
            description: The OCID of the boot volume.
            returned: always
            type: string
            sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        image_id:
            description: The image OCID used to create the boot volume.
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of a boot volume.
            returned: always
            type: string
            sample: PROVISIONING
        size_in_gbs:
            description: The size of the boot volume in GBs.
            returned: always
            type: int
            sample: 50
        size_in_mbs:
            description: The size of the boot volume in MBs.
            returned: always
            type: int
            sample: 51200
        time_created:
            description: The date and time the boot volume was created. Format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2017-11-22T19:40:08.871000+00:00
        attached_instance_information:
            description: Information of the instance the boot volume is attached to.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: when this boot volume is attached to a compute instance
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
    sample: {
                "attached_instance_information": {
                    "availability_domain": "IwGV:US-ASHBURN-AD-1",
                    "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "display_name": "Remote boot attachment for instance",
                    "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                    "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state": "ATTACHED",
                    "time_created": "2018-01-14T19:02:49.085000+00:00"
                },
                "availability_domain": "IwGV:US-ASHBURN-AD-1",
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "display_name": "demo-20171214-100_bastion_instance (Boot Volume)",
                "id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
                "lifecycle_state": "AVAILABLE",
                "size_in_gbs": 46,
                "size_in_mbs": 47694,
                "time_created": "2018-01-14T19:02:49.042000+00:00"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle.oci_utils import check_mode

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.models.update_boot_volume_details import UpdateBootVolumeDetails
    from oci.exceptions import ServiceError
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def handle_delete_boot_volume(block_storage_client, module):
    return oci_utils.delete_and_wait(resource_type="boot_volume",
                                     client=block_storage_client,
                                     get_fn=block_storage_client.get_boot_volume,
                                     kwargs_get={"boot_volume_id": module.params["boot_volume_id"]},
                                     delete_fn=block_storage_client.delete_boot_volume,
                                     kwargs_delete={"boot_volume_id": module.params["boot_volume_id"]},
                                     module=module
                                     )


def handle_update_boot_volume(block_storage_client, module):
    return oci_utils.check_and_update_resource(resource_type="boot_volume",
                                               get_fn=block_storage_client.get_boot_volume,
                                               kwargs_get={"boot_volume_id": module.params["boot_volume_id"]},
                                               update_fn=block_storage_client.update_boot_volume,
                                               primitive_params_update=['boot_volume_id'],
                                               kwargs_non_primitive_update={
                                                   UpdateBootVolumeDetails: "update_boot_volume_details"},
                                               module=module,
                                               update_attributes=UpdateBootVolumeDetails().attribute_map.keys()
                                               )


@check_mode
def add_attached_instance_info(config, module, result, lookup_attached_instance):
    compute_client = ComputeClient(config)
    try:
        result['boot_volume']['attached_instance_information'] = oci_utils.get_attached_instance_info(
            config,
            lookup_attached_instance,
            list_attachments_fn=compute_client.list_boot_volume_attachments,
            list_attachments_args={"boot_volume_id": result["boot_volume"]["id"],
                                   "availability_domain": result["boot_volume"]["availability_domain"],
                                   "compartment_id": result["boot_volume"]["compartment_id"]}
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(dict(
        boot_volume_id=dict(type='str', required=True, aliases=['id']),
        display_name=dict(type='str', required=False, aliases=['name']),
        state=dict(type='str', required=False, default='present', choices=['absent', 'present']),
        lookup_attached_instance=dict(type='bool', required=False, default='no')
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ['state', 'present', ['display_name']]
        ]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    config = oci_utils.get_oci_config(module)
    block_storage_client = BlockstorageClient(config)

    state = module.params['state']

    if state == 'absent':
        result = handle_delete_boot_volume(block_storage_client, module)

    else:
        result = handle_update_boot_volume(block_storage_client, module)

    add_attached_instance_info(config, module, result, module.params['lookup_attached_instance'])

    module.exit_json(**result)


if __name__ == '__main__':
    main()
