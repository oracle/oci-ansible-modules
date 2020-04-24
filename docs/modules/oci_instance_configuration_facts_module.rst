:source: cloud/oracle/oci_instance_configuration_facts.py

:orphan:

.. _oci_instance_configuration_facts_module:


oci_instance_configuration_facts -- Retrieve facts of instance configurations in OCI Compute Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module retrieves information of a specified instance configuration or all the instance configurations in a specified compartment.



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
                                                                        <div>The OCID of the compartment. Required to get information of all the instance configurations in a specified compartment.</div>
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
                    <b>instance_configuration_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the instance configuration. Required to get information of the specified instance configuration.</div>
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

    
    - name: Get information of all the instance configurations for a specific availability domain & compartment_id
      oci_instance_configuration_facts:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd

    - name: Get information of a instance configuration
      oci_instance_configuration_facts:
        instance_configuration_id: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...efgh




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
                    <b>instance_configurations</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>On success</td>
                <td>
                                            <div>List of instance configuration information</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;time-created&#x27;: &#x27;2018-11-07T04:16:20.454000+00:00&#x27;, &#x27;compartment-id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...mkwq&#x27;, &#x27;instance-details&#x27;: {&#x27;block-volumes&#x27;: None, &#x27;secondary-vnics&#x27;: None, &#x27;instance-type&#x27;: &#x27;compute&#x27;, &#x27;launch-details&#x27;: {&#x27;availability-domain&#x27;: None, &#x27;source-details&#x27;: {&#x27;image-id&#x27;: &#x27;ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx...ayda&#x27;, &#x27;source-type&#x27;: &#x27;image&#x27;}, &#x27;ipxe-script&#x27;: None, &#x27;compartment-id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...mkwq&#x27;, &#x27;create-vnic-details&#x27;: {&#x27;display-name&#x27;: &#x27;siva-test-3&#x27;, &#x27;private-ip&#x27;: None, &#x27;skip-source-dest-check&#x27;: False, &#x27;hostname-label&#x27;: None, &#x27;subnet-id&#x27;: None, &#x27;assign-public-ip&#x27;: True}, &#x27;extended-metadata&#x27;: None, &#x27;metadata&#x27;: {&#x27;user_data&#x27;: &#x27;dW5kZWZpbmVk&#x27;, &#x27;ssh_authorized_keys&#x27;: &#x27;ssh-rsa ...k8Id/ug/xxxxxEXAMPLExxxxx...RYzAEYT foo@bar&#x27;}, &#x27;display-name&#x27;: &#x27;siva-test-3&#x27;, &#x27;freeform-tags&#x27;: None, &#x27;defined-tags&#x27;: None, &#x27;shape&#x27;: &#x27;VM.Standard2.1&#x27;}}, &#x27;display-name&#x27;: &#x27;siva-test-conf-3&#x27;, &#x27;freeform-tags&#x27;: {}, &#x27;defined-tags&#x27;: {}, &#x27;deferred-fields&#x27;: [&#x27;instanceDetails.launchDetails.availabilityDomain&#x27;, &#x27;instanceDetails.launchDetails.createVnicDetails.subnetId&#x27;], &#x27;id&#x27;: &#x27;ocid1.instanceconfiguration.oc1.iad.xxxxxEXAMPLExxxxx...ejka&#x27;}]</div>
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
                                            <div>The OCID of the compartment containing the instance configuration.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>deferred_fields</b>
                    <div style="font-size: small; color: purple">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>List of deferred fields</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;instanceDetails.launchDetails.availabilityDomain&quot;, &quot;instanceDetails.launchDetails.createVnicDetails.subnetId&quot;]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>defined_tags</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;42&#x27;}}</div>
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
                                            <div>A user-friendly name for the instance configuration</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">backend-servers</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>freeform_tags</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
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
                                            <div>The OCID of the instance configuration.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>instance_details</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Details of the instance</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_created</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The date and time the instance configuration was created, in the format defined by RFC3339.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2018-11-07T04:16:20.454000+00:00</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_instance_configuration_facts.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
