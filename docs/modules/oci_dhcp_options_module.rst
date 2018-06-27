.. _oci_dhcp_options:


oci_dhcp_options - Create,update and delete OCI Dhcp Options
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Creates OCI Dhcp Options
* Update OCI Dhcp Options, if present, with a new display name
* Update OCI Dhcp Options, if present, by appending new options to existing options
* Update OCI Dhcp Options, if present, by purging existing options and replacing them with specified ones
* Delete OCI Dhcp Options, if present.



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
        <div>Identifier of the compartment under which this Dhcp Options would be created. Mandatory for create operation.Optional for delete and update. Mutually exclusive with dhcp_id.</div>
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
    <td>dhcp_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Dhcp Options. Mandatory for delete and update.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the Dhcp Options. A user friendly name. Does not have to be unique, and could be changed. If not specified, a default name would be provided.</div>
        </br><div style="font-size: small;">aliases: name</div>
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
    <td>key_by<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">options<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A set of DHCP options. Mandatory for create and update.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object options</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>type<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>DomainNameServer</li><li>SearchDomain</li></ul></td>
        <td>
        <div>The specific DHCP option.</div>
        </td>
        </tr>

        <tr>
        <td>search_domain_names<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>Applicable only for the <em>type='SearchDomain'</em>.A single search domain name according to RFC 952 and RFC 1123. Do not include this option with an empty list of search domain names, or with an empty string as the value for any search domain name.</div>
        </td>
        </tr>

        <tr>
        <td>custom_dns_servers<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Applicable only for the <em>type='DomainNameServer'</em> and <em>server_type='CustomDnsServer'</em>. Maximum three DNS server ips are allowed as part of this option.</div>
        </td>
        </tr>

        <tr>
        <td>server_type<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>VcnLocalPlusInternet</li><li>CustomDnsServer</li></ul></td>
        <td>
        <div>Applicable only for the <em>type='DomainNameServer'</em>.Describes the type of the server.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>purge_dhcp_options<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Purge existing Dhcp Options which are not present in the provided Dhcp Options. If <em>purge_dhcp_options=no</em>, provided options would be appended to existing options.</div>
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
        <div>Create,update or delete Dhcp Options. For <em>state=present</em>, if it does not exist, it gets created. If it exists, it gets updated.</div>
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
        <div>Identifier of the Virtual Cloud Network to which the Dhcp Options should be attached. Mandatory for create operation. Optional for delete and update. Mutually exclusive with dhcp_id.</div>
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

    
    #Note: These examples do not set authentication details.
    #Create/update Dhcp Options
    - name: Create dhcp options
      oci_dhcp_options:
        compartment_id: 'ocid1.compartment..xdsc'
        name: 'ansible_dhcp_options'
        vcn_id: 'ocid1.vcn..aaaa'
        options:
              - type: 'DomainNameServer'
                server_type: 'VcnLocalPlusInternet'
                custom_dns_servers: []
              - type: 'SearchDomain'
                search_domain_names: ['ansibletestvcn.oraclevcn.com']
        freeform_tags:
            region: 'east'
        defined_tags:
            features:
                capacity: 'medium'
        state: 'present'

    #Update Dhcp Options by appending new options
    - name: Update the display name of a Dhcp Options
      oci_dhcp_options:
        id: 'ocid1.dhcpoptions.oc1.aaa'
        purge_dhcp_options: 'no'
        options:
              - type: 'DomainNameServer'
                server_type: 'CustomDnsServer'
                custom_dns_servers: ['10.0.0.8']
              - type: 'SearchDomain'
                search_domain_names: ['ansibletestvcn.oraclevcn.com']
        state: 'present'

    #Update Dhcp Options by purging existing options
    - name: Update the display name of a Dhcp Options
      oci_dhcp_options:
        dhcp_id: 'ocid1.dhcpoptions.oc1.aaa'
        options:
              - type: 'DomainNameServer'
                server_type: 'CustomDnsServer'
                custom_dns_servers: ['10.0.0.8', '10.0.0.10', '10.0.0.12']
              - type: 'SearchDomain'
                search_domain_names: ['ansibletestvcn.oraclevcn.com']
        state: 'present'

    #Delete Dhcp Options
    - name: Delete Dhcp Options
      oci_dhcp_options:
        dhcp_id: 'ocid1.dhcpoptions..xdsc'
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
    <td>dhcp_options</td>
    <td>
        <div>Attributes of the created/updated Dhcp Options. For delete, deleted Dhcp Options description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'AVAILABLE', 'display_name': 'ansible_dhcp_options', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'vcn_id': 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx', 'defined_tags': {'features': {'capacity': 'medium'}}, 'freeform_tags': {'region': 'east'}, 'time_created': '2017-11-26T16:41:06.996000+00:00', 'id': 'ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx', 'options': [{'type': 'DomainNameServer', 'custom_dns_servers': [], 'server_type': 'VcnLocalPlusInternet'}, {'type': 'SearchDomain', 'search_domain_names': ['ansibletestvcn.oraclevcn.com']}, {'type': 'DomainNameServer', 'custom_dns_servers': ['10.0.0.8'], 'server_type': 'CustomDnsServer'}]}</td>
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
            <div>Identifier of the Virtual Cloud Network to which the Dhcp Options is attached.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vcn..ixcd</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name assigned to the Dhcp Options during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_dhcp_options</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the Dhcp Options</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>lifecycle_state</td>
        <td>
            <div>The current state of the Dhcp Options</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Dhcp Options</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dhcpoptions.oc1.axdf</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the Dhcp Options was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>options</td>
        <td>
            <div>A list of dhcp options.</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'type': 'DomainNameServer', 'custom_dns_servers': [], 'server_type': 'CustomDnsServer'}, {'type': 'SearchDomain', 'search_domain_names': ['myansiblevcn.oraclevcn.com']}]</td>
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
