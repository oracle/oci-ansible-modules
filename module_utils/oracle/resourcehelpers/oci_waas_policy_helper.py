# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_common_utils


try:
    import oci

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyHelperCustom:
    def list_resources(self):
        return [
            oci_common_utils.call_with_backoff(
                self.client.get_waas_policy, waas_policy_id=waas_policy_summary.id
            ).data
            for waas_policy_summary in super(
                WaasPolicyHelperCustom, self
            ).list_resources()
        ]
