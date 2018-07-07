.. _oci_volume_facts:


oci_volume_facts - Retrieve facts of volumes in OCI Block Volume service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of a specified volume or all the volumes in a specified compartment and availability domain.



Requirements (on host that executes module)
-------------------------------------------

  * python >= 2.6
  * Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io



Options
-------

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>api_user<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_fingerprint<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_key_file<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
    </td>
    </tr>

    <tr>
    <td>api_user_key_pass_phrase<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
    </td>
    </tr>

    <tr>
    <td>availability_domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the Availability Domain.</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compartment. Required to get information of all the volumes in a specified compartment. This option is mutually exclusive with <em>volume_id</em>.</div>
    </td>
    </tr>

    <tr>
    <td>config_file_location<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
    </td>
    </tr>

    <tr>
    <td>config_profile_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>DEFAULT</td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
    </td>
    </tr>

    <tr>
    <td>lookup_all_attached_instances<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to fetch information of compute instances attached to this volume from all the compartments in the tenancy.Fetching this information requires traversing through all the compartments in the Tenancy and therefore can potentially take a long time. This option is only supported in experimental mode.
    When <em>lookup_all_attached_instances=False</em>, only attached compute instances belonging to this volume's compartment, is returned. This is useful when the volume is used within a single compartment. When <em>lookup_all_attached_instances=True</em>, all the compartments in the tenancy are searched to find out the compute instances that are attached to this volume. Fetching information about compute instances attached to this volume is an experimental feature (ie, this may or may not be supported in future releases). To use such experimental features, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.</div>
    </td>
    </tr>

    <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
    </td>
    </tr>

    <tr>
    <td>tenancy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
    </td>
    </tr>

    <tr>
    <td>volume_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the volume. Required to get information of a specific volume. This option is mutually exclusive with <em>compartment_id</em>.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get information of all the volumes for a specific availability domain & compartment_id
      oci_volume_facts:
        availability_domain: BnQb:PHX-AD-1
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

    - name: Get information of a volume
      oci_volume_facts:
        volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx


Return Values
-------------

Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

    <tr>
    <td>volumes</td>
    <td>
        <div>List of volume information</div>
    </td>
    <td align=center>On success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'availability_domain': 'IwGV:US-ASHBURN-AD-2', 'display_name': 'ansible_test_volume', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'attached_instance_information': {'lifecycle_state': 'ATTACHED', 'availability_domain': 'IwGV:US-ASHBURN-AD-2', 'display_name': 'volumeattachment20171204124856', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'chap_username': None, 'time_created': '2017-12-04T12:48:56.497000+00:00', 'id': 'ocid1.volumeattachment.oc1.iad.xxxxxEXAMPLExxxxx', 'instance_id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx', 'iqn': 'iqn.2015-12.com.oracleiaas:8ea342ff-4687-4038-b733-d20cb1025b48', 'ipv4': '169.254.2.7', 'volume_id': 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx', 'attachment_type': 'iscsi', 'port': 3260, 'chap_secret': None}, 'size_in_mbs': 51200, 'time_created': '2017-12-05T15:35:28.747000+00:00', 'source_details': {'type': 'volume', 'id': 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx'}, 'size_in_gbs': 50, 'is_hydrated': True, 'id': 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
    </tr>

    <tr>
    <td>contains:</td>
    <td colspan=4>
        <table border=1 cellpadding=2>

        <tr>
        <th class="head">name</th>
        <th class="head">description</th>
        <th class="head">returned</th>
        <th class="head">type</th>
        <th class="head">sample</th>
        </tr>

        <tr>
        <td>lifecycle_state</td>
        <td>
            <div>The current state of a volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>PROVISIONING</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain of the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>IwGV:US-ASHBURN-AD-2</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name of the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_test_volume</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>attached_instance_information</td>
        <td>
            <div>Information of instance currently attached to the block volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>size_in_mbs</td>
        <td>
            <div>The size of the volume in MBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>int</td>
        <td align=center>51200</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the volume was created. Format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2017-11-22 19:40:08.871000</td>
        </tr>

        <tr>
        <td>source_details</td>
        <td>
            <div>The volume source, either an existing volume in the same Availability Domain or a volume backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'type': 'volumeBackup', 'id': 'ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx'}</td>
        </tr>

        <tr>
        <td>size_in_gbs</td>
        <td>
            <div>The size of the volume in GBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>int</td>
        <td align=center>50</td>
        </tr>

        <tr>
        <td>is_hydrated</td>
        <td>
            <div>Specifies whether the cloned volume's data has finished copying from the source volume or backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>bool</td>
        <td align=center>False</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        </table>
    </td>
    </tr>

    </table>
    </br>
    </br>


Notes
-----

.. note::
    - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html


Author
~~~~~~

    * Rohit Chaware (@rohitChaware)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
