#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_volume_backup_policy_facts
short_description: Fetches details about one or multiple VolumeBackupPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeBackupPolicy resources in Oracle Cloud Infrastructure
    - Lists all volume backup policies available to the caller.
    - If I(policy_id) is specified, the details of a single VolumeBackupPolicy will be returned.
version_added: "2.5"
options:
    policy_id:
        description:
            - The OCID of the volume backup policy.
            - Required to get a specific volume_backup_policy.
        aliases: ["id"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: List volume_backup_policies
  oci_volume_backup_policy_facts:

- name: Get a specific volume_backup_policy
  oci_volume_backup_policy_facts:
    policy_id: ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
volume_backup_policies:
    description:
        - List of VolumeBackupPolicy resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        id:
            description:
                - The OCID of the volume backup policy.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        schedules:
            description:
                - The collection of schedules that this policy will apply.
            returned: on success
            type: complex
            contains:
                backup_type:
                    description:
                        - The type of backup to create.
                    returned: on success
                    type: string
                    sample: FULL
                offset_seconds:
                    description:
                        - The number of seconds that the backup time should be shifted from the default interval boundaries specified by the period. Backup time
                          = Frequency start time + Offset.
                    returned: on success
                    type: int
                    sample: 56
                period:
                    description:
                        - How often the backup should occur.
                    returned: on success
                    type: string
                    sample: ONE_HOUR
                retention_seconds:
                    description:
                        - How long, in seconds, backups created by this schedule should be kept until being automatically deleted.
                    returned: on success
                    type: int
                    sample: 56
        time_created:
            description:
                - The date and time the volume backup policy was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "schedules": [{
            "backup_type": "FULL",
            "offset_seconds": 56,
            "period": "ONE_HOUR",
            "retention_seconds": 56
        }],
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return ["policy_id"]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup_policy,
            policy_id=self.module.params.get("policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = ["display_name"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_volume_backup_policies, **optional_kwargs
        )


VolumeBackupPolicyFactsHelperCustom = get_custom_class(
    "VolumeBackupPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    VolumeBackupPolicyFactsHelperCustom, VolumeBackupPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(policy_id=dict(aliases=["id"], type="str"), display_name=dict(type="str"))
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="volume_backup_policy",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(volume_backup_policies=result)


if __name__ == "__main__":
    main()
