.. _oci_volume_backup_facts:


oci_volume_backup_facts - Retrieve facts of volume backups in OCI Block Volume service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of a specified volume backup or all the volume backups in a compartment in OCI Block Volume service.



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
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compartment.</div>
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
    <td></td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
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
    <td>volume_backup_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the volume backup.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get information of all the volume backups in a compartment
      oci_volume_backup_facts:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

    - name: Get information of a volume backup
      oci_volume_backup_facts:
        id: ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx


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
    <td>volume_backups</td>
    <td>
        <div>List of volume backup information</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'size_in_gbs': 50, 'display_name': 'ansible_backup', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'size_in_mbs': 51200, 'time_created': '2017-12-22T15:40:53.219000+00:00', 'unique_size_in_gbs': 0, 'volume_id': 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx', 'unique_size_in_mbs': 1, 'time_request_received': '2017-12-22T15:40:48.111000+00:00', 'id': 'ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
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
            <div>The current state of a volume backup. Allowed values for this property are &quot;CREATING&quot;, &quot;AVAILABLE&quot;, &quot;TERMINATING&quot;, &quot;TERMINATED&quot;, &quot;FAULTY&quot;, &quot;REQUEST_RECEIVED&quot;, 'UNKNOWN_ENUM_VALUE'.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>size_in_gbs</td>
        <td>
            <div>The size of the volume, in GBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>50</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the volume backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>test_backup</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the volume backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>size_in_mbs</td>
        <td>
            <div>The size of the volume, in MBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>51200</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the volume backup was created. This is the time the actual point-in-time image of the volume data was taken. Format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-12-22 15:40:53.219000</td>
        </tr>

        <tr>
        <td>unique_size_in_gbs</td>
        <td>
            <div>The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space consumed on the volume and whether the backup is full or incremental.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>0</td>
        </tr>

        <tr>
        <td>volume_id</td>
        <td>
            <div>The OCID of the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>unique_size_in_mbs</td>
        <td>
            <div>The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space consumed on the volume and whether the backup is full or incremental.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>1</td>
        </tr>

        <tr>
        <td>time_request_received</td>
        <td>
            <div>The date and time the request to create the volume backup was received. Format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-12-22 15:40:48.111000</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the volume backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx</td>
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
