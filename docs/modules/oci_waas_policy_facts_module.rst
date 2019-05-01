:source: cloud/oracle/oci_waas_policy_facts.py

:orphan:

.. _oci_waas_policy_facts_module:


oci_waas_policy_facts - Retrieve details about WAAS Policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This module retrieves information of a specific WAAS policy or lists all WAAS policies in the given compartment.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- python >= 2.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <b>api_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_fingerprint</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_pass_phrase</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>auth_type</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this 'auth_type' module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the compartment.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_file_location</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_profile_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>display_name</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Filter policies using a list of display names.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>id</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Filter policies using a list of policy OCIDs.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Filter policies using a list of lifecycle states.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>region</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_by</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>id</li>
                                                                                                                                                                                                <li>displayName</li>
                                                                                                                                                                                                <li>timeCreated</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The value by which policies are sorted in a paginated 'List' call. If unspecified, defaults to timeCreated.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_order</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>ASC</li>
                                                                                                                                                                                                <li>DESC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The order in which to sort the results.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tenancy</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>time_created_greater_than_or_equal_to</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A filter that matches policies created on or after the specified date and time.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>time_created_less_than</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A filter that matches policies created before the specified date-time.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>waas_policy_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the WAAS policy. Required to get information of a specific waas policy.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html


Examples
--------

