.. _oci_private_ip_facts:


oci_private_ip_facts - Retrieve facts of private IPs
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of a specified private IP or lists all the private IPs in a subnet.



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
    <td>DEFAULT</td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
    </td>
    </tr>

    <tr>
    <td>private_ip_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the private IP. <em>private_ip_id</em> is required to get a specific private IP's information.</div>
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
    <td>subnet_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the subnet. Required to list all the private IPs in a subnet.</div>
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

    
    - name: Get all the private IPs
      oci_private_ip_facts:
        subnet_id: ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx

    - name: Get a specific private IP
      oci_private_ip_facts:
        private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx


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
    <td>private_ips</td>
    <td>
        <div>List of private IP details</div>
    </td>
    <td align=center>always</td>
    <td align=center>complex</td>
    <td align=center>[{'availability_domain': 'IwGV:US-ASHBURN-AD-1', 'display_name': 'ansible_private_ip', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'hostname_label': 'db', 'subnet_id': 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'defined_tags': {}, 'freeform_tags': {}, 'time_created': '2018-03-28T18:37:56.190000+00:00', 'vnic_id': 'ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx', 'is_primary': False, 'ip_address': '10.0.0.114', 'id': 'ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
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
        <td>availability_domain</td>
        <td>
            <div>The private IP's Availability Domain.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>IwGV:US-ASHBURN-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_private_ip</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment containing the private IP.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>hostname_label</td>
        <td>
            <div>The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>webserver</td>
        </tr>

        <tr>
        <td>subnet_id</td>
        <td>
            <div>The OCID of the subnet the VNIC is in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>defined_tags</td>
        <td>
            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>{'Operations': {'CostCenter': '42'}}</td>
        </tr>

        <tr>
        <td>freeform_tags</td>
        <td>
            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>{'Department': 'Finance'}</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the private IP was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2018-03-28 18:37:56.190000</td>
        </tr>

        <tr>
        <td>vnic_id</td>
        <td>
            <div>The OCID of the VNIC the private IP is assigned to. The VNIC and private IP must be in the same subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>is_primary</td>
        <td>
            <div>Whether this private IP is the primary one on the VNIC. Primary private IPs are unassigned and deleted automatically when the VNIC is terminated.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>False</td>
        </tr>

        <tr>
        <td>ip_address</td>
        <td>
            <div>The private IP address of the privateIp object. The address is within the CIDR of the VNIC's subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>10.0.0.114</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The private IP's Oracle ID (OCID).</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx</td>
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
