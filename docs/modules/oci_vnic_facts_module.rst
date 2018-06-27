.. _oci_vnic_facts:


oci_vnic_facts - Retrieve details about a specific VNIC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves details about a specific VNIC.



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
    <td>vnic_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the VNIC. Required for retrieving information about a specific VNIC attachment.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get details of a specific VNIC
      oci_vnic_facts:
        id: 'ocid1.vnic.oc1..xxxxxEXAMPLExxxxx...vm62xq'


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
    <td>vnic</td>
    <td>
        <div>Information about a specific VNIC</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'my-vnic-1', 'hostname_label': 'myhostname-1', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...lwbvm62xq', 'subnet_id': 'ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...dusmpqpaoa', 'is_primary': True, 'time_created': '2017-11-26T16:23:29.932000+00:00', 'public_ip': None, 'skip_source_dest_check': False, 'private_ip': '10.0.0.10', 'mac_address': '00:00:17:00:6C:A2', 'id': 'ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...u7ybd56p6a'}]</td>
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
            <div>The current state of the VNIC.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain of the VNIC</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>Uocm:PHX-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the image. It does not have to be unique, and it's changeable.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>my-vnic1</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment containing the VNIC</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'</td>
        </tr>

        <tr>
        <td>hostname_label</td>
        <td>
            <div>The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>my-host-1</td>
        </tr>

        <tr>
        <td>subnet_id</td>
        <td>
            <div>The OCID of the subnet the VNIC is in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...pbf7yux45iddusmpqpaoa</td>
        </tr>

        <tr>
        <td>is_primary</td>
        <td>
            <div>Whether the VNIC is the primary VNIC</div>
        </td>
        <td align=center>always</td>
        <td align=center>boolean</td>
        <td align=center>True</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the image was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>public_ip</td>
        <td>
            <div>The public IP address of the VNIC, if one is assigned.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>10.1.2.3</td>
        </tr>

        <tr>
        <td>skip_source_dest_check</td>
        <td>
            <div>Whether the source/destination check is disabled on the VNIC. Defaults to false, which means the check is performed.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>True</td>
        </tr>

        <tr>
        <td>private_ip</td>
        <td>
            <div>The private IP address of the primary privateIp object on the VNIC. The address is within the CIDR of the VNIC's subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>10.0.3.3</td>
        </tr>

        <tr>
        <td>mac_address</td>
        <td>
            <div>The MAC address of the VNIC.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>00:00:17:B6:4D:DD</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the VNIC</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...asdadv3qca</td>
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
