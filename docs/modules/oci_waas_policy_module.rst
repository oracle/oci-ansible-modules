:source: cloud/oracle/oci_waas_policy.py

:orphan:

.. _oci_waas_policy_module:


oci_waas_policy - Manage WAAS policies in OCI
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This module allows the user to create, delete and update WAAS policies in OCI.



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
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
                    <b>additional_domains</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>An array of additional domains for the specified web application.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>api_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>api_user_fingerprint</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>api_user_key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>api_user_key_pass_phrase</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the compartment.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>config_file_location</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>config_profile_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>defined_tags</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>display_name</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>domain</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The web application domain that the WAAS policy protects.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>force_create</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>freeform_tags</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>key_by</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>origins</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>http_port</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTP port on the origin that the web application listens on. If unspecified, defaults to 80.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>custom_headers</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of HTTP headers to forward to your origin.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the header.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>value</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of the header.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>https_port</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTPS port on the origin that the web application listens on. If unspecified, defaults to 443.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>uri</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The URI of the origin. Does not support paths. Port numbers should be specified in the http_port and https_port fields.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="4">
                    <b>policy_config</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Config for the WAAS policy.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>certificate_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the SSL certificate to use if HTTPS is supported.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>is_https_enabled</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                                <td>
                                            <div>Enable or disable HTTPS support. If true, a certificateId is required.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>is_https_forced</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                                <td>
                                            <div>Force HTTP to HTTPS redirection.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="4">
                    <b>region</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>state</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Create or update a WAAS policy with <em>state=present</em>. Use <em>state=absent</em> to delete a WAAS policy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>tenancy</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>waas_policy_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the WAAS policy. Required when deleting a WAAS policy with <em>state=absent</em> or updating a WAAS policy with <em>state=present</em>. This option is mutually exclusive with <em>compartment_id</em>.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>waf_config</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The WAF config for the WAAS policy.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>origin</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in Origins. Required when creating the WafConfig resource, but not on update.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>protection_rules</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of the protection rules and their details.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                                <td>
                                            <div>The action to take when the traffic is detected as malicious.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>description</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique key of the protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>mod_security_rule_ids</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of the ModSecurity rule IDs that apply to this protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>labels</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of labels for the protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>exclusions</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The exclusions of this ProtectionRule.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>exclusions</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The exclusions of this ProtectionRuleExclusion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>target</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>REQUEST_COOKIES</li>
                                                                                                                                                                                                <li>REQUEST_COOKIE_NAMES</li>
                                                                                                                                                                                                <li>ARGS</li>
                                                                                                                                                                                                <li>ARGS_NAMES</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The target of the exclusion.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the protection rule.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>address_rate_limiting</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address rate limiting settings used to limit the number of requests from an address.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>allowed_rate_per_address</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1</div>
                                    </td>
                                                                <td>
                                            <div>The number of allowed requests per second from one IP address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_enabled</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enables or disables the address rate limiting Web Application Firewall feature.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">503</div>
                                    </td>
                                                                <td>
                                            <div>The response status code returned when a request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_delayed_count_per_address</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                                <td>
                                            <div>The maximum number of requests allowed to be queued before subsequent requests are dropped.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>js_challenge</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_enabled</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enables or disables the JavaScript challenge Web Application Firewall feature.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>set_http_header</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when <em>action=DETECT</em>.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the header.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>value</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of the header.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_threshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                                <td>
                                            <div>The number of failed requests before taking action.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>DETECT</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to take against requests from detected bots.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds between challenges from the same IP address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>challenge_settings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The challenge settings.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_message</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access to the website is blocked.</div>
                                    </td>
                                                                <td>
                                            <div>The message to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_footer</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Enter the letters and numbers as they are shown in image above.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the footer when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The error code to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SET_RESPONSE_CODE</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>SHOW_ERROR_PAGE</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>SHOW_CAPTCHA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The method used to block requests that fail the challenge if <em>action=BLOCK</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_title</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Are you human?</div>
                                    </td>
                                                                <td>
                                            <div>The title used when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_header</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the header when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The response status code to return when <em>action=BLOCK</em>, <em>block_action=SET_RESPONSE_CODE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_description</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access blocked by website owner. Please contact support.</div>
                                    </td>
                                                                <td>
                                            <div>The description text to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_submit_label</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Yes, I am human.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show on the label of the CAPTCHA challenge submit button when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                    
                                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>device_fingerprint_challenge</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_enabled</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enables or disables the device fingerprint challenge Web Application Firewall feature.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_threshold_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds before the failure threshold resets.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds between challenges for the same IP address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_address_count_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds before the maximum addresses count resets.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_threshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                                <td>
                                            <div>The number of failed requests allowed before taking action.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>DETECT</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to take on requests from detected bots.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_address_count</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">20</div>
                                    </td>
                                                                <td>
                                            <div>The maximum number of IP addresses permitted with the same device fingerprint.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>challenge_settings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The challenge settings.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_message</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access to the website is blocked.</div>
                                    </td>
                                                                <td>
                                            <div>The message to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_footer</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Enter the letters and numbers as they are shown in image above.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the footer when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The error code to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SET_RESPONSE_CODE</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>SHOW_ERROR_PAGE</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>SHOW_CAPTCHA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The method used to block requests that fail the challenge if <em>action=BLOCK</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_title</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Are you human?</div>
                                    </td>
                                                                <td>
                                            <div>The title used when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_header</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the header when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The response status code to return when <em>action=BLOCK</em>, <em>block_action=SET_RESPONSE_CODE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_description</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access blocked by website owner. Please contact support.</div>
                                    </td>
                                                                <td>
                                            <div>The description text to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_submit_label</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Yes, I am human.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show on the label of the CAPTCHA challenge submit button when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                    
                                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>whitelists</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of IP addresses that bypass the Web Application Firewall.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>addresses</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A set of IP addresses or CIDR notations to include in the whitelist.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique name of the whitelist.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>human_interaction_challenge</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_enabled</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enables or disables the human interaction challenge Web Application Firewall feature.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>set_http_header</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when <em>action=DETECT</em>.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the header.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>value</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of the header.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>recording_period_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">15</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds to record the interactions from the user.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_threshold_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds before the failure threshold resets.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action_expiration_in_seconds</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">60</div>
                                    </td>
                                                                <td>
                                            <div>The number of seconds between challenges for the same IP address.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_threshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                                <td>
                                            <div>The number of failed requests allowed before taking action.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>DETECT</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to take on requests from detected bots.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>interaction_threshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3</div>
                                    </td>
                                                                <td>
                                            <div>The number of interactions required to pass the challenge.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>challenge_settings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The challenge settings.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_message</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access to the website is blocked.</div>
                                    </td>
                                                                <td>
                                            <div>The message to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_footer</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Enter the letters and numbers as they are shown in image above.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the footer when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The error code to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SET_RESPONSE_CODE</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>SHOW_ERROR_PAGE</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>SHOW_CAPTCHA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The method used to block requests that fail the challenge if <em>action=BLOCK</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_title</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Are you human?</div>
                                    </td>
                                                                <td>
                                            <div>The title used when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_header</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the header when showing a CAPTCHA challenge when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The response status code to return when <em>action=BLOCK</em>, <em>block_action=SET_RESPONSE_CODE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>block_error_page_description</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access blocked by website owner. Please contact support.</div>
                                    </td>
                                                                <td>
                                            <div>The description text to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>captcha_submit_label</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Yes, I am human.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show on the label of the CAPTCHA challenge submit button when <em>action=BLOCK</em>, <em>block_action=SHOW_CAPTCHA</em>, and the request is blocked.</div>
                                                        </td>
            </tr>
                    
                                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>good_bots</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of bots allowed to access the web application.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_enabled</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Enables or disables the bot.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>description</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the bot.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique key for the bot.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The bot name.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>access_rules</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of ALLOW, DETECT, and BLOCK rules, based on different criteria.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_message</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access to the website is blocked.</div>
                                    </td>
                                                                <td>
                                            <div>The message to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the access criteria are met.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique name of the access rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access rules</div>
                                    </td>
                                                                <td>
                                            <div>The error code to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the access criteria are met.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>SET_RESPONSE_CODE</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>SHOW_ERROR_PAGE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The method used to block requests if <em>action=BLOCK</em> and the access criteria are met.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>criteria</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of access rule criteria.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>condition</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The criteria the access rule uses to determine if action should be taken on a request.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>value</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>URL_IS</li>
                                                                                                                                                                                                <li>URL_IS_NOT</li>
                                                                                                                                                                                                <li>URL_STARTS_WITH</li>
                                                                                                                                                                                                <li>URL_PART_ENDS_WITH</li>
                                                                                                                                                                                                <li>URL_PART_CONTAINS</li>
                                                                                                                                                                                                <li>URL_REGEX</li>
                                                                                                                                                                                                <li>IP_IS</li>
                                                                                                                                                                                                <li>IP_IS_NOT</li>
                                                                                                                                                                                                <li>HTTP_HEADER_CONTAINS</li>
                                                                                                                                                                                                <li>COUNTRY_IS</li>
                                                                                                                                                                                                <li>COUNTRY_IS_NOT</li>
                                                                                                                                                                                                <li>USER_AGENT_IS</li>
                                                                                                                                                                                                <li>USER_AGENT_IS_NOT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The criteria value.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ALLOW</div>
                                    </td>
                                                                <td>
                                            <div>The action to take when the access criteria are met for a rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The response status code to return when <em>action=BLOCK</em>, <em>block_action=SET_RESPONSE_CODE</em>, and the access criteria are met.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_description</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access blocked by website owner. Please contact support.</div>
                                    </td>
                                                                <td>
                                            <div>The description text to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the access criteria are met.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>protection_settings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The settings to apply to protection rules.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>media_types</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;text/html&#39;, u&#39;text/plain&#39;, u&#39;text/xml&#39;]</div>
                                    </td>
                                                                <td>
                                            <div>The list of media types to allow for inspection, if <em>is_response_inspected=True</em>. Only responses with MIME types in this list will be inspected.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_message</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access to the website is blocked.</div>
                                    </td>
                                                                <td>
                                            <div>The message to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the traffic is detected as malicious by a protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_total_name_length_of_arguments</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">64000</div>
                                    </td>
                                                                <td>
                                            <div>The maximum length allowed for the sum of all argument names, in characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>recommendations_period_in_days</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                                <td>
                                            <div>The length of time to analyze traffic, in days. After the analysis period, WafRecommendations will be populated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The error code to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the traffic is detected as malicious by a protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_response_size_in_ki_b</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1024</div>
                                    </td>
                                                                <td>
                                            <div>The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SHOW_ERROR_PAGE</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>SET_RESPONSE_CODE</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If <em>action=BLOCK</em>, this specifies how the traffic is blocked when detected as malicious by a protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_argument_count</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">255</div>
                                    </td>
                                                                <td>
                                            <div>The maximum number of arguments allowed to be passed to your application before an action is taken.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>max_name_length_per_argument</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">400</div>
                                    </td>
                                                                <td>
                                            <div>The maximum length allowed for each argument name, in characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>is_response_inspected</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                                <td>
                                            <div>Inspects the response body of origin responses. Can be used to detect leakage of sensitive data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_response_code</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">403</div>
                                    </td>
                                                                <td>
                                            <div>The response code returned when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the traffic is detected as malicious by a protection rule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>allowed_http_methods</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>OPTIONS</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li><div style="color: blue"><b>GET</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li><div style="color: blue"><b>HEAD</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li><div style="color: blue"><b>POST</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>PUT</li>
                                                                                                                                                                                                <li>DELETE</li>
                                                                                                                                                                                                <li>TRACE</li>
                                                                                                                                                                                                <li>CONNECT</li>
                                                                                                                                                                                                <li>PATCH</li>
                                                                                                                                                                                                <li>PROPFIND</li>
                                                                                    </ul>
                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;OPTIONS&#39;, u&#39;GET&#39;, u&#39;HEAD&#39;, u&#39;POST&#39;]</div>
                                    </td>
                                                                <td>
                                            <div>The list of allowed HTTP methods. If unspecified, default to [OPTIONS, GET, HEAD, POST].</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>block_error_page_description</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Access blocked by website owner. Please contact support.</div>
                                    </td>
                                                                <td>
                                            <div>The description text to show on the error page when <em>action=BLOCK</em>, <em>block_action=SHOW_ERROR_PAGE</em>, and the traffic is detected as malicious by a protection rule.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>captchas</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>submit_label</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text to show on the label of the CAPTCHA challenge submit button.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>header_text</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">We have detected an increased number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the text from the image below.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the header when showing a CAPTCHA challenge.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>title</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The title used when displaying a CAPTCHA challenge.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>url</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique URL path at which to show the CAPTCHA challenge.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>session_expiration_in_seconds</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The amount of time before the CAPTCHA expires, in seconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>footer_text</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Enter the letters and numbers as they are shown in the image above.</div>
                                    </td>
                                                                <td>
                                            <div>The text to show in the footer when showing a CAPTCHA challenge.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>failure_message</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text to show when incorrect CAPTCHA text is entered.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <b>threat_feeds</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.</div>
                                                        </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                                                                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>DETECT</li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                                    <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                                <td>
                                            <div>The action to take when traffic is flagged as malicious by data from the threat intelligence feed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>description</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The description of the threat intelligence feed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique key of the threat intelligence feed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the threat intelligence feed.</div>
                                                        </td>
            </tr>
                    
                                    
                                                <tr>
                                                                <td colspan="4">
                    <b>wait</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to wait for create or delete operation to complete.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>wait_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1200</div>
                                    </td>
                                                                <td>
                                                                        <div>Time, in seconds, to wait when <em>wait=yes</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <b>wait_until</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The lifecycle state to wait for the resource to transition into when <em>wait=yes</em>. By default, when <em>wait=yes</em>, we wait for the resource to get into ACTIVE/ATTACHED/AVAILABLE/PROVISIONED/ RUNNING applicable lifecycle state during create operation &amp; to get into DELETED/DETACHED/ TERMINATED lifecycle state during delete operation.</div>
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
                    <b>waas_policy</b>
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
                                            <div>The waf_config of this WaasPolicy.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_waas_policy.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
