.. _oci_vcn_facts:


oci_vcn_facts - Retrieve facts of Virtual Cloud Networks(VCNs)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of a specified virtual cloud network(VCN) or lists all the VCNs in the specified compartment.



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
        <div>The OCID of the compartment. <em>compartment_id</em> is required to get all the VCNs in the compartment.</div>
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
    <td>vcn_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the VCN. <em>vcn_id</em> is required to get a specific VCN's information.</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get all the VCNs in a compartment
      oci_vcn_facts:
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

    - name: Get a specific VCN
      oci_vcn_facts:
        vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx


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
    <td>vcns</td>
    <td>
        <div>List of VCN details</div>
    </td>
    <td align=center>always</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'dns_label': 'ansiblevcn', 'display_name': 'ansible_vcn', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'default_dhcp_options_id': 'ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx', 'time_created': '2017-11-13T20:22:40.626000+00:00', 'vcn_domain_name': 'ansiblevcn.oraclevcn.com', 'default_security_list_id': 'ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx', 'cidr_block': '10.0.0.0/16', 'id': 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx', 'default_route_table_id': 'ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx'}]</td>
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
            <div>Current state of the VCN.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>dns_label</td>
        <td>
            <div>A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS                         label to form a fully qualified domain name (FQDN) for each VNIC within this subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansiblevcn</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name of the VCN.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_vcn</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment containing the VCN.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>default_dhcp_options_id</td>
        <td>
            <div>The OCID for the VCN's default set of DHCP options.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the VCN was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-13 20:22:40.626000</td>
        </tr>

        <tr>
        <td>vcn_domain_name</td>
        <td>
            <div>The VCN's domain name, which consists of the VCN's DNS label, and the oraclevcn.com domain.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansiblevcn.oraclevcn.com</td>
        </tr>

        <tr>
        <td>default_security_list_id</td>
        <td>
            <div>The OCID for the VCN's default security list.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>cidr_block</td>
        <td>
            <div>The CIDR IP address block of the VCN.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>10.0.0.0/16</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>OCID of the VCN.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>default_route_table_id</td>
        <td>
            <div>The OCID for the VCN's default route table.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx</td>
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
