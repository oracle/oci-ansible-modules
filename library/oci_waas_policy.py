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
module: oci_waas_policy
short_description: Manage WAAS policies in OCI
description:
    - This module allows the user to create, delete and update WAAS policies in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        type: str
    display_name:
        description: A user-friendly name for the WAAS policy. The name is can be changed and does not need to
                     be unique.
        type: str
        aliases: [ 'name' ]
    domain:
        description: The web application domain that the WAAS policy protects.
        type: str
    additional_domains:
        description: An array of additional domains for the specified web application.
        type: list
    origins:
        description: A map of host to origin for the web application. The key should be a customer friendly name for
                     the host, ex. primary, secondary, etc.
        type: dict
        suboptions:
            custom_headers:
                description: A list of HTTP headers to forward to your origin.
                suboptions:
                    name:
                        description: The name of the header.
                    value:
                        description: The value of the header.
            http_port:
                description: The HTTP port on the origin that the web application listens on. If unspecified, defaults
                             to 80.
            https_port:
                description: The HTTPS port on the origin that the web application listens on. If unspecified, defaults
                             to 443.
            uri:
                description: The URI of the origin. Does not support paths. Port numbers should be specified in the
                             http_port and https_port fields.
    policy_config:
        description: Config for the WAAS policy.
        type: dict
        suboptions:
            certificate_id:
                description: The OCID of the SSL certificate to use if HTTPS is supported.
            is_https_enabled:
                description: Enable or disable HTTPS support. If true, a certificateId is required.
                default: False
            is_https_forced:
                description: Force HTTP to HTTPS redirection.
                default: False
    waf_config:
        description: The WAF config for the WAAS policy.
        type: dict
        suboptions:
            access_rules:
                description: The access rules applied to the Web Application Firewall. Used for defining custom access
                             policies with the combination of ALLOW, DETECT, and BLOCK rules, based on different
                             criteria.
                suboptions:
                    action:
                        description: The action to take when the access criteria are met for a rule.
                        default: ALLOW
                    block_action:
                        description: The method used to block requests if I(action=BLOCK) and the access criteria
                                     are met.
                        choices:
                            - SET_RESPONSE_CODE
                            - SHOW_ERROR_PAGE
                        default: SET_RESPONSE_CODE
                    block_error_page_code:
                        description: The error code to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the access criteria are met.
                        default: Access rules
                    block_error_page_description:
                        description: The description text to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the access criteria are met.
                        default: Access blocked by website owner. Please contact support.
                    block_error_page_message:
                        description: The message to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the access criteria are met.
                        default: Access to the website is blocked.
                    block_response_code:
                        description: The response status code to return when I(action=BLOCK),
                                     I(block_action=SET_RESPONSE_CODE), and the access criteria are met.
                        default: 403
                    criteria:
                        description: The list of access rule criteria.
                        suboptions:
                            condition:
                                description: The criteria the access rule uses to determine if action should be taken
                                             on a request.
                                required: true
                            value:
                                description: The criteria value.
                                required: true
                                choices: ["URL_IS", "URL_IS_NOT", "URL_STARTS_WITH", "URL_PART_ENDS_WITH",
                                          "URL_PART_CONTAINS", "URL_REGEX", "IP_IS", "IP_IS_NOT", "HTTP_HEADER_CONTAINS",
                                          "COUNTRY_IS", "COUNTRY_IS_NOT", "USER_AGENT_IS", "USER_AGENT_IS_NOT"]
                    name:
                        description: The unique name of the access rule.
            address_rate_limiting:
                description: The IP address rate limiting settings used to limit the number of requests from an address.
                suboptions:
                    allowed_rate_per_address:
                        description: The number of allowed requests per second from one IP address.
                        default: 1
                    block_response_code:
                        description: The response status code returned when a request is blocked.
                        default: 503
                    is_enabled:
                        description: Enables or disables the address rate limiting Web Application Firewall feature.
                    max_delayed_count_per_address:
                        description: The maximum number of requests allowed to be queued before subsequent requests
                                     are dropped.
                        default: 10
            captchas:
                description: A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA
                             to block bots.
                suboptions:
                    failure_message:
                        description: The text to show when incorrect CAPTCHA text is entered.
                        required: true
                    footer_text:
                        description: The text to show in the footer when showing a CAPTCHA challenge.
                        default: Enter the letters and numbers as they are shown in the image above.
                    header_text:
                        description: The text to show in the header when showing a CAPTCHA challenge.
                        default: We have detected an increased number of attempts to access this website.
                                 To help us keep this site secure, please let us know that you are not a robot by
                                 entering the text from the image below.
                    session_expiration_in_seconds:
                        description: The amount of time before the CAPTCHA expires, in seconds.
                        required: true
                    submit_label:
                        description: The text to show on the label of the CAPTCHA challenge submit button.
                        required: true
                    title:
                        description: The title used when displaying a CAPTCHA challenge.
                        required: true
                    url:
                        description: The unique URL path at which to show the CAPTCHA challenge.
                        required: true
            device_fingerprint_challenge:
                description: The device fingerprint challenge settings. Used to detect unique devices based on the
                             device fingerprint information collected in order to block bots.
                suboptions:
                    action:
                        description: The action to take on requests from detected bots.
                        choices:
                            - DETECT
                            - BLOCK
                        default: DETECT
                    action_expiration_in_seconds:
                        description: The number of seconds between challenges for the same IP address.
                        default: 60
                    challenge_settings:
                        description: The challenge settings.
                        suboptions:
                            block_action:
                                description: The method used to block requests that fail the challenge if
                                             I(action=BLOCK).
                                choices:
                                    - SET_RESPONSE_CODE
                                    - SHOW_ERROR_PAGE
                                    - SHOW_CAPTCHA
                                default: SHOW_ERROR_PAGE
                            block_error_page_code:
                                description: The error code to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: 403
                            block_error_page_description:
                                description: The description text to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access blocked by website owner. Please contact support.
                            block_error_page_message:
                                description: The message to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access to the website is blocked.
                            block_response_code:
                                description: The response status code to return when I(action=BLOCK),
                                             I(block_action=SET_RESPONSE_CODE), and the request is blocked.
                                default: 403
                            captcha_footer:
                                description: The text to show in the footer when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Enter the letters and numbers as they are shown in image above.
                            captcha_header:
                                description: The text to show in the header when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: We have detected an increased number of attempts to access this webapp.
                                         To help us keep this webapp secure, please let us know that you are not a robot
                                         by entering the text from captcha below.
                            captcha_submit_label:
                                description: The text to show on the label of the CAPTCHA challenge submit button when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Yes, I am human.
                            captcha_title:
                                description: The title used when showing a CAPTCHA challenge when I(action=BLOCK),
                                             I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Are you human?
                    failure_threshold:
                        description: The number of failed requests allowed before taking action.
                        default: 10
                    failure_threshold_expiration_in_seconds:
                        description: The number of seconds before the failure threshold resets.
                        default: 60
                    is_enabled:
                        description: Enables or disables the device fingerprint challenge Web Application Firewall
                                     feature.
                    max_address_count:
                        description: The maximum number of IP addresses permitted with the same device fingerprint.
                        default: 20
                    max_address_count_expiration_in_seconds:
                        description: The number of seconds before the maximum addresses count resets.
                        default: 60
            good_bots:
                description: A list of bots allowed to access the web application.
                suboptions:
                    description:
                        description: The description of the bot.
                    is_enabled:
                        description: Enables or disables the bot.
                    key:
                        description: The unique key for the bot.
                    name:
                        description: The bot name.
            human_interaction_challenge:
                description: The human interaction challenge settings. Used to look for natural human interactions such
                             as mouse movements, time on site, and page scrolling to identify bots.
                suboptions:
                    action:
                        description: The action to take on requests from detected bots.
                        choices:
                            - DETECT
                            - BLOCK
                        default: DETECT
                    action_expiration_in_seconds:
                        description: The number of seconds between challenges for the same IP address.
                        default: 60
                    challenge_settings:
                        description: The challenge settings.
                        suboptions:
                            block_action:
                                description: The method used to block requests that fail the challenge if
                                             I(action=BLOCK).
                                choices:
                                    - SET_RESPONSE_CODE
                                    - SHOW_ERROR_PAGE
                                    - SHOW_CAPTCHA
                                default: SHOW_ERROR_PAGE
                            block_error_page_code:
                                description: The error code to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: 403
                            block_error_page_description:
                                description: The description text to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access blocked by website owner. Please contact support.
                            block_error_page_message:
                                description: The message to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access to the website is blocked.
                            block_response_code:
                                description: The response status code to return when I(action=BLOCK),
                                             I(block_action=SET_RESPONSE_CODE), and the request is blocked.
                                default: 403
                            captcha_footer:
                                description: The text to show in the footer when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Enter the letters and numbers as they are shown in image above.
                            captcha_header:
                                description: The text to show in the header when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: We have detected an increased number of attempts to access this webapp.
                                         To help us keep this webapp secure, please let us know that you are not a robot
                                         by entering the text from captcha below.
                            captcha_submit_label:
                                description: The text to show on the label of the CAPTCHA challenge submit button when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Yes, I am human.
                            captcha_title:
                                description: The title used when showing a CAPTCHA challenge when I(action=BLOCK),
                                             I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Are you human?
                    failure_threshold:
                        description: The number of failed requests allowed before taking action.
                        default: 10
                    failure_threshold_expiration_in_seconds:
                        description: The number of seconds before the failure threshold resets.
                        default: 60
                    interaction_threshold:
                        description: The number of interactions required to pass the challenge.
                        default: 3
                    is_enabled:
                        description: Enables or disables the human interaction challenge Web Application Firewall
                                     feature.
                    recording_period_in_seconds:
                        description: The number of seconds to record the interactions from the user.
                        default: 15
                    set_http_header:
                        description: Adds an additional HTTP header to requests that fail the challenge before being
                                     passed to the origin. Only applicable when I(action=DETECT).
                        suboptions:
                            name:
                                description: The name of the header.
                            value:
                                description: The value of the header.
            js_challenge:
                description: The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge
                             and take the action if a browser has no JavaScript support in order to block bots.
                suboptions:
                    action:
                        description: The action to take against requests from detected bots.
                        choices:
                            - DETECT
                            - BLOCK
                        default: DETECT
                    action_expiration_in_seconds:
                        description: The number of seconds between challenges from the same IP address.
                        default: 60
                    challenge_settings:
                        description: The challenge settings.
                        suboptions:
                            block_action:
                                description: The method used to block requests that fail the challenge if
                                             I(action=BLOCK).
                                choices:
                                    - SET_RESPONSE_CODE
                                    - SHOW_ERROR_PAGE
                                    - SHOW_CAPTCHA
                                default: SHOW_ERROR_PAGE
                            block_error_page_code:
                                description: The error code to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: 403
                            block_error_page_description:
                                description: The description text to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access blocked by website owner. Please contact support.
                            block_error_page_message:
                                description: The message to show on the error page when I(action=BLOCK),
                                             I(block_action=SHOW_ERROR_PAGE), and the request is blocked.
                                default: Access to the website is blocked.
                            block_response_code:
                                description: The response status code to return when I(action=BLOCK),
                                             I(block_action=SET_RESPONSE_CODE), and the request is blocked.
                                default: 403
                            captcha_footer:
                                description: The text to show in the footer when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Enter the letters and numbers as they are shown in image above.
                            captcha_header:
                                description: The text to show in the header when showing a CAPTCHA challenge when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: We have detected an increased number of attempts to access this webapp.
                                         To help us keep this webapp secure, please let us know that you are not a robot
                                         by entering the text from captcha below.
                            captcha_submit_label:
                                description: The text to show on the label of the CAPTCHA challenge submit button when
                                             I(action=BLOCK), I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Yes, I am human.
                            captcha_title:
                                description: The title used when showing a CAPTCHA challenge when I(action=BLOCK),
                                             I(block_action=SHOW_CAPTCHA), and the request is blocked.
                                default: Are you human?
                    failure_threshold:
                        description: The number of failed requests before taking action.
                        default: 10
                    is_enabled:
                        description: Enables or disables the JavaScript challenge Web Application Firewall feature.
                        required: true
                    set_http_header:
                        description: Adds an additional HTTP header to requests that fail the challenge before being
                                     passed to the origin. Only applicable when I(action=DETECT).
                        suboptions:
                            name:
                                description: The name of the header.
                            value:
                                description: The value of the header.
            origin:
                description: The key in the map of origins referencing the origin used for the Web Application Firewall.
                             The origin must already be included in Origins. Required when creating the WafConfig
                             resource, but not on update.
            protection_rules:
                description: A list of the protection rules and their details.
                suboptions:
                    action:
                        description: The action to take when the traffic is detected as malicious.
                        default: OFF
                    description:
                        description: The description of the protection rule.
                    exclusions:
                        description: The exclusions of this ProtectionRule.
                        suboptions:
                            exclusions:
                                description: The exclusions of this ProtectionRuleExclusion.
                            target:
                                description: The target of the exclusion.
                                choices:
                                    - REQUEST_COOKIES
                                    - REQUEST_COOKIE_NAMES
                                    - ARGS
                                    - ARGS_NAMES
                    key:
                        description: The unique key of the protection rule.
                    labels:
                        description: The list of labels for the protection rule.
                    mod_security_rule_ids:
                        description: The list of the ModSecurity rule IDs that apply to this protection rule.
                    name:
                        description: The name of the protection rule.
            protection_settings:
                description: The settings to apply to protection rules.
                suboptions:
                    allowed_http_methods:
                        description: The list of allowed HTTP methods. If unspecified, default to [OPTIONS, GET, HEAD, POST].
                        choices: ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH",
                                  "PROPFIND"]
                        default: ["OPTIONS", "GET", "HEAD", "POST"]
                    block_action:
                        description: If I(action=BLOCK), this specifies how the traffic is blocked when detected as
                                     malicious by a protection rule.
                        choices:
                            - SHOW_ERROR_PAGE
                            - SET_RESPONSE_CODE
                        default: SET_RESPONSE_CODE
                    block_error_page_code:
                        description: The error code to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the traffic is detected as malicious by a
                                     protection rule.
                        default: 403
                    block_error_page_description:
                        description: The description text to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the traffic is detected as malicious by a
                                     protection rule.
                        default: Access blocked by website owner. Please contact support.
                    block_error_page_message:
                        description: The message to show on the error page when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the traffic is detected as malicious by a
                                     protection rule.
                        default: Access to the website is blocked.
                    block_response_code:
                        description: The response code returned when I(action=BLOCK),
                                     I(block_action=SHOW_ERROR_PAGE), and the traffic is detected as malicious by a
                                     protection rule.
                        default: 403
                    is_response_inspected:
                        description: Inspects the response body of origin responses. Can be used to detect leakage of
                                     sensitive data.
                        default: false
                    max_argument_count:
                        description: The maximum number of arguments allowed to be passed to your application before
                                     an action is taken.
                        default: 255
                    max_name_length_per_argument:
                        description: The maximum length allowed for each argument name, in characters.
                        default: 400
                    max_response_size_in_ki_b:
                        description: The maximum response size to be fully inspected, in binary kilobytes (KiB).
                                     Anything over this limit will be partially inspected.
                        default: 1024
                    max_total_name_length_of_arguments:
                        description: The maximum length allowed for the sum of all argument names, in characters.
                        default: 64000
                    media_types:
                        description: The list of media types to allow for inspection, if I(is_response_inspected=True).
                                     Only responses with MIME types in this list will be inspected.
                        default: ["text/html", "text/plain", "text/xml"]
                    recommendations_period_in_days:
                        description: The length of time to analyze traffic, in days. After the analysis period,
                                     WafRecommendations will be populated.
                        default: 10
            threat_feeds:
                description: A list of threat intelligence feeds and the actions to apply to known malicious traffic
                             based on internet intelligence.
                suboptions:
                    action:
                        description: The action to take when traffic is flagged as malicious by data from the threat
                                     intelligence feed.
                        choices:
                            - OFF
                            - DETECT
                            - BLOCK
                        default: OFF
                    description:
                        description: The description of the threat intelligence feed.
                    key:
                        description: The unique key of the threat intelligence feed.
                    name:
                        description: The name of the threat intelligence feed.
            whitelists:
                description: A list of IP addresses that bypass the Web Application Firewall.
                suboptions:
                    addresses:
                        description: A set of IP addresses or CIDR notations to include in the whitelist.
                        required: true
                    name:
                        description: The unique name of the whitelist.
                        required: true
    state:
        description: Create or update a WAAS policy with I(state=present). Use I(state=absent) to delete a WAAS policy.
        default: present
        choices: ['present', 'absent']
    waas_policy_id:
        description: The OCID of the WAAS policy. Required when deleting a WAAS policy with I(state=absent) or updating
                     a WAAS policy with I(state=present). This option is mutually exclusive with I(compartment_id).
        required: false
        aliases: [ 'id' ]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a WAAS policy
  oci_waas_policy:
    cidr_block: '10.0.0.0/16'
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_vcn
    dns_label: ansiblevcn

