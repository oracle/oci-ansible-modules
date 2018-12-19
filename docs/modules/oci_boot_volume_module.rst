:source: cloud/oracle/oci_boot_volume.py

:orphan:

.. _oci_boot_volume_module:


oci_boot_volume - Manage boot volumes in OCI Block Volume service
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This module allows the user to perform create, delete & update operations on boot volumes in OCI Block Volume service.



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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <b>api_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>api_user_fingerprint</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>api_user_key_file</b>
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
                                                                <td colspan="2">
                    <b>availability_domain</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The availability domain of the boot volume. <em>availability_domain</em> is required to create a boot volume.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>backup_policy_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>If provided, specifies the ID of the boot volume backup policy to assign to the newly created boot volume. If omitted, no policy will be assigned.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>boot_volume_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the boot volume.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>compartment_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the compartment that contains the boot volume. <em>compartment_id</em> is required to create a boot volume.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>config_file_location</b>
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
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">DEFAULT</div>
                                    </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defined_tags</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>display_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>freeform_tags</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>key_by</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>kms_key_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the KMS key to be used as the master encryption key for the boot volume.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>lookup_attached_instance</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to fetch information of the compute instance attached to this boot volume from all the compartments in the tenancy.Fetching this information requires traversing through all the compartments in the  Tenancy and therefore can potentially take a long time. This option is only supported in experimental mode.
    When <em>lookup_all_attached_instances=False</em>, only an attached compute instance belonging to this boot volume's compartment, is returned. This is useful when the boot volume is used within a single compartment. When <em>lookup_all_attached_instances=True</em>, all the compartments in the tenancy are searched to find out the compute instance that is attached to this boot volume. Fetching information about compute instances attached to this boot volume is an experimental feature (ie, this may or may not be supported in future releases). To use such experimental features, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>region</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>size_in_gbs</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The size of the volume in GBs. <em>size_in_gbs</em> can be used to resize a boot volume. Ensure that the boot volume is detached, before resizing the boot volume.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>source_details</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the boot volume source details for a new boot volume. The volume source is either another boot volume in the same availability domain or a boot volume backup. <em>source_details</em> is required to create a boot volume.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>wait_for_copy</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to wait for the operation of copying from source boot volume or backup to complete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>type</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>bootVolumeBackup</li>
                                                                                                                                                                                                <li>bootVolume</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of boot volume source details.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the boot volume backup when <em>source_details.type=bootVolumeBackup</em> or the OCID of the boot volume in the same availability domain when <em>source_details.type=bootVolume</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>copy_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1800</div>
                                    </td>
                                                                <td>
                                            <div>Time, in seconds, to wait for the operation to complete when <em>wait_for_copy=yes</em>.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>state</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Update a boot volume with <em>state=present</em>. Delete a boot volume with <em>state=absent</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>tenancy</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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

    
    - name: Create a boot volume by cloning data from another boot volume in the same availability domain
      oci_boot_volume:
        name: sample_boot_volume
        source_details:
            id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
            type: 'bootVolume'
        availability_domain: IwGV:US-ASHBURN-AD-2
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        size_in_gbs: 50

    - name: Update name of a boot volume
      oci_boot_volume:
        name: ansible_boot_volume
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx

    - name: Resize a boot volume
      oci_boot_volume:
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        size_in_gbs: 100

    - name: Delete a boot volume
      oci_boot_volume:
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        state: 'absent'




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
                    <b>boot_volume</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>On successful update and delete operation</td>
                <td>
                                            <div>Information about the boot volume</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{'lifecycle_state': 'AVAILABLE', 'availability_domain': 'IwGV:US-ASHBURN-AD-1', 'display_name': 'demo-20171214-100_bastion_instance (Boot Volume)', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'attached_instance_information': {'boot_volume_id': 'ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx', 'availability_domain': 'IwGV:US-ASHBURN-AD-1', 'display_name': 'Remote boot attachment for instance', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'lifecycle_state': 'ATTACHED', 'time_created': '2018-01-14T19:02:49.085000+00:00', 'instance_id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx', 'id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx'}, 'size_in_mbs': 47694, 'time_created': '2018-01-14T19:02:49.042000+00:00', 'image_id': 'ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx', 'size_in_gbs': 46, 'id': 'ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx'}</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>lifecycle_state</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The current state of a boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>availability_domain</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The Availability Domain of the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">IwGV:US-ASHBURN-AD-2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>display_name</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name of the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ansible_boot_volume</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The OCID of the compartment that contains the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>attached_instance_information</b>
                    <br/><div style="font-size: small; color: red">dict</div>
                                    </td>
                <td>In experimental mode.</td>
                <td>
                                            <div>Information of the instance the boot volume is attached to.</div>
                                        <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>boot_volume_id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The OCID of the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>availability_domain</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The Availability Domain of an instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BnQb:PHX-AD-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>display_name</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it cannot be changed.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">My boot volume attachment</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The OCID of the compartment.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The current state of the boot volume attachment.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ATTACHED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_created</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The date and time the boot volume was created, in the format defined by RFC3339.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-08-25 21:10:29.600000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>instance_id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The OCID of the instance the boot volume is attached to.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when this boot volume is attached to a compute instance</td>
                <td>
                                            <div>The OCID of the boot volume attachment.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                    
                                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>size_in_mbs</b>
                    <br/><div style="font-size: small; color: red">int</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The size of the boot volume in MBs.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">51200</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>time_created</b>
                    <br/><div style="font-size: small; color: red">datetime</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The date and time the boot volume was created. Format defined by RFC3339.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2017-11-22 19:40:08.871000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>image_id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The image OCID used to create the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>size_in_gbs</b>
                    <br/><div style="font-size: small; color: red">int</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The size of the boot volume in GBs.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">50</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <b>id</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The OCID of the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx</div>
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

- Rohit Chaware (@rohitChaware)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_boot_volume.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
