:source: cloud/oracle/oci_image_actions.py

:orphan:

.. _oci_image_actions_module:


oci_image_actions -- Perform actions on an Image resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Perform actions on an Image resource in Oracle Cloud Infrastructure
- For *action=export*, exports the specified image to the Oracle Cloud Infrastructure Object Storage service. You can use the Object Storage URL, or the namespace, bucket name, and object name when specifying the location to export to. For more information about exporting images, see `Image Import/Export <https://docs.cloud.oracle.com/Content/Compute/Tasks/imageimportexport.htm>`_. To perform an image export, you need write access to the Object Storage bucket for the image, see `Let Users Write Objects to Object Storage Buckets <https://docs.cloud.oracle.com/Content/Identity/Concepts/commonpolicies.htm#Let4>`_. See `Object Storage URLs <https://docs.cloud.oracle.com/Content/Compute/Tasks/imageimportexport.htm#URLs>`_ and `Using Pre-Authenticated Requests <https://docs.cloud.oracle.com/Content/Object/Tasks/usingpreauthenticatedrequests.htm>`_ for constructing URLs for image import/export.



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
                    <b>action</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>export</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The action to perform on the Image.</div>
                                                                                </td>
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
                    <b>bucket_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Object Storage bucket to export the image to.</div>
                                                    <div>Required when destination_type is &#x27;objectStorageTuple&#x27;</div>
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
                    <b>destination_type</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>objectStorageUri</li>
                                                                                                                                                                                                <li>objectStorageTuple</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>destination_uri</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Object Storage URL to export the image to. See <a href='https://docs.cloud.oracle.com/Content/Compute/Tasks/imageimportexport.htm#URLs'>Object Storage URLs</a> and <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingpreauthenticatedrequests.htm'>Using Pre-Authenticated Requests</a> for constructing URLs for image import/export.</div>
                                                    <div>Required when destination_type is &#x27;objectStorageUri&#x27;</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>image_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the image.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>namespace_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Object Storage namespace to export the image to.</div>
                                                    <div>Required when destination_type is &#x27;objectStorageTuple&#x27;</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>object_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Object Storage object name for the exported image.</div>
                                                    <div>Required when destination_type is &#x27;objectStorageTuple&#x27;</div>
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
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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

    
    - name: Perform action export on image
      oci_image_actions:
        object_name: exported-image.oci
        bucket_name: MyBucket
        namespace_name: MyNamespace
        destination_type: objectStorageTuple
        image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        action: export

    - name: Perform action export on image
      oci_image_actions:
        destination_uri: https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/exported-image.oci
        destination_type: objectStorageUri
        image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        action: export





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
                    <b>image</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Details of the Image resource acted upon by the current operation</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;launch_options&#x27;: {&#x27;is_pv_encryption_in_transit_enabled&#x27;: True, &#x27;firmware&#x27;: &#x27;BIOS&#x27;, &#x27;remote_data_volume_type&#x27;: &#x27;ISCSI&#x27;, &#x27;boot_volume_type&#x27;: &#x27;ISCSI&#x27;, &#x27;is_consistent_volume_naming_enabled&#x27;: True, &#x27;network_type&#x27;: &#x27;E1000&#x27;}, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;operating_system&#x27;: &#x27;Oracle Linux&#x27;, &#x27;create_image_allowed&#x27;: True, &#x27;size_in_mbs&#x27;: 47694, &#x27;launch_mode&#x27;: &#x27;NATIVE&#x27;, &#x27;base_image_id&#x27;: &#x27;ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;My custom Oracle Linux image&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;agent_features&#x27;: {&#x27;is_monitoring_supported&#x27;: True}, &#x27;operating_system_version&#x27;: &#x27;7.2&#x27;, &#x27;time_created&#x27;: &#x27;2016-08-25T21:10:29.600Z&#x27;}</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>agent_features</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div></div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>is_monitoring_supported</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Whether the agent running on the instance can gather performance metrics and monitor the instance.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>base_image_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The OCID of the image originally used to launch the instance.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.baseimage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>compartment_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The OCID of the compartment containing the instance you want to use as the basis for the image.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>create_image_allowed</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Whether instances launched with this image can be used to create new images. For example, you cannot create an image of an Oracle Database instance.</div>
                                                    <div>Example: `true`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>defined_tags</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                                    <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>display_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>A user-friendly name for the image. It does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                    <div>You cannot use an Oracle-provided image name as a custom image name.</div>
                                                    <div>Example: `My custom Oracle Linux image`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">My custom Oracle Linux image</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>freeform_tags</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                                    <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The OCID of the image.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>launch_mode</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NATIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>launch_options</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div></div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>boot_volume_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block Storage volumes on Oracle provided images. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data volumes on Oracle provided images. * `PARAVIRTUALIZED` - Paravirtualized disk.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>firmware</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Firmware used to boot VM.  Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the default for Oracle provided images.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BIOS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>is_consistent_volume_naming_enabled</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Whether to enable consistent volume naming feature. Defaults to false.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <div style="font-size: small; color: purple">boolean</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Whether to enable in-transit encryption for the boot volume&#x27;s paravirtualized attachment. The default value is false.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>network_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using virtio drivers.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">E1000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>remote_data_volume_type</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. This is the default for Boot Volumes and Remote Block Storage volumes on Oracle provided images. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for Local data volumes on Oracle provided images. * `PARAVIRTUALIZED` - Paravirtualized disk.</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>lifecycle_state</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div></div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>operating_system</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The image&#x27;s operating system.</div>
                                                    <div>Example: `Oracle Linux`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Oracle Linux</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>operating_system_version</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The image&#x27;s operating system version.</div>
                                                    <div>Example: `7.2`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">7.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>size_in_mbs</b>
                    <div style="font-size: small; color: purple">integer</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The boot volume size for an instance launched from this image, (1 MB = 1048576 bytes). Note this is not the same as the size of the image when it was exported or the actual size of the image.</div>
                                                    <div>Example: `47694`</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">47694</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>time_created</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>on success</td>
                <td>
                                                                        <div>The date and time the image was created, in the format defined by RFC3339.</div>
                                                    <div>Example: `2016-08-25T21:10:29.600Z`</div>
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

- Manoj Meda (@manojmeda)
- Mike Ross (@mross22)
- Nabeel Al-Saber (@nalsaber)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_image_actions.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
