.. _oci_security_list:


oci_security_list - Create,update and delete OCI Security List
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Creates OCI Security List
* Update OCI Security List, if present, with a new display name
* Update OCI Security List, if present, with ingress/egress security rules
* Delete OCI Security List, if present.



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
        <div>Identifier of the compartment under which this Security List would be created. Mandatory for create operation.Optional for delete and update. Mutually exclusive with security_list_id.</div>
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
    <td>defined_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the Security List. A user friendly name. Does not have to be unique, and could be changed. If not specified, a default name would be provided.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">egress_security_rules<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Rules for allowing egress IP packets.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object egress_security_rules</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>icmp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for ICMP. Use to specify a particular ICMP type and code as defined in <a href='u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml''>u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml'</a>. If you specify ICMP as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 Destination Unreachable code 4 Fragmentation Needed and Do not Fragment was Set. If you need to specify multiple codes for a single type, create a separate security list rule for each.</div>
        </td>
        </tr>

        <tr>
        <td>udp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for UDP. Use to specify particular destination ports for UDP rules. If UDP specified as the protocol but omit this object, then all destination ports are allowed.</div>
        </td>
        </tr>

        <tr>
        <td>is_stateless<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td>
        <div>A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.</div>
        </td>
        </tr>

        <tr>
        <td>tcp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for TCP. Use to specify particular destination ports for TCP rules. If TCP specified as the protocol but omit this object, then all destination ports are allowed.</div>
        </td>
        </tr>

        <tr>
        <td>destination<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The destination CIDR block for the egress rule. This is the range of IP addresses that a packet originating from the instance can go to.</div>
        </td>
        </tr>

        <tr>
        <td>protocol<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>1</li><li>6</li><li>17</li></ul></td>
        <td>
        <div>Specify either all or an IPv4 protocol number as defined in <a href='u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml''>u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'</a> Options are supported only for ICMP 1, TCP 6, and UDP 17.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>force_create<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
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
    <td rowspan="2">ingress_security_rules<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Rules for allowing ingress IP packets.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object ingress_security_rules</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>source<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The source CIDR block for the ingress rule. This is the range of IP addresses that a packet coming into the instance can come from.</div>
        </td>
        </tr>

        <tr>
        <td>icmp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for ICMP. Use to specify a particular ICMP type and code as defined in <a href='u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml''>u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml'</a>. If you specify ICMP as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 Destination Unreachable code 4 Fragmentation Needed and Do not Fragment was Set. If you need to specify multiple codes for a single type, create a separate security list rule for each.</div>
        </td>
        </tr>

        <tr>
        <td>udp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for UDP. Use to specify particular destination ports for UDP rules. If UDP specified as the protocol but omit this object, then all destination ports are allowed.</div>
        </td>
        </tr>

        <tr>
        <td>is_stateless<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td>
        <div>A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if ingress traffic allows TCP destination port 80, there should be an egress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.</div>
        </td>
        </tr>

        <tr>
        <td>tcp_options<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Valid only for TCP. Use to specify particular destination ports for TCP rules. If TCP specified as the protocol but omit this object, then all destination ports are allowed.</div>
        </td>
        </tr>

        <tr>
        <td>protocol<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>1</li><li>6</li><li>17</li></ul></td>
        <td>
        <div>Specify either all or an IPv4 protocol number as defined in <a href='u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml''>u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'</a> Options are supported only for ICMP 1, TCP 6, and UDP 17.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>key_by<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
    </td>
    </tr>

    <tr>
    <td>purge_security_rules<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Purge security rules  from security list which are not present in the provided group security list. If <em>purge_security_rules=no</em>, provided security rules would be appended to existing security rules.</div>
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
    <td>security_list_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Security List. Mandatory for delete and update.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create,update or delete Security List. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
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
        <div>Identifier of the Virtual Cloud Network to which the Security List should be attached. Mandatory for create operation. Optional for delete and update. Mutually exclusive with security_list_id.</div>
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

    
    # Note: These examples do not set authentication details.
    # Create/update Security List
    - name: Create a security list with rules
      oci_security_list:
        name: 'ansible_sec_list'
        compartment_id: 'ocid.comprtment..aa'
        vcn_id: 'ocid1.vcn..aa'
        state: 'present'
        freeform_tags:
            region: 'east'
        defined_tags:
            features:
                capacity: 'medium'
        ingress_security_rules:
          - source: '0.0.0.0/0'
            is_stateless: False
            protocol: '6'
            tcp_options:
                destination_port_range:
                    min: '22'
                    max: '22'
          - source: '0.0.0.0/0'
            is_stateless: False
            protocol: '1'
            icmp_options:
                code: 4
                type: 3
        egress_security_rules:
            - destination: '0.0.0.0/0'
              protocol: 'all'

    - name: Update a security list by purging existing ingress rules
      oci_security_list:
        security_list_id: 'ocid1.securitylist.aa'
        ingress_security_rules:
            - source: '10.0.0.0/8'
              is_stateless: False
              protocol: '6'
              tcp_options:
                  destination_port_range:
                     min: '25'
                     max: '30'
        purge_security_rules: 'yes'
        state: 'present'

    # Delete a security list
    - name: Delete a security list
      oci_security_list:
        id: 'ocid1.securitylist.aa'
        state: 'absent'


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
    <td>security_list</td>
    <td>
        <div>Attributes of the created/updated Security List. For delete, deleted Security List description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'AVAILABLE', 'egress_security_rules': [{'icmp_options': None, 'udp_options': None, 'is_stateless': None, 'tcp_options': None, 'destination': '0.0.0.0/0', 'protocol': 'all'}], 'display_name': 'ansible_security_list_one', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'vcn_id': 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx', 'defined_tags': {'features': {'capacity': 'medium'}}, 'freeform_tags': {'region': 'east'}, 'time_created': '2017-11-24T05:33:44.779000+00:00', 'ingress_security_rules': [{'source': '0.0.0.0/0', 'icmp_options': None, 'udp_options': None, 'is_stateless': False, 'tcp_options': {'source_port_range': None, 'destination_port_range': {'max': 22, 'min': 22}}, 'protocol': '6'}, {'source': '0.0.0.0/0', 'icmp_options': {'code': 4, 'type': 3}, 'udp_options': None, 'is_stateless': False, 'tcp_options': None, 'protocol': '1'}, {'source': '10.0.0.0/16', 'icmp_options': {'code': None, 'type': 3}, 'udp_options': None, 'is_stateless': False, 'tcp_options': None, 'protocol': '1'}], 'id': 'ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx'}</td>
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
        <td>vcn_id</td>
        <td>
            <div>Identifier of the Virtual Cloud Network to which the Security List is attached.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vcn..ixcd</td>
        </tr>

        <tr>
        <td>egress_security_rules</td>
        <td>
            <div>Rules for allowing egress IP packets</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'icmp_options': None, 'udp_options': None, 'is_stateless': None, 'tcp_options': None, 'destination': '0.0.0.0/0', 'protocol': 'all'}]</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name assigned to the Security List during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_security_list</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>lifecycle_state</td>
        <td>
            <div>The current state of the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the Security List was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>ingress_security_rules</td>
        <td>
            <div>Rules for allowing ingress IP packets</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'source': '0.0.0.0/0', 'icmp_options': None, 'udp_options': None, 'is_stateless': None, 'tcp_options': {'source_port_range': None, 'destination_port_range': {'max': 22, 'min': 22}}, 'protocol': '6'}]</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Security List</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.securitylist.oc1.axdf</td>
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

    * Debayan Gupta(@debayan_gupta)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
