:source: cloud/oracle/oci_load_balancer_facts.py

:orphan:

.. _oci_load_balancer_facts_module:


oci_load_balancer_facts -- Fetches details of the OCI Load Balancer
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Fetches details of the OCI Load Balancer.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
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
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_fingerprint</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_file</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
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
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
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
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible` playbooks within an OCI compute instance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>compartment_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the compartment in which this Load Balancer exists</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_file_location</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
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
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>detail</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>full</li>
                                                                                                                                                                                                <li>simple</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The level of detail to return for each result.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>display_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Use <em>display_name</em> along with the other options to return only resources that match the given display name exactly.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CREATING</li>
                                                                                                                                                                                                <li>FAILED</li>
                                                                                                                                                                                                <li>ACTIVE</li>
                                                                                                                                                                                                <li>DELETING</li>
                                                                                                                                                                                                <li>DELETED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>A filter to return only resources that match the given lifecycle state.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>load_balancer_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the Load Balancer whose details needs to be fetched.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>region</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tenancy</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
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

    
    #Fetch Load Balancer
    - name: List Load Balancer
      oci_load_balancer_facts:
          compartment_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

    #Fetch specific Load Balancer
    - name: List a specific Load Balancer
      oci_load_balancer_facts:
          load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'




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
                    <b>load_balancers</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Attributes of the  Load Balancers.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;path_route_sets&#x27;: {&#x27;ansible_path_route_set&#x27;: {&#x27;path_routes&#x27;: [{&#x27;backend_set_name&#x27;: &#x27;ansible_backend_set&#x27;, &#x27;path&#x27;: &#x27;/example/user&#x27;, &#x27;path_match_type&#x27;: {&#x27;match_type&#x27;: &#x27;EXACT_MATCH&#x27;}}]}}, &#x27;lifecycle_state&#x27;: &#x27;ACTIVE&#x27;, &#x27;listeners&#x27;: {&#x27;listener1&#x27;: {&#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;name&#x27;: &#x27;listerner1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;port&#x27;: 80, &#x27;connection_configuration&#x27;: {&#x27;idle_timeout&#x27;: 1200}, &#x27;default_backend_set_name&#x27;: &#x27;backend1&#x27;}}, &#x27;subnet_ids&#x27;: [&#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;, &#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;], &#x27;ip_addresses&#x27;: [{&#x27;ip_address&#x27;: &#x27;129.213.72.32&#x27;, &#x27;is_public&#x27;: True}], &#x27;backend_sets&#x27;: {&#x27;backend1&#x27;: {&#x27;session_persistence_configuration&#x27;: None, &#x27;backends&#x27;: [{&#x27;weight&#x27;: 1, &#x27;name&#x27;: &#x27;10.159.34.21:8080&#x27;, &#x27;ip_address&#x27;: &#x27;10.159.34.21&#x27;, &#x27;port&#x27;: 8080, &#x27;drain&#x27;: False, &#x27;backup&#x27;: False, &#x27;offline&#x27;: False}], &#x27;name&#x27;: &#x27;backend1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;policy&#x27;: &#x27;LEAST_CONNECTIONS&#x27;, &#x27;health_checker&#x27;: {&#x27;timeout_in_millis&#x27;: 6000, &#x27;retries&#x27;: 3, &#x27;response_body_regex&#x27;: &#x27;^(500|40[1348])$&#x27;, &#x27;url_path&#x27;: &#x27;/healthcheck&#x27;, &#x27;port&#x27;: 8080, &#x27;interval_in_millis&#x27;: 30000, &#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;return_code&#x27;: 200}}}, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;42&#x27;}}, &#x27;display_name&#x27;: &#x27;ansible_lb955&#x27;, &#x27;certificates&#x27;: {&#x27;certs1&#x27;: {&#x27;public_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n- ----END CERTIFICATE-----&#x27;, &#x27;ca_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n-----END CERTIFICATE -----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----&#x27;, &#x27;certificate_name&#x27;: &#x27;certs1&#x27;}}, &#x27;shape_name&#x27;: &#x27;100Mbps&#x27;, &#x27;time_created&#x27;: &#x27;2018-01-06T18:22:17.198000+00:00&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxEXAMPLExxxxx&#x27;, &#x27;is_private&#x27;: False, &#x27;id&#x27;: &#x27;ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx&#x27;}]</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>backend_sets</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The configuration details for a load balancer backend set</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;backend1&#x27;: {&#x27;backends&#x27;: [{&#x27;weight&#x27;: 1, &#x27;name&#x27;: &#x27;10.159.34.21:8080&#x27;, &#x27;ip_address&#x27;: &#x27;10.159.34.21&#x27;, &#x27;port&#x27;: 8080, &#x27;drain&#x27;: False, &#x27;backup&#x27;: False, &#x27;offline&#x27;: False}], &#x27;health_checker&#x27;: {&#x27;timeout_in_millis&#x27;: 6000, &#x27;retries&#x27;: 3, &#x27;response_body_regex&#x27;: &#x27;^(500|40[1348])$&#x27;, &#x27;url_path&#x27;: &#x27;/healthcheck&#x27;, &#x27;port&#x27;: 8080, &#x27;interval_in_millis&#x27;: 30000, &#x27;policy&#x27;: &#x27;LEAST_CONNECTIONS&#x27;, &#x27;session_persistence_configuration&#x27;: None, &#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;return_code&#x27;: 200, &#x27;ssl_configuration&#x27;: None, &#x27;name&#x27;: &#x27;backend1&#x27;}}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>certificates</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The configuration details for a listener certificate bundle.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;certs1&#x27;: {&#x27;public_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE----- MIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----&#x27;, &#x27;ca_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----&#x27;, &#x27;certificate_name&#x27;: &#x27;certs1&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>compartment_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The identifier of the compartment containing the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>defined_tags</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>display_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name assigned to the Load Balancer during creation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ansible_lb</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>freeform_tags</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined                              name, type, or namespace.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Identifier of the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The current state of the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>listeners</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The listener configuration details.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;listerner1&#x27;: {&#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;name&#x27;: &#x27;listerner1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;port&#x27;: 80, &#x27;connection_configuration&#x27;: {&#x27;idle_timeout&#x27;: 1200}, &#x27;default_backend_set_name&#x27;: &#x27;backend1&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>path_route_sets</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The path route sets configuration details.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;ansible_path_route_set&#x27;: {&#x27;path_routes&#x27;: [{&#x27;backend_set_name&#x27;: &#x27;ansible_backend_set&#x27;, &#x27;path&#x27;: &#x27;/example/user&#x27;, &#x27;path_match_type&#x27;: {&#x27;match_type&#x27;: &#x27;EXACT_MATCH&#x27;}}]}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>shape_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">100Mbps</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>subnet_ids</b>
                    <div style="font-size: small; color: purple">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>An array of subnet OCIDs.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;, &#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_created</b>
                    <div style="font-size: small; color: purple">datetime</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Date and time when the Load Balancer was created, in the format defined by RFC3339</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-08-25 21:10:29.600000+00:00</div>
                                    </td>
            </tr>
                    
                                        </table>
    <br/><br/>


Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is :ref:`maintained by the Ansible Community <modules_support>`. *[community]*





Authors
~~~~~~~

- Debayan Gupta(@debayan_gupta)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_load_balancer_facts.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
