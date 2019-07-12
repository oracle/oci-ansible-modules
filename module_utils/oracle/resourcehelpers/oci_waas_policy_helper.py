# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_common_utils, oci_waas_utils


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

    def get_create_model(self):
        return oci_waas_utils.get_waas_policy_create_model(self.module)

    def get_update_model(self):
        update_waas_policy_details_class = self.get_update_model_class()
        update_waas_policy_details = update_waas_policy_details_class()
        update_waas_policy_details.origins = oci_waas_utils.get_waas_origins(
            self.module
        )
        update_waas_policy_details.policy_config = oci_waas_utils.get_waas_policy_config(
            self.module
        )
        update_waas_policy_details.waf_config = oci_waas_utils.get_waf_config_for_update(
            self.module
        )
        for attr in update_waas_policy_details.attribute_map:
            if attr in ["origins", "policy_config", "waf_config"]:
                continue
            if self.module.params.get(attr) is None:
                continue
            setattr(update_waas_policy_details, attr, self.module.params[attr])
        return update_waas_policy_details

    def create_wait(self, create_response):
        work_request_response = self.wait_for_work_request(
            create_response, oci_common_utils.WORK_REQUEST_COMPLETED_STATES
        )
        for work_request_resource in work_request_response.data.resources:
            if (
                work_request_resource.entity_type == "waas"
                and work_request_resource.action_type == "CREATED"
            ):
                waas_policy_id = work_request_resource.identifier
                break
        if not waas_policy_id:
            self.module.fail_json(
                msg="Cound not get the waas policy id from the work request."
            )
        waas_policy = oci_common_utils.call_with_backoff(
            self.client.get_waas_policy, waas_policy_id=waas_policy_id
        ).data
        if not waas_policy:
            self.module.fail_json(
                "Could not get the waas policy resource after creation."
            )
        if waas_policy.lifecycle_state in oci_common_utils.DEAD_STATES:
            self.module.fail_json(
                msg="WAAS policy created but in {0} state.".format(
                    waas_policy.lifecycle_state
                )
            )
        return waas_policy
