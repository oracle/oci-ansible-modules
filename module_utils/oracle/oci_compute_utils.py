# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from ansible.module_utils.oracle import oci_utils

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_utils.get_logger("oci_compute_utils")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


def get_volume_attachments(compute_client, instance):
    param_map = {
        "instance_id": instance["id"],
        "compartment_id": instance["compartment_id"],
    }

    volume_attachments = to_dict(
        oci_utils.list_all_resources(
            compute_client.list_volume_attachments, **param_map
        )
    )
    return volume_attachments


def get_boot_volume_attachment(compute_client, instance):
    param_map = {
        "availability_domain": instance["availability_domain"],
        "instance_id": instance["id"],
        "compartment_id": instance["compartment_id"],
    }

    boot_volume_attachments = to_dict(
        oci_utils.list_all_resources(
            compute_client.list_boot_volume_attachments, **param_map
        )
    )

    if boot_volume_attachments:
        return boot_volume_attachments[0]
    return None
