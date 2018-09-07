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
module: oci_api_key
short_description: Upload and delete API signing key of a user in OCI
description:
    - This module allows the user upload and delete API signing keys of a user in OCI. A PEM-format RSA credential for
      securing requests to the Oracle Cloud Infrastructure REST API. Also known as an API signing key. Specifically,
      this is the public key from the key pair. The private key remains with the user calling the API. For information
      about generating a key pair in the required PEM format, see Required Keys and OCIDs.
      Note that this is not the SSH key for accessing compute instances.
      Each user can have a maximum of three API signing keys.
      For more information about user credentials, see
      U(https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm).
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user whose API signing key needs to be created or deleted.
        required: true
    api_signing_key:
        description: The public key. Must be an RSA key in PEM format. Required when the API signing key is
                     uploaded with I(state=present)
        required: false
        aliases: ['key']
    api_key_id:
        description: The API signing key's id. The Id must be of the format TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.
        required: false
        aliases: ['id']
    state:
        description: The state of the api signing key that must be asserted to. When I(state=present), and the
                     api key doesn't exist, the api key is created with the provided C(api_signing_key).
                     When I(state=absent), the api signing key corresponding to the provided C(fingerprint) is deleted.
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
'''

EXAMPLES = '''
- name: Upload a new api signing key for the specified user
  oci_api_key:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    key: "-----BEGIN PUBLIC KEY-----cmdnMIIBIjANBgkqhkiG9w0BAQEFA......mwIDAQAB-----END PUBLIC KEY-----"

- name: Delete an API signing key for the specified user
  oci_api_key:
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
        "id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da"
        state: "absent"
'''

RETURN = '''
oci_api_key:
    description: Details of the API signing key
    returned: On success
    type: dict
    sample: {
        "fingerprint": "08:07:a6:7d:06:b4:73:91:e9:2c:da:42:c8:cb:df:02",
        "inactive_status": null,
        "key_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da",
        "key_value": "-----BEGIN PUBLIC KEY-----...urt/fN8jNz2nZwIDAQAB-----END PUBLIC KEY-----",
        "lifecycle_state": "ACTIVE",
        "time_created": "2018-01-08T09:33:59.705000+00:00",
        "user_id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
     }
'''

import oci
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateApiKeyDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None
RESOURCE_NAME = "api_key"


def set_logger(provided_logger):
    global logger
    logger = provided_logger


def get_logger():
    return logger


def _get_api_key_from_id(identity_client, user_id, api_key_id, module):
    try:
        resp = oci_utils.call_with_backoff(identity_client.list_api_keys, user_id=user_id)
        if resp is not None:
            for api_key in resp.data:
                if api_key.key_id == api_key_id:
                    return api_key
        return None
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def delete_api_key(identity_client, user_id, id, module):
    result = {}
    changed = False
    try:
        api_key = _get_api_key_from_id(identity_client, user_id, id, module)
        oci_utils.call_with_backoff(identity_client.delete_api_key, user_id=user_id, fingerprint=api_key.fingerprint)
        get_logger().info("Deleted api password %s", id)
        changed = True

        # The API key is not returned by list api passwords after it
        # is deleted, and so we currently reuse the earlier api password object and mark
        # its lifecycle state as DELETED.
        # Note: This current approach has problems around idempotency.
        # We also don't wait, as there is no state transition that we need to wait for.
        api_key.lifecycle_state = "DELETED"
        result[RESOURCE_NAME] = to_dict(api_key)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result['changed'] = changed
    return result


def _is_api_key_active(api_keys, api_key_id):
    result = [api_key for api_key in api_keys if api_key.key_id == api_key_id and api_key.lifecycle_state == "ACTIVE"]
    return len(result) == 1


def create_api_key(identity_client, user_id, key, module):
    try:
        cakd = CreateApiKeyDetails()
        cakd.key = key
        result = oci_utils.create_resource(resource_type=RESOURCE_NAME, create_fn=identity_client.upload_api_key,
                                           kwargs_create={
                                               "user_id": user_id,
                                               "create_api_key_details": cakd
                                           },
                                           module=module)
        resource = result[RESOURCE_NAME]
        api_key_id = resource["key_id"]
        get_logger().info("Created API signing key %s", to_dict(resource))

        # API keys don't have a get<resource> and so we can't use oci_utils.create_and_wait
        # The following logic manually checks if the API key in `list_api_keys` has reached the desired ACTIVE state
        response = identity_client.list_api_keys(user_id)
        # wait until the created API Key reaches Active state
        oci.wait_until(identity_client, response,
                       evaluate_response=lambda resp: _is_api_key_active(resp.data, api_key_id))

        result[RESOURCE_NAME] = to_dict(_get_api_key_from_id(identity_client, user_id, api_key_id, module))
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def main():
    set_logger(oci_utils.get_logger("oci_api_key"))

    module_args = oci_utils.get_common_arg_spec(supports_create=True, supports_wait=True)
    module_args.update(dict(
        user_id=dict(type='str', required=True),
        api_key_id=dict(type='str', required=False, aliases=['id']),
        api_signing_key=dict(type='str', required=False, aliases=['key']),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[('state', 'absent', ['api_key_id'])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params['state']

    result = dict(changed=False)

    user_id = module.params.get("user_id", None)
    public_key = module.params.get("api_signing_key", None)
    api_key_id = module.params.get("api_key_id", None)

    if api_key_id is not None:
        api_key = _get_api_key_from_id(identity_client, user_id, api_key_id, module)

        if state == 'absent':
            get_logger().debug("Delete api password %s for user %s requested", api_key_id, user_id)
            if api_key is not None:
                get_logger().debug("Deleting %s", api_key.key_id)
                result = delete_api_key(identity_client, user_id, api_key_id, module)
            else:
                get_logger().debug("API Signing Key %s already deleted.", api_key_id)
        elif state == 'present':
            module.fail_json(msg="API signing key cannot be updated.")
    else:
        result = oci_utils.check_and_create_resource(resource_type=RESOURCE_NAME, create_fn=create_api_key,
                                                     kwargs_create={"identity_client": identity_client,
                                                                    "user_id": user_id, "key": public_key,
                                                                    "module": module},
                                                     list_fn=identity_client.list_api_keys,
                                                     kwargs_list={"user_id": user_id},
                                                     module=module,
                                                     model=CreateApiKeyDetails()
                                                     )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
