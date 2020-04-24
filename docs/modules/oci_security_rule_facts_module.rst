:source: cloud/oracle/oci_security_rule_facts.py

:orphan:

.. _oci_security_rule_facts_module:


oci_security_rule_facts -- Fetches details about one or multiple SecurityRule resources in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Fetches details about one or multiple SecurityRule resources in Oracle Cloud Infrastructure
- Lists the security rules in the specified network security group.



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
                    <b>direction</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>EGRESS</li>
                                                                                                                                                                                                <li>INGRESS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets, or `INGRESS` for rules that allow inbound IP packets.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>network_security_group_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the network security group.</div>
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
                    <b>sort_by</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TIMECREATED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The field to sort by.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_order</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ASC</li>
                                                                                                                                                                                                <li>DESC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.</div>
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

    
    - name: List security_rules
      oci_security_rule_facts:
        network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx





Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <b>security_rules</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>List of SecurityRule resources</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;source&#x27;: &#x27;source_example&#x27;, &#x27;destination&#x27;: &#x27;destination_example&#x27;, &#x27;icmp_options&#x27;: {&#x27;code&#x27;: 56, &#x27;type&#x27;: 56}, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;is_stateless&#x27;: True, &#x27;destination_type&#x27;: &#x27;CIDR_BLOCK&#x27;, &#x27;id&#x27;: &#x27;04ABEC&#x27;, &#x27;source_type&#x27;: &#x27;CIDR_BLOCK&#x27;, &#x27;is_valid&#x27;: True, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;direction&#x27;: &#x27;EGRESS&#x27;, &#x27;tcp_options&#x27;: {&#x27;destination_port_range&#x27;: {&#x27;min&#x27;: 56, &#x27;max&#x27;: 56}, &#x27;source_port_range&#x27;: {&#x27;min&#x27;: 56, &#x27;max&#x27;: 56}}, &#x27;udp_options&#x27;: {&#x27;destination_port_range&#x27;: {&#x27;min&#x27;: 56, &#x27;max&#x27;: 56}, &#x27;source_port_range&#x27;: {&#x27;min&#x27;: 56, &#x27;max&#x27;: 56}}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}]</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>description</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An optional description of your choice for the rule.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>destination</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.</div>
                                                    <div>Allowed values:</div>
                                                    <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                                    <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                                    <div>* The OCID of a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">destination_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>destination_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Type of destination for the rule. Required if `direction` = `EGRESS`.</div>
                                                    <div>Allowed values:</div>
                                                    <div>* `CIDR_BLOCK`: If the rule&#x27;s `destination` is an IP address range in CIDR notation.</div>
                                                    <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `destination` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic destined for a particular `Service` through a service gateway).</div>
                                                    <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `destination` is the OCID of a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CIDR_BLOCK</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>direction</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EGRESS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>icmp_options</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code as defined in: - <a href='http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml'>ICMP Parameters</a> - <a href='https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml'>ICMPv6 Parameters</a></div>
                                                    <div>If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (&quot;Destination Unreachable&quot;) code 4 (&quot;Fragmentation Needed and Don&#x27;t Fragment was Set&quot;). If you need to specify multiple codes for a single type, create a separate security rule for each.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>code</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The ICMP code (optional).</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>type</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The ICMP type.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An Oracle-assigned identifier for the security rule. You specify this ID when you want to update or delete the rule.</div>
                                                    <div>Example: `04ABEC`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">04ABEC</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>is_stateless</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>is_valid</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Whether the rule is valid. The value is `True` when the rule is first created. If the rule&#x27;s `source` or `destination` is a network security group, the value changes to `False` if that network security group is deleted.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>protocol</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The transport protocol. Specify either `all` or an IPv4 protocol number as defined in <a href='http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'>Protocol Numbers</a>. Options are supported only for ICMP (&quot;1&quot;), TCP (&quot;6&quot;), UDP (&quot;17&quot;), and ICMPv6 (&quot;58&quot;).</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>source</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.</div>
                                                    <div>Allowed values:</div>
                                                    <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                                    <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                                    <div>* The OCID of a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">source_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>source_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Type of source for the rule. Required if `direction` = `INGRESS`.</div>
                                                    <div>* `CIDR_BLOCK`: If the rule&#x27;s `source` is an IP address range in CIDR notation.</div>
                                                    <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `source` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic coming from a particular `Service` through a service gateway).</div>
                                                    <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `source` is the OCID of a <a href='https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CIDR_BLOCK</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>tcp_options</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>destination_port_range</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>max</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>min</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>source_port_range</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>max</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>min</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>time_created</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The date and time the security rule was created. Format defined by RFC3339.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20 19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <b>udp_options</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>destination_port_range</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>max</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>min</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>source_port_range</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>max</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>min</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
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

- Manoj Meda (@manojmeda)
- Mike Ross (@mross22)
- Nabeel Al-Saber (@nalsaber)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_security_rule_facts.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
