.. _oci_volume_attachment_facts:


oci_volume_attachment_facts - Retrieve facts of volume attachments in OCI
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of a specified volume attachment or all the volume attachments in a specified compartment.



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
        <div>The OCID of the compartment. Required to get information of all the volume attachments in a specific compartment.</div>
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
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the instance. Use <em>instance_id</em> with <em>compartment_id</em> to get volume attachment information related to <em>instance_id</em>.</div>
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
    <td>volume_attachment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the volume attachment. Required to get information of a specific volume attachment.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>volume_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the volume. Use <em>volume_id</em> with <em>compartment_id</em> to get volume attachment information related to <em>volume_id</em>.</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get information of all volume attachments in a compartment
      oci_volume_attachment_facts:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

    - name: Get volume attachment information for a specified compartment & instance
      oci_volume_attachment_facts:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        instance_id: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx

    - name: Get volume attachment information for a specified compartment & block volume
      oci_volume_attachment_facts:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

    - name: Get information of a specific volume attachment
      oci_volume_attachment:
        volume_attachment_id: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx


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
    <td>volume_attachments</td>
    <td>
        <div>List of information about volume attachments</div>
    </td>
    <td align=center>On success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'ATTACHED', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'ansible_volume_attachment', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'chap_username': None, 'time_created': '2017-11-23T11:17:50.139000+00:00', 'id': 'ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx', 'instance_id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx', 'iqn': 'iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3', 'ipv4': '169.254.2.2', 'volume_id': 'ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx', 'attachment_type': 'iscsi', 'port': 3260, 'chap_secret': None}]</td>
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
            <div>The current state of the volume attachment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ATTACHED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain of an instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name. Does not have to be unique, and it cannot be changed.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>My volume attachment</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>chap_username</td>
        <td>
            <div>The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the volume was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the volume attachment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>instance_id</td>
        <td>
            <div>The OCID of the instance the volume is attached to.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>iqn</td>
        <td>
            <div>The target volume's iSCSI Qualified Name in the format defined by RFC 3720.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9</td>
        </tr>

        <tr>
        <td>ipv4</td>
        <td>
            <div>The volume's iSCSI IP address.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>169.254.0.2</td>
        </tr>

        <tr>
        <td>volume_id</td>
        <td>
            <div>The OCID of the volume.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>attachment_type</td>
        <td>
            <div>The type of volume attachment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>iscsi</td>
        </tr>

        <tr>
        <td>port</td>
        <td>
            <div>The volume's iSCSI port.</div>
        </td>
        <td align=center>always</td>
        <td align=center>int</td>
        <td align=center>3260</td>
        </tr>

        <tr>
        <td>chap_secret</td>
        <td>
            <div>The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP user name. (Also called the &quot;CHAP password&quot;.)</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>d6866c0d-298b-48ba-95af-309b4faux45e</td>
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
