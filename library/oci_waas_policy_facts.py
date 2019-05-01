#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_waas_policy_facts
short_description: Retrieve details about WAAS Policies.
description:
    - This module retrieves information of a specific WAAS policy or lists all WAAS policies in the given compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        type: str
    waas_policy_id:
        description: The OCID of the WAAS policy. Required to get information of a specific waas policy.
        type: str
    id:
        description: Filter policies using a list of policy OCIDs.
        type: list
    display_name:
        description: Filter policies using a list of display names.
        type: list
    lifecycle_state:
        description: Filter policies using a list of lifecycle states.
        type: list
    time_created_greater_than_or_equal_to:
        description: A filter that matches policies created on or after the specified date and time.
        type: str
    time_created_less_than:
        description: A filter that matches policies created before the specified date-time.
        type: str
    sort_by:
        description: The value by which policies are sorted in a paginated 'List' call. If unspecified,
                     defaults to timeCreated.
        type: str
        choices: ["id", "displayName", "timeCreated"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_sort_order_option ]
"""

EXAMPLES = """
- name: Get all the waas policies in a compartment
  oci_waas_policy_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific waas policy using its OCID
  oci_waas_policy_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx

- name: Get waas policy having the specified display name
  oci_waas_policy_facts:
    display_name: examplewaaspolicy

- name: Get waas policies in a compartment with given display names
  oci_waas_policy_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name:
        - examplewaaspolicy1
        - examplewaaspolicy2

- name: Filter waas policies in a compartment using display_name, lifecycle_state and sort the results
  oci_waas_policy_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name:
        - examplewaaspolicy1
        - examplewaaspolicy2
    lifecycle_state:
        - AVAILABLE
    sort_by: timeCreated
    sort_order: DESC
