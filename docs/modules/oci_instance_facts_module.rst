.. _oci_instance_facts:


oci_instance_facts - Retrieve details about one or more Compute instances in OCI Compute Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves details about a specific Compute instance, or all Compute instances in a specified Compartment in a specified Availability Domain in OCI Compute Service.



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
        <div>The OCID of the compartment (either the tenancy or another compartment in the tenancy). Required for retrieving information about all instances in a Compartment/Tenancy.</div>
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
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the instance. Required for retrieving information about a specific instance.</div>
        </br><div style="font-size: small;">aliases: id</div>
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

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get details of all the compute instances of a specified compartment in a specified Availability Domain
      oci_instance_facts:
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
        availability_domain: "BnQb:PHX-AD-1"

    - name: Get details of a specific Compute instance
      oci_instance_facts:
        id:"ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"


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
    <td>instances</td>
    <td>
        <div>Information about one or more compute instances</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'TERMINATED', 'availability_domain': 'BnQb:PHX-AD-1', 'extended_metadata': {}, 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq', 'region': 'phx', 'time_created': '2017-11-20T04:52:54.541000+00:00', 'display_name': 'ansible-modname-968', 'image_id': 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....lnoa', 'shape': 'BM.Standard1.36', 'ipxe_script': None, 'volume_attachments': [{'lifecycle_state': 'ATTACHED', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'ansible_volume_attachment', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'chap_username': None, 'time_created': '2017-11-23T11:17:50.139000+00:00', 'id': 'ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx', 'instance_id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx', 'iqn': 'iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3', 'ipv4': '169.254.2.2', 'volume_id': 'ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx', 'attachment_type': 'iscsi', 'port': 3260, 'chap_secret': None}], 'boot_volume_attachment': {'boot_volume_id': 'ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx', 'availability_domain': 'IwGV:US-ASHBURN-AD-1', 'display_name': 'Remote boot attachment for instance', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'lifecycle_state': 'ATTACHED', 'time_created': '2018-01-15T07:23:10.838000+00:00', 'instance_id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx', 'id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx'}, 'id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx.....2siq', 'metadata': {'foo': 'bar', 'baz': 'quux'}}</td>
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
            <div>The current state of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>TERMINATED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>extended_metadata</td>
        <td>
            <div>Additional key-value pairs associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq</td>
        </tr>

        <tr>
        <td>region</td>
        <td>
            <div>The region that contains the Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>phx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the instance was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-instance-968</td>
        </tr>

        <tr>
        <td>image_id</td>
        <td>
            <div>The OCID of the image that the instance is based on</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.Standard1.36</td>
        </tr>

        <tr>
        <td>ipxe_script</td>
        <td>
            <div>A custom iPXE script that will run when the instance boots</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>volume_attachments</td>
        <td>
            <div>List of information about volume attachments</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>complex</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>boot_volume_attachment</td>
        <td>
            <div>Information of the boot volume attachment.</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Custom metadata that was associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
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

    * Sivakumar Thyagarajan (@sivakumart)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
