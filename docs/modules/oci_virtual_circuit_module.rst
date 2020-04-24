:source: cloud/oracle/oci_virtual_circuit.py

:orphan:

.. _oci_virtual_circuit_module:


oci_virtual_circuit -- Create, update and delete OCI Virtual Circuit
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create an OCI Virtual Circuit to use with Oracle Cloud Infrastructure FastConnect
- Update an OCI Virtual Circuit, if present
- Delete an OCI Virtual Circuit, if present.



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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>bandwidth_shape_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The provisioned data rate of the connection.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>compartment_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the compartment under which this Virtual Circuit would be created. Mandatory for create operation.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>cross_connect_mappings</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>An array of mappings, each containing properties for a cross-connect or cross-connect group that is associated with this virtual circuit.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>bgp_md5_auth_key</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set, that means you don&#x27;t use BGP MD5 authentication.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>cross_connect_or_cross_connect_group_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>customer_bgp_peering_ip</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The BGP IP address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IP address of the customer&#x27;s edge router. If the session goes from Oracle to a provider, this is the BGP IP address of the provider&#x27;s edge router. Must use a /30 or /31 subnet mask. There&#x27;s one exception, for a public virtual circuit, Oracle specifies the BGP IP addresses.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>oracle_bgp_peering_ip</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address for Oracle&#x27;s end of the BGP session. Must use a /30 or /31 subnet mask. If the session goes from Oracle to a customer&#x27;s edge router, the customer specifies this information. If the session goes from Oracle to a provider&#x27;s edge router, the provider specifies this. There&#x27;s one exception, for a public virtual circuit, Oracle specifies the BGP IP addresses.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>vlan</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>customer_bgp_asn</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Your BGP ASN (either public or private). Provide this value only if there&#x27;s a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>delete_cross_connect_mappings</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Delete any cross connect mappings in the virtual circuit that is specified in <em>cross_connect_mappings</em>. If <em>delete_cross_connect_mappings=yes</em>, cross connect mappings provided by <em>cross_connect_mappings</em> would be deleted from existing cross connect mappings, if they are part of existing cross connect mappings. If they are not part of existing cross connect mappings, they will be ignored. <em>delete_cross_connect_mappings</em> and <em>purge_cross_connect_mappings</em> are mutually exclusive.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>delete_public_prefixes</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"no"</div>
                                    </td>
                                                                <td>
                                                                        <div>Indicates whether public prefixes associated with a public virtual circuit needs to be deleted. If <em>delete_public_prefixes=false</em>, then input publi prefixes gets added.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>display_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>force_create</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn&#x27;t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>gateway_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>For private virtual circuits only. The OCID of the dynamic routing gateway (DRG) that this virtual circuit uses.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>key_by</b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Deprecated. Instead use provider_service_id.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider_service_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the service offered by the provider (if you&#x27;re connecting via a provider).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider_service_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Deprecated. Instead use provider_service_id.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider_state</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACTIVE</li>
                                                                                                                                                                                                <li>INACTIVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The provider&#x27;s state in relation to this virtual circuit. Relevant only if the customer is using FastConnect via a provider. ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>public_prefixes</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>cidr_block</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An individual public IP prefix (CIDR) to add to the public virtual circuit. Must be /31 or less specific.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>purge_cross_connect_mappings</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Purge cross connect mappings from virtual circuit which are not present in the provided cross connect mappings list.If <em>purge_cross_connect_mappings=no</em>, provided cross connect mappings would be appended to existing cross connect mappings. <em>purge_cross_connect_mappings</em> and <em>delete_cross_connect_mappings</em> are mutually exclusive.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>reference_comment</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Provider-supplied reference information about this virtual circuit. Relevant only if the customer is using FastConnect via a provider. To be updated only by the provider.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>region</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region where this virtual circuit is located.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>state</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Create,update or delete cross-connect group. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                <tr>
                                                                <td colspan="2">
                    <b>type</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PUBLIC</li>
                                                                                                                                                                                                <li>PRIVATE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of IP addresses used in this virtual circuit. PRIVATE means RFC 1918 addresses (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>virtual_circuit_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the Virtual Circuit. Mandatory for delete and update.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to wait for create or delete operation to complete.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait_timeout</b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">2000</div>
                                    </td>
                                                                <td>
                                                                        <div>Time, in seconds, to wait when <em>wait=yes</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait_until</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
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

    
    # Note: These examples do not set authentication details.
    # Create a new colocated Virtual Circuit
    - name: Create a new colocated Virtual Circuit
      oci_virtual_circuit:
          compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
          display_name: 'ansible-virtual-circuit'
          cross_connect_mappings:
                - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
                  vlan: 100
          public_prefixes:
                 - 206.209.218.0/24
          customer_bgp_asn: 5
          type: 'PUBLIC'
          port_speed_shape_name: '10 Gbps'
          state: 'present'

    # Create a new colocated Virtual Circuit
    - name: Create a new colocated Virtual Circuit of private type
      oci_virtual_circuit:
          compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
          display_name: 'ansible-virtual-circuit-private'
          cross_connect_mappings:
                - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
                  customer_bgp_peering_ip: '10.0.0.18/31'
                  oracle_bgp_peering_ip: '10.0.0.19/31'
                  vlan: 100
          customer_bgp_asn: 5
          type: 'PRIVATE'
          port_speed_shape_name: '10 Gbps'
          state: 'present'

    # Create a Virtual Circuit using Provider
    - name: Create a Virtual Circuit using Provider
      oci_virtual_circuit:
          compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
          display_name: 'ansible-virtual-circuit'
          provider_service_id: 'ocid1.providerservice...xxxxxEXAMPLExxxxx'
          customer_bgp_asn: 5
          type: 'PUBLIC'
          port_speed_shape_name: '10 Gbps'
          state: 'present'

    # Update an existing Virtual Circuit's Cross Connect Mappings
    - name: Update an existing Virtual Circuit's Cross Connect Mappings
      oci_virtual_circuit:
          virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
          cross_connect_mappings:
                - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
                  vlan: 105
          state: 'present'

    # Update an existing Virtual Circuit's Cross Connect Mappings by appending new Cross Connect Mappings
    - name: Update an existing Virtual Circuit's Cross Connect Mappings by appending new Cross Connect Mappings
      oci_virtual_circuit:
          virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
          cross_connect_mappings:
                - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
                  vlan: 100
          purge_cross_connect_mappings: false
          state: 'present'

    # Update an existing Virtual Circuit's Cross Connect Mappings by deleting a Cross Connect Mappings
    - name: Update an existing Virtual Circuit's Cross Connect Mappings by deleting a Cross Connect Mappings
      oci_virtual_circuit:
          virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
          cross_connect_mappings:
                - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
                  vlan: 100
          delete_cross_connect_mappings: false
          state: 'present'

    # Update an existing Virtual Circuit by deleting Public Prefixes
    - name: Update an existing Virtual Circuit by deleting Public Prefixes
      oci_virtual_circuit:
          virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
          public_prefixes:
                - '10.0.0.21/31'
          delete_public_prefixes: true
          state: 'present'

    # Delete Virtual Circuit
    - name: Delete Virtual Circuit
      oci_virtual_circuit:
          virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
          state: 'absent'




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
                    <b>oci_virtual_circuit</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Attributes of the Virtual Circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;public_prefixes&#x27;: None, &#x27;provider_state&#x27;: None, &#x27;bandwidth_shape_name&#x27;: &#x27;10 Gbps&#x27;, &#x27;provider_service_id&#x27;: None, &#x27;service_type&#x27;: &#x27;COLOCATED&#x27;, &#x27;region&#x27;: None, &#x27;cross_connect_mappings&#x27;: [{&#x27;oracle_bgp_peering_ip&#x27;: &#x27;169.254.203.201/30&#x27;, &#x27;bgp_md5_auth_key&#x27;: None, &#x27;vlan&#x27;: 105, &#x27;cross_connect_or_cross_connect_group_id&#x27;: &#x27;ocid1.crossconnectgroup.xxxxxEXAMPLExxxxx&#x27;, &#x27;customer_bgp_peering_ip&#x27;: &#x27;169.254.203.202/30&#x27;}], &#x27;display_name&#x27;: &#x27;sample-virtual-circuit&#x27;, &#x27;time_created&#x27;: &#x27;2018-12-15T12:09:34.999000+00:00&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONED&#x27;, &#x27;provider_service_name&#x27;: None, &#x27;gateway_id&#x27;: None, &#x27;reference_comment&#x27;: None, &#x27;oracle_bgp_asn&#x27;: 31898, &#x27;customer_bgp_asn&#x27;: 5, &#x27;bgp_session_state&#x27;: &#x27;DOWN&#x27;, &#x27;provider_name&#x27;: None, &#x27;bgp_management&#x27;: &#x27;CUSTOMER_MANAGED&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxEXAMPLExxxxx&#x27;, &#x27;type&#x27;: &#x27;PUBLIC&#x27;, &#x27;id&#x27;: &#x27;ocid1.virtualcircuit.oc1..xxxxxEXAMPLExxxxx&#x27;}</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>bgp_management</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>BGP management option.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CUSTOMER_MANAGED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>bgp_session_state</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The state of the BGP session associated with the virtual circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UP</div>
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
                                            <div>The OCID of the compartment containing the Virtual Circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>cross_connect_mappings</b>
                    <div style="font-size: small; color: purple">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>An array of mappings, each containing properties for a cross-connect or cross-connect group that is associated with this virtual circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;oracle_bgp_peering_ip&#x27;: &#x27;10.0.0.19/31&#x27;, &#x27;bgp_md5_auth_key&#x27;: None, &#x27;vlan&#x27;: None, &#x27;cross_connect_or_cross_connect_group_id&#x27;: None, &#x27;customer_bgp_peering_ip&#x27;: &#x27;10.0.0.18/31&#x27;}]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>customer_bgp_asn</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The BGP ASN of the network at the other end of the BGP session from Oracle. If the session is between the customer&#x27;s edge router and Oracle, the value is the customer&#x27;s ASN. If the BGP session is between the provider&#x27;s edge router and Oracle, the value is the provider&#x27;s ASN.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">10</div>
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
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ansible-virtual-circuit</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>gateway_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The OCID of the customer&#x27;s dynamic routing gateway (DRG) that this virtual circuit uses. Applicable only to private virtual circuits.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.drg..xxxxxEXAMPLExxxxx</div>
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
                                            <div>Identifier of the Virtual Circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.virtualcircuit.oc1.iad.xxxxxEXAMPLExxxxx</div>
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
                                            <div>The current state of the Virtual Circuit.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>oracle_bgp_asn</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The Oracle BGP ASN.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">31898</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>port_speed_shape_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The port speed for this cross-connect.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">10 Gbps</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>provider_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name of the Provider.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Megaport</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>provider_service_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The OCID of the service offered by the provider (if the customer is connecting via a provider).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.providerservice.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>provider_service_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name of the Provider Service.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Service</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>provider_state</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The provider&#x27;s state in relation to this virtual circuit (if the customer is connecting via a provider). ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">INACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>public_prefixes</b>
                    <div style="font-size: small; color: purple">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection. Each prefix must be /31 or less specific.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;cidr_block&#x27;: &#x27;10.0.0.10/31&#x27;}]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>reference_comment</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Provider-supplied reference information about this virtual circuit (if the customer is connecting via a provider).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SAMPLE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>region</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The Oracle Cloud Infrastructure region where this virtual circuit is located.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">phx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>service_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Provider service type.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">COLOCATED</div>
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
                                            <div>Date and time when the Virtual Circuit was created, in the format defined by RFC3339</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-08-25 21:10:29.600000+00:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Whether the virtual circuit supports private or public peering.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PUBLIC</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_virtual_circuit.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