"""

RETURN = """
waas_policies:
    description: List of waas policies
    returned: on success
    type: complex
    contains:
        additional_domains:
            description: An array of additional domains for this web application.
            returned: success
            type: list
            sample: ["www.exampledomain1.com", "www.exampledomain2.com"]
        cname:
            description: The CNAME record to add to your DNS configuration to route traffic for the domain, and all
                         additional domains, through the WAF.
            returned: success
            type: str
            sample: www-exampledomain-com.b.waas.oci.oraclecloud.net
        compartment_id:
            description: The OCID of the WAAS policy's compartment.
            returned: success
            type: str
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: A key-value pair with a defined schema that restricts the values of tags. These predefined keys
                         are scoped to namespaces.
            returned: success
            type: complex
            sample: {"example_namespace": {"example_key": "example_value"}}
        display_name:
            description: The user-friendly name of the WAAS policy.
            returned: success
            type: str
            sample: examplewaaspolicy1
        domain:
            description: The web application domain that the WAAS policy protects.
            returned: success
            type: str
            sample: "www.exampledomain.com"
        freeform_tags:
            description: A simple key-value pair without any defined schema.
            returned: success
            type: complex
            sample: {"example_freeform_key": "example_freeform_value"}
        id:
            description: The OCID of the WAAS policy.
            returned: success
            type: str
            sample: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current lifecycle state of the WAAS policy.
            returned: success
            type: str
            sample: ACTIVE
        origins:
            description: A map of host to origin for the web application.
            returned: success
            type: complex
            sample: {"LBaaS": {"custom_headers": [], "http_port": 80, "https_port": 443, "uri": "1.2.3.4"}}
        policy_config:
            description: The policy_config of the WaasPolicy.
            returned: success
            type: complex
            sample: {"certificate_id": null, "is_https_enabled": false, "is_https_forced": false}
        time_created:
            description: The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: success
            type: str
            sample: 2019-03-22T13:02:55.563000+00:00
        waf_config:
            description: The WAF config of this policy.
            returned: success
            type: complex
            sample: {
                    "access_rules": [],
                    "address_rate_limiting": {
                        "allowed_rate_per_address": 1,
                        "block_response_code": 503,
                        "is_enabled": false,
                        "max_delayed_count_per_address": 10
                    },
                    "captchas": [],
                    "device_fingerprint_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "DFC",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "failure_threshold_expiration_in_seconds": 60,
                        "is_enabled": false,
                        "max_address_count": 20,
                        "max_address_count_expiration_in_seconds": 60
                    },
                    "good_bots": [
                        {
                            "description": "Googlebot is the search bot software used by Google",
                            "is_enabled": false,
                            "key": "4a4c6e7b-4d89-4141-8555-ec3b22b90a73",
                            "name": "Googlebot "
                        },
                    ],
                    "human_interaction_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "HIC",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "failure_threshold_expiration_in_seconds": 60,
                        "interaction_threshold": 3,
                        "is_enabled": false,
                        "recording_period_in_seconds": 15,
                        "set_http_header": null
                    },
                    "js_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "JSC-403",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "is_enabled": false,
                        "set_http_header": {
                            "name": "x-jsc-alerts",
                            "value": "{failed_amount}"
                        }
                    },
                    "origin": "LBaaS",
                    "protection_rules": [
                        {
                            "action": "OFF",
                            "description": "Cross-Site Scripting (XSS) Attempt: XSS Filters from IE",
                            "exclusions": [],
                            "key": "941340",
                            "labels": [
                                "OWASP",
                                "OWASP-2017",
                                "CRS3",
                                "WASCTC",
                                "PCI",
                                "HTTP",
                                "A2",
                                "A2-2017",
                                "XSS",
                                "Cross-Site Scripting"
                            ],
                            "mod_security_rule_ids": [
                                "941340"
                            ],
                            "name": "Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer"
                        },
                    ],
                    "whitelists": []}
    sample: [{
            "additional_domains": ["www.exampledomain1.com", "www.exampledomain2.com"],
            "cname": "www-exampledomain-com.b.waas.oci.oraclecloud.net",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {"example_namespace": {"example_key": "example_value"}},
            "display_name": "ansible_test_waas_policy",
            "domain": "www.example.com",
            "freeform_tags": {"example_freeform_key": "example_freeform_value"},
            "id": "ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx",
            "lifecycle_state": "ACTIVE",
            "origins": {"LBaaS": {"custom_headers": [], "http_port": 80, "https_port": 443, "uri": "1.2.3.4"}},
            "policy_config": {"certificate_id": null, "is_https_enabled": false, "is_https_forced": false},
            "time_created": "2019-03-22T13:02:55.563000+00:00",
            "waf_config": {
                    "access_rules": [],
                    "address_rate_limiting": {
                        "allowed_rate_per_address": 1,
                        "block_response_code": 503,
                        "is_enabled": false,
                        "max_delayed_count_per_address": 10
                    },
                    "captchas": [],
                    "device_fingerprint_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "DFC",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "failure_threshold_expiration_in_seconds": 60,
                        "is_enabled": false,
                        "max_address_count": 20,
                        "max_address_count_expiration_in_seconds": 60
                    },
                    "good_bots": [
                        {
                            "description": "Googlebot is the search bot software used by Google.",
                            "is_enabled": false,
                            "key": "4a4c6e7b-4d89-4141-8555-ec3b22b90a73",
                            "name": "Googlebot "
                        },
                    ],
                    "human_interaction_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "HIC",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "failure_threshold_expiration_in_seconds": 60,
                        "interaction_threshold": 3,
                        "is_enabled": false,
                        "recording_period_in_seconds": 15,
                        "set_http_header": null
                    },
                    "js_challenge": {
                        "action": "DETECT",
                        "action_expiration_in_seconds": 60,
                        "challenge_settings": {
                            "block_action": "SHOW_ERROR_PAGE",
                            "block_error_page_code": "JSC-403",
                            "block_error_page_description": "Access blocked by website owner. Please contact support.",
                            "block_error_page_message": "Access to the website is blocked.",
                            "block_response_code": 403,
                            "captcha_footer": "Enter the letters and numbers as they are shown in image above.",
                            "captcha_header": "We have detected an increased number of attempts to access this website.",
                            "captcha_submit_label": "Yes, I am human.",
                            "captcha_title": "Are you human?"
                        },
                        "failure_threshold": 10,
                        "is_enabled": false,
                        "set_http_header": {
                            "name": "x-jsc-alerts",
                            "value": "{failed_amount}"
                        }
                    },
                    "origin": "LBaaS",
                    "protection_rules": [
                        {
                            "action": "OFF",
                            "description": "Cross-Site Scripting (XSS) Attempt: XSS Filters from IE",
                            "exclusions": [],
                            "key": "941340",
                            "labels": [
                                "OWASP",
                                "OWASP-2017",
                                "CRS3",
                                "WASCTC",
                                "PCI",
                                "HTTP",
                                "A2",
                                "A2-2017",
                                "XSS",
                                "Cross-Site Scripting"
                            ],
                            "mod_security_rule_ids": [
                                "941340"
                            ],
                            "name": "Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer"
                        },
                    ],
                    "whitelists": []}
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def list_waas_policies(waas_client, module):
    compartment_id = module.params["compartment_id"]
    optional_list_method_params = [
        "sort_by",
        "sort_order",
        "id",
        "display_name",
        "lifecycle_state",
        "time_created_greater_than_or_equal_to",
        "time_created_less_than",
    ]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_waas_policy, waas_policy_id=waas_policy.id
            ).data
            for waas_policy in oci_utils.list_all_resources(
                waas_client.list_waas_policies,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        ]
    )


def get_waas_policy(waas_client, module):
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_waas_policy,
                waas_policy_id=module.params["waas_policy_id"],
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(
        filter_by_display_name=False,
        supports_sort=True,
        sort_by_choices=["id", "displayName", "timeCreated"],
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            waas_policy_id=dict(type="str"),
            display_name=dict(type="list"),
            id=dict(type="list"),
            lifecycle_state=dict(type="list"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("compartment_id", "waas_policy_id")],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    waas_client = oci_utils.create_service_client(module, WaasClient)
    try:
        if module.params["waas_policy_id"]:
            result = get_waas_policy(waas_client, module)
        elif module.params["compartment_id"]:
            result = list_waas_policies(waas_client, module)
        else:
            module.fail_json(
                msg="Specify a compartment_id to get all the waas policies in the compartment or a "
                "waas_policy_id to retrieve a specific waas policy"
            )
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(waas_policies=result)


if __name__ == "__main__":
    main()
