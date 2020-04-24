:source: cloud/oracle/oci_resource_type_facts.py

:orphan:

.. _oci_resource_type_facts_module:


oci_resource_type_facts -- Retrieves facts of types of resource that you can find with a search or query
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module allows the user to retrieve facts of all resource types or a specific resource type that you can find with a search or query.



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
                    <b>name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The name of the resource type. Required if you want details of a specific resource type. If <em>name</em> is unspecified, details of all resource types that are supported is returned.</div>
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

    
    - name: Get facts about all resource types that you can find with a search or query
      oci_resource_type_facts:

    - name: Get details of the Vcn resource type
      oci_resource_type_facts:
        name: "Vcn"




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <b>resource_types</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>On successful operation</td>
                <td>
                                            <div>A type of resource that you can find with a search or query.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;fields&#x27;: [{&#x27;fieldName&#x27;: &#x27;freeformTags&#x27;, &#x27;isArray&#x27;: True, &#x27;fieldType&#x27;: &#x27;OBJECT&#x27;, &#x27;objectProperties&#x27;: [{&#x27;fieldName&#x27;: &#x27;freeformTags.value&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;freeformTags.key&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}]}, {&#x27;fieldName&#x27;: &#x27;displayName&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;definedTags&#x27;, &#x27;isArray&#x27;: True, &#x27;fieldType&#x27;: &#x27;OBJECT&#x27;, &#x27;objectProperties&#x27;: [{&#x27;fieldName&#x27;: &#x27;definedTags.key&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;definedTags.namespace&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;definedTags.value&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}]}, {&#x27;fieldName&#x27;: &#x27;lifecycleState&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;compartmentId&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;IDENTIFIER&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;availabilityDomain&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;timeLastIndexed&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;DATETIME&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;timeCreated&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;DATETIME&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;identifier&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;IDENTIFIER&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;cidrBlock&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;dnsLabel&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}, {&#x27;fieldName&#x27;: &#x27;vcnDomainName&#x27;, &#x27;isArray&#x27;: False, &#x27;fieldType&#x27;: &#x27;STRING&#x27;, &#x27;objectProperties&#x27;: None}], &#x27;name&#x27;: &#x27;Vcn&#x27;}]</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>fields</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>List of all the fields and their value type that are indexed for querying.</div>
                                        <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>field_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The name of the field to use when constructing the query. Field names are present for all types except OBJECT.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>field_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The type of the field, which dictates what semantics and query constraints you can use when searching or querying.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>is_array</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Indicates this field is actually an array of the specified field type.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>object_properties</b>
                    <div style="font-size: small; color: purple">same as fields</div>
                                    </td>
                <td>if the field type is OBJECT</td>
                <td>
                                            <div>If the field type is OBJECT, then this property will provide all the individual properties on the object that can be queried.</div>
                                        <br/>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The unique name of the resource type, which matches the value returned as part of the ResourceSummary object.</div>
                                        <br/>
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

- Sivakumar Thyagarajan (@sivakumart)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_resource_type_facts.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
