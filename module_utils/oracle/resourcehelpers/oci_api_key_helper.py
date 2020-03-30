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


class ApiKeyHelperCustom:
    def is_update(self):
        return False

    def get_resource(self):
        api_keys = self.list_resources()
        for api_key in api_keys:
            if api_key.key_id == self.module.params.get("api_key_id"):
                return oci_common_utils.get_default_response_from_resource(api_key)
        return None

    def create_resource(self):
        create_api_key_details = self.get_create_model()
        create_response = oci_common_utils.call_with_backoff(
            self.client.upload_api_key,
            user_id=self.module.params.get("user_id"),
            create_api_key_details=create_api_key_details,
        )
        api_key_id = create_response.data.key_id

        # wait until the api key is active.
        # The following logic manually checks if the API key in `list_api_keys` has reached the desired ACTIVE state
        response = self.client.list_api_keys(self.module.params.get("user_id"))

        def is_api_key_active(response):
            for api_key in response.data:
                if api_key.key_id == api_key_id and api_key.lifecycle_state == "ACTIVE":
                    return True
            return False

        # wait until the created API Key reaches Active state
        wait_response = oci.wait_until(
            self.client, response, evaluate_response=is_api_key_active
        )

        api_keys = wait_response.data
        created_api_key = None
        for api_key in api_keys:
            if api_key.key_id == api_key_id:
                created_api_key = api_key

        return created_api_key

    def delete_resource(self):
        api_key = self.get_resource().data
        operation_response = oci_common_utils.call_with_backoff(
            self.client.delete_api_key,
            user_id=self.module.params.get("user_id"),
            fingerprint=api_key.fingerprint,
        )
        return operation_response.data

    def delete(self):
        super_result = super(ApiKeyHelperCustom, self).delete()
        return oci_common_utils.get_result(
            changed=super_result.get("changed"),
            resource_type=self.resource_type,
            resource=oci_common_utils.get_resource_with_state(
                super_result.get(self.resource_type), "DELETED"
            ),
        )

    def get_matching_resource(self):
        create_model = self.get_create_model()
        for resource in self.list_resources():
            if not self._is_resource_active(resource):
                continue
            if resource.key_value == create_model.key:
                return resource
        return None
