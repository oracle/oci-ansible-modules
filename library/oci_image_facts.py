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
module: oci_image_facts
short_description: Retrieve details about one or more Compute images in OCI Compute Service
description:
    - This module retrieves details about a specific image, or all images in a specified Compartment in OCI Compute
      Service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment (either the tenancy or another compartment in the tenancy). Required
                     for retrieving information about all images in a Compartment/Tenancy.
        required: false
    image_id:
        description: The OCID of the image. Required for retrieving information about a specific image
        required: false
        aliases: ['id']
    operating_system:
        description: The image's operating system.
        required: false
    operating_system_version:
        description: The image's operating system version.
        required: false
    shape:
        description: Shape name.
        required: false
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING",
                     "DISABLED", "DELETED"
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
'''

EXAMPLES = '''
- name: Get details of all the images of a specified compartment
  oci_image_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'

- name: Get details of a specific image
  oci_image_facts:
    id:"ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
'''

RETURN = '''
images:
    description: Information about one or more images
    returned: on success
    type: complex
    contains:
        base_image_id:
            description: The OCID of the image originally used to create the image.
            returned: always
            type: string
            sample: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....yw2wxfa
        compartment_id:
            description: The OCID of the compartment containing the instance that was used as the basis for the image.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        create_image_allowed:
            description: Whether instances launched with this image can be used to create new images. For example,
                         an image of an Oracle Database instance cannot be created
            returned: always
            type: boolean
            sample: True
        display_name:
            description: A user-friendly name for the image. It does not have to be unique, and it's changeable.
            returned: always
            type: string
            sample: my_custom_image_1
        id:
            description: The OCID of the image.
            returned: always
            type: string
            sample: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...e4mehv6bv3qca
        lifecycle_state:
            description: The current state of the image.
            returned: always
            type: string
            sample: DELETED
        operating_system:
            description: The image's operating system.
            returned: always
            type: string
            sample: Oracle Linux
        operating_system_version:
            description: The image's operating system version.
            returned: always
            type: string
            sample: 7.2
        time_created:
            description: The date and time the image was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00

    sample: {
      "base-image-id": null,
      "compartment-id": null,
      "create-image-allowed": true,
      "display-name": "Oracle-Linux-7.4-2017.11.15-0",
      "id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...cmnzlbv2v4q",
      "lifecycle-state": "AVAILABLE",
      "operating-system": "Oracle Linux",
      "operating-system-version": "7.4",
      "time-created": "2017-11-16T01:16:41.409000+00:00"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(dict(
        compartment_id=dict(type='str', required=False),
        image_id=dict(type='str', required=False, aliases=['id']),
        operating_system=dict(type='str', required=False),
        operating_system_version=dict(type='str', required=False),
        lifecycle_state=dict(type='str', required=False),
        shape=dict(type='str', required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=['id', 'compartment_id']
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    compartment_id = module.params['compartment_id']
    id = module.params['image_id']

    result = dict(changed=False)
    try:
        if compartment_id:
            optional_list_method_params = ['operating_system', 'operating_system_version', 'lifecycle_state', 'shape']
            optional_kwargs = {param: module.params[param] for param in optional_list_method_params
                               if module.params.get(param) is not None}
            inst = oci_utils.list_all_resources(compute_client.list_images, compartment_id=compartment_id,
                                                **optional_kwargs)
            result = to_dict(inst)
        else:
            inst = oci_utils.call_with_backoff(compute_client.get_image, image_id=id).data
            result = to_dict([inst])
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))

    module.exit_json(images=result)


if __name__ == '__main__':
    main()