- name: Updates the specified VCN's display name
  oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_vcn

- name: Delete the specified VCN
  oci_vcn:
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
waas_policy:
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
            description: The waf_config of this WaasPolicy.
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
from ansible.module_utils.oracle import oci_utils, oci_waas_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.waas.models import CreateWaasPolicyDetails
    from oci.waas.models import UpdateWaasPolicyDetails
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_TYPE = "waas_policy"


def create_waas_policy(waas_client, module):
    create_waas_policy_details = oci_waas_utils.get_waas_policy_create_model(module)
    result = oci_utils.create_and_wait_on_work_request(
        resource_type=RESOURCE_TYPE,
        create_fn=waas_client.create_waas_policy,
        kwargs_create={"create_waas_policy_details": create_waas_policy_details},
        module=module,
        client=waas_client,
        get_resource_from_work_request_response_fn=oci_waas_utils.get_waas_policy_from_work_request_response,
    )
    return result


def update_waas_policy(waas_client, module):
    origins = oci_waas_utils.get_waas_origins(module)
    policy_config = oci_waas_utils.get_waas_policy_config(module)
    waf_config = oci_waas_utils.get_waf_config_for_update(module)
    result = oci_utils.check_and_update_resource(
        resource_type=RESOURCE_TYPE,
        client=waas_client,
        get_fn=waas_client.get_waas_policy,
        kwargs_get={"waas_policy_id": module.params["waas_policy_id"]},
        update_fn=waas_client.update_waas_policy,
        primitive_params_update=["waas_policy_id"],
        kwargs_non_primitive_update={
            UpdateWaasPolicyDetails: "update_waas_policy_details"
        },
        module=module,
        update_attributes=UpdateWaasPolicyDetails().attribute_map.keys(),
        sub_attributes_of_update_model={
            "origins": origins,
            "policy_config": policy_config,
            "waf_config": waf_config,
        },
    )
    return result