.. code-block:: yaml+jinja

    
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




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <b>waas_policies</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of waas policies</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{'lifecycle_state': 'ACTIVE', 'domain': 'www.example.com', 'display_name': 'ansible_test_waas_policy', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'origins': {'LBaaS': {'http_port': 80, 'custom_headers': [], 'https_port': 443, 'uri': '1.2.3.4'}}, 'waf_config': {'origin': 'LBaaS', 'protection_rules': [{'action': 'OFF', 'description': 'Cross-Site Scripting (XSS) Attempt: XSS Filters from IE', 'key': '941340', 'mod_security_rule_ids': ['941340'], 'labels': ['OWASP', 'OWASP-2017', 'CRS3', 'WASCTC', 'PCI', 'HTTP', 'A2', 'A2-2017', 'XSS', 'Cross-Site Scripting'], 'exclusions': [], 'name': 'Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer'}], 'address_rate_limiting': {'allowed_rate_per_address': 1, 'is_enabled': False, 'block_response_code': 503, 'max_delayed_count_per_address': 10}, 'js_challenge': {'is_enabled': False, 'set_http_header': {'name': 'x-jsc-alerts', 'value': '{failed_amount}'}, 'failure_threshold': 10, 'action': 'DETECT', 'action_expiration_in_seconds': 60, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'JSC-403', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'device_fingerprint_challenge': {'is_enabled': False, 'failure_threshold_expiration_in_seconds': 60, 'action_expiration_in_seconds': 60, 'max_address_count_expiration_in_seconds': 60, 'failure_threshold': 10, 'action': 'DETECT', 'max_address_count': 20, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'DFC', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'whitelists': [], 'human_interaction_challenge': {'is_enabled': False, 'set_http_header': None, 'recording_period_in_seconds': 15, 'failure_threshold_expiration_in_seconds': 60, 'action_expiration_in_seconds': 60, 'failure_threshold': 10, 'action': 'DETECT', 'interaction_threshold': 3, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'HIC', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'good_bots': [{'is_enabled': False, 'description': 'Googlebot is the search bot software used by Google.', 'key': '4a4c6e7b-4d89-4141-8555-ec3b22b90a73', 'name': 'Googlebot '}], 'access_rules': [], 'captchas': []}, 'defined_tags': {'example_namespace': {'example_key': 'example_value'}}, 'freeform_tags': {'example_freeform_key': 'example_freeform_value'}, 'time_created': '2019-03-22T13:02:55.563000+00:00', 'policy_config': {'certificate_id': None, 'is_https_enabled': False, 'is_https_forced': False}, 'cname': 'www-exampledomain-com.b.waas.oci.oraclecloud.net', 'additional_domains': ['www.exampledomain1.com', 'www.exampledomain2.com'], 'id': 'ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx'}]</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The current lifecycle state of the WAAS policy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>domain</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The web application domain that the WAAS policy protects.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">www.exampledomain.com</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>display_name</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The user-friendly name of the WAAS policy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">examplewaaspolicy1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The OCID of the WAAS policy's compartment.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>origins</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A map of host to origin for the web application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'LBaaS': {'http_port': 80, 'custom_headers': [], 'https_port': 443, 'uri': '1.2.3.4'}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>waf_config</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The WAF config of this policy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'origin': 'LBaaS', 'protection_rules': [{'action': 'OFF', 'description': 'Cross-Site Scripting (XSS) Attempt: XSS Filters from IE', 'key': '941340', 'mod_security_rule_ids': ['941340'], 'labels': ['OWASP', 'OWASP-2017', 'CRS3', 'WASCTC', 'PCI', 'HTTP', 'A2', 'A2-2017', 'XSS', 'Cross-Site Scripting'], 'exclusions': [], 'name': 'Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer'}], 'address_rate_limiting': {'allowed_rate_per_address': 1, 'is_enabled': False, 'block_response_code': 503, 'max_delayed_count_per_address': 10}, 'js_challenge': {'is_enabled': False, 'set_http_header': {'name': 'x-jsc-alerts', 'value': '{failed_amount}'}, 'failure_threshold': 10, 'action': 'DETECT', 'action_expiration_in_seconds': 60, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'JSC-403', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'device_fingerprint_challenge': {'is_enabled': False, 'failure_threshold_expiration_in_seconds': 60, 'action_expiration_in_seconds': 60, 'max_address_count_expiration_in_seconds': 60, 'failure_threshold': 10, 'action': 'DETECT', 'max_address_count': 20, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'DFC', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'whitelists': [], 'human_interaction_challenge': {'is_enabled': False, 'set_http_header': None, 'recording_period_in_seconds': 15, 'failure_threshold_expiration_in_seconds': 60, 'action_expiration_in_seconds': 60, 'failure_threshold': 10, 'action': 'DETECT', 'interaction_threshold': 3, 'challenge_settings': {'block_error_page_message': 'Access to the website is blocked.', 'captcha_footer': 'Enter the letters and numbers as they are shown in image above.', 'block_error_page_code': 'HIC', 'block_action': 'SHOW_ERROR_PAGE', 'captcha_title': 'Are you human?', 'captcha_header': 'We have detected an increased number of attempts to access this website.', 'block_response_code': 403, 'block_error_page_description': 'Access blocked by website owner. Please contact support.', 'captcha_submit_label': 'Yes, I am human.'}}, 'good_bots': [{'is_enabled': False, 'description': 'Googlebot is the search bot software used by Google', 'key': '4a4c6e7b-4d89-4141-8555-ec3b22b90a73', 'name': 'Googlebot '}], 'access_rules': [], 'captchas': []}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>defined_tags</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'example_namespace': {'example_key': 'example_value'}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>freeform_tags</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A simple key-value pair without any defined schema.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'example_freeform_key': 'example_freeform_value'}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_created</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The date and time the policy was created, expressed in RFC 3339 timestamp format.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2019-03-22 13:02:55.563000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>policy_config</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The policy_config of the WaasPolicy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'certificate_id': None, 'is_https_enabled': False, 'is_https_forced': False}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>cname</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">www-exampledomain-com.b.waas.oci.oraclecloud.net</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>additional_domains</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>An array of additional domains for this web application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">['www.exampledomain1.com', 'www.exampledomain2.com']</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>id</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The OCID of the WAAS policy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                    
                                        </table>
    <br/><br/>


Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



Author
~~~~~~

- Manoj Meda (@manojmeda)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_waas_policy_facts.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
