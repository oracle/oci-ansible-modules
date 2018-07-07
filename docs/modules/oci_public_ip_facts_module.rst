.. _oci_public_ip_facts:


oci_public_ip_facts - Retrieve facts of public IPs
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves information of the specified public IP or all public IPs in the specified compartment.



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
        <div>The name of the Availability Domain. <em>availability_domain</em> is required to list all the ephemeral public IPs in the specified <em>compartment_id</em> and <em>availability_domain</em>.</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compartment. <em>compartment_id</em> is required to list all the public IPs in a compartment.</div>
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
    <td>ip_address<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The public IP address. Use <em>ip_address</em> to get the public IP based on the public IP address.</div>
    </td>
    </tr>

    <tr>
    <td>private_ip_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of the private IP that the public IP is assigned to. Use <em>private_ip_id</em> to retrieve information of a public IP assigned to it.</div>
    </td>
    </tr>

    <tr>
    <td>public_ip_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of the public IP. Use <em>public_ip_id</em> to retrieve a specific public IP's information using its OCID.</div>
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
    <td>scope<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>REGION</li><li>AVAILABILITY_DOMAIN</li></ul></td>
    <td>
        <div>Whether the public IP is regional or specific to a particular Availability Domain. Reserved public IPs have <em>scope=REGION</em>. Ephemeral public IPs have <em>scope=AVAILABILITY_DOMAIN</em>. <em>scope</em> is required to list all the public IPs in a compartment.</div>
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

    
    - name: Get all the reserved public IPs in a compartment
      oci_public_ip_facts:
        scope: REGION
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

    - name: Get all the ephemeral public IPs in a compartment and availability domain
      oci_public_ip_facts:
        scope: AVAILABILITY_DOMAIN
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        availability_domain: "BnQb:PHX-AD-1"

    - name: Get a specific public IP using its OCID
      oci_public_ip_facts:
        public_ip_id: ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx

    - name: Get a specific public IP using the OCID of the private IP to which it is assigned
      oci_public_ip_facts:
        private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx

    - name: Get a specific public IP using its public IP address
      oci_public_ip_facts:
        ip_address: 129.146.2.1


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
    <td>public_ips</td>
    <td>
        <div>List of public IP details</div>
    </td>
    <td align=center>always</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'availability_domain': None, 'display_name': 'ansible_public_ip', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'time_created': '2018-06-22T15:25:25.569000+00:00', 'lifetime': 'RESERVED', 'scope': 'REGION', 'private_ip_id': None, 'ip_address': '129.213.14.148', 'id': 'ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
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
            <div>The public IP's current state.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ASSIGNED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The public IP's Availability Domain. This property is set only for ephemeral public IPs (that is, when the scope of the public IP is set to AVAILABILITY_DOMAIN). The value is the Availability Domain of the assigned private IP.</div>
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
        <td align=center>ansible_public_ip</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment containing the public IP. For an ephemeral public IP, this is the same compartment as the private IP's. For a reserved public IP that is currently assigned, this can be a different compartment than the assigned private IP's.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
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
        <td align=center>2018-06-22 15:25:25.569000</td>
        </tr>

        <tr>
        <td>lifetime</td>
        <td>
            <div>Defines when the public IP is deleted and released back to Oracle's public IP pool.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>EPHEMERAL</td>
        </tr>

        <tr>
        <td>scope</td>
        <td>
            <div>Whether the public IP is regional or specific to a particular Availability Domain.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>REGION</td>
        </tr>

        <tr>
        <td>private_ip_id</td>
        <td>
            <div>The OCID of the private IP that the public IP is currently assigned to, or in the process of being assigned to.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>ip_address</td>
        <td>
            <div>The public IP address of the publicIp object.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>129.146.2.1</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The public IP's Oracle ID (OCID).</div>
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