def delete_waas_policy(waas_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_TYPE,
        client=waas_client,
        get_fn=waas_client.get_waas_policy,
        kwargs_get={"waas_policy_id": module.params["waas_policy_id"]},
        delete_fn=waas_client.delete_waas_policy,
        kwargs_delete={"waas_policy_id": module.params["waas_policy_id"]},
        module=module,
    )
    return result


def list_waas_policies(waas_client, module):
    if not module.params.get("compartment_id"):
        module.fail_json("compartment_id required to list waas policies.")
    compartment_id = module.params["compartment_id"]
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_waas_policy, waas_policy_id=waas_policy.id
            ).data
            for waas_policy in oci_utils.list_all_resources(
                waas_client.list_waas_policies, compartment_id=compartment_id
            )
        ]
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            domain=dict(type="str", required=False),
            additional_domains=dict(type="list", required=False),
            origins=dict(type="dict", required=False),
            policy_config=dict(type="dict", required=False),
            waf_config=dict(type="dict", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            waas_policy_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("compartment_id", "waas_policy_id")],
    )

    waas_client = oci_utils.create_service_client(module, WaasClient)
    exclude_attributes = {"display_name": True}
    exclude_attributes_even_when_user_provides_value = {"waf_config": True}
    state = module.params["state"]
    waas_policy_id = module.params["waas_policy_id"]

    if state == "absent":
        if not waas_policy_id:
            module.fail_json(
                msg="Specify waas_policy_id with state as 'absent' to delete the waas policy."
            )
        result = delete_waas_policy(waas_client, module)

    else:
        if waas_policy_id:
            result = update_waas_policy(waas_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="waas_policy",
                create_fn=create_waas_policy,
                kwargs_create={"waas_client": waas_client, "module": module},
                list_fn=waas_client.list_waas_policies,
                kwargs_list={"compartment_id": module.params["compartment_id"]},
                module=module,
                model=CreateWaasPolicyDetails(),
                exclude_attributes=exclude_attributes,
                exclude_attributes_even_when_user_provides_value=exclude_attributes_even_when_user_provides_value,
                default_attribute_values={
                    "policy_config": {
                        "certificate_id": None,
                        "is_https_enabled": False,
                        "is_https_forced": False,
                    }
                },
                get_resource_from_summary_fn=oci_waas_utils.get_waas_policy_from_summary_resource,
                get_resource_from_summary_fn_kwargs={"waas_client": waas_client},
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
