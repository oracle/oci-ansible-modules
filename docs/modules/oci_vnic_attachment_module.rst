.. _oci_vnic_attachment:


oci_vnic_attachment - Create a secondary VNIC and attach it to a compute instance, detach or delete VNIC attachments from a compute instance.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module allows the user to create a secondary VNIC and attach it to a compute instance, detach a secondary VNIC attachment from a compute instance, and delete the secondary VNIC.



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
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A user-friendly name to be associated with the VNIC attachment. This does not have to be unique, and can be changed later.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the instance to which the secondary VNIC must be attached. Required when a secondary VNIC needs to be created and attached to an instance with <em>state=present</em>.</div>
    </td>
    </tr>

    <tr>
    <td>nic_index<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Specifies the physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). When a secondary VNIC is added to one of these instances, the NIC that the VNIC will use can be specified using <code>nic_index</code>. This option may be specified while creating a VNIC and attaching to an instance using <em>state=present</em>.</div>
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
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>The state of the VNIC attachment that must be asserted to. When <em>state=present</em>, and the VNIC attachment doesn't exist, the secondary VNIC is created with the specified details, and is attached to the specified compute instance. When <em>state=absent</em>, the secondary VNIC is detached from the compute instance and deleted.</div>
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
    <td rowspan="2">vnic<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for creating a new secondary VNIC. This option must be specified when a secondary VNIC needs to be created and associated with an instance using <em>state=present</em>.</div>
        </br><div style="font-size: small;">aliases: create_vnic_details</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object vnic</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>display_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A user-friendly name for the VNIC. Does not have to be unique.</div>
        </td>
        </tr>

        <tr>
        <td>hostname_label<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.</div>
        </td>
        </tr>

        <tr>
        <td>subnet_id<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the subnet to create the VNIC in.</div>
        </td>
        </tr>

        <tr>
        <td>defined_tags<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
        </td>
        </tr>

        <tr>
        <td>freeform_tags<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
        </td>
        </tr>

        <tr>
        <td>skip_source_dest_check<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Determines whether the source/destination check is disabled on the VNIC. Defaults to false, which means the check is performed.</div>
        </td>
        </tr>

        <tr>
        <td>private_ip<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The private IP to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's primary private IP address.</div>
        </td>
        </tr>

        <tr>
        <td>assign_public_ip<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Determines whether the secondary VNIC should be assigned a public IP address.  If not set and the VNIC is being created in a private subnet (that is, where <em>prohibitPublicIpOnVnic = true</em> in the Subnet), then no public IP address is assigned. If not set and the subnet is public <em>prohibitPublicIpOnVnic = false</em>, then a public IP address is assigned. If set to true and <em>prohibitPublicIpOnVnic = true</em>, an error is returned.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>vnic_attachment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the VNIC attachment. Required when a secondary VNIC needs to be detached from a compute instance and deleted using <em>state=absent</em>.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to wait for create or delete operation to complete.</div>
    </td>
    </tr>

    <tr>
    <td>wait_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1200</td>
    <td></td>
    <td>
        <div>Time, in seconds, to wait when <em>wait=yes</em>.</div>
    </td>
    </tr>

    <tr>
    <td>wait_until<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The lifecycle state to wait for the resource to transition into when <em>wait=yes</em>. By default, when <em>wait=yes</em>, we wait for the resource to get into ACTIVE/ATTACHED/AVAILABLE/PROVISIONED/ RUNNING applicable lifecycle state during create operation &amp; to get into DELETED/DETACHED/ TERMINATED lifecycle state during delete operation.</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Create a new secondary VNIC and attach it to the specified compute instance
      oci_vnic_attachment:
        name: sec-vnic1-to-instance1
        instance_id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....dszaitd3da"
        nicindex: 1
        vnic:
            hostname_label: "myinstance1_1"
            private_ip: "10.0.0.6"
            subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

    - name: Detach a secondary VNIC from an instance and delete the VNIC
      oci_vnic_attachment:
            id: "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...lxasdsadgdq"
            state: "absent"


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
    <td>vnic_attachment</td>
    <td>
        <div>Details of the VNIC attachment</div>
    </td>
    <td align=center>On success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'DETACHED', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'sec_vnic_1_for_my_instance', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...m62xq', 'subnet_id': 'ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...mpqpaoa', 'time_created': '2017-11-26T16:24:35.487000+00:00', 'instance_id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q', 'vnic_id': 'ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...mv2beqa', 'vlan_tag': 41, 'id': 'ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...3momq'}</td>
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
            <div>The current state of the VNIC attachment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>DETACHED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>Uocm:PHX-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name. Does not have to be unique.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>sec_vnic1_for_my_instance</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment the VNIC attachment is in, which is the same compartment the instance is in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...m62xq</td>
        </tr>

        <tr>
        <td>subnet_id</td>
        <td>
            <div>The OCID of the VNIC's subnet.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...mpqpaoa</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the VNIC attachment was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-26 16:24:35.487000</td>
        </tr>

        <tr>
        <td>instance_id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...qkwr6q</td>
        </tr>

        <tr>
        <td>vnic_id</td>
        <td>
            <div>The OCID of the VNIC. Available after the attachment process is complete.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...mv2beqa</td>
        </tr>

        <tr>
        <td>vlan_tag</td>
        <td>
            <div>The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process is complete.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>41</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the VNIC attachment.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx...3momq</td>
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
