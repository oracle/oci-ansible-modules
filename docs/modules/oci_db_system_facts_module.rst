.. _oci_db_system_facts:


oci_db_system_facts - Fetches details of the OCI DB System
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of the OCI DB System.



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
        <div>Identifier of the compartment in which this DB System exists</div>
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
    <td>db_system_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the DB System whose details needs to be fetched.</div>
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

    
    #Fetch DB System
    - name: List all DB System in a compartment
      oci_db_system_facts:
          compartment_id: 'ocid1.compartment..xcds'

    #Fetch specific DB System
    - name: List a specific DB System
      oci_db_system_facts:
          db_system_id: 'ocid1.dbsystem..xcds'


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
    <td>db_system</td>
    <td>
        <div>Attributes of the Fetched DB System.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'domain': 'ansiblevcn955.ansiblevcn955.oraclevcn.com', 'backup_subnet_id': None, 'reco_storage_size_in_gb': None, 'database_edition': 'STANDARD_EDITION', 'time_created': '2018-02-10T19:21:44.171000+00:00', 'shape': 'BM.DenseIO1.36', 'disk_redundancy': 'NORMAL', 'last_patch_history_entry_id': None, 'license_model': 'LICENSE_INCLUDED', 'lifecycle_details': None, 'data_storage_size_in_gbs': None, 'id': 'ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx', 'listener_port': 1521, 'lifecycle_state': 'PROVISIONING', 'availability_domain': 'IwGV:US-ASHBURN-AD-2', 'display_name': 'ansible-db-system-955', 'data_storage_percentage': 80, 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'subnet_id': 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'defined_tags': {'target_users': {'division': 'accounts'}}, 'hostname': 'db-system-955', 'freeform_tags': {'deployment': 'production'}, 'ssh_public_keys': ['ssh-rsa AAA'], 'vip_ids': None, 'cluster_name': 'db-clus-955', 'scan_ip_ids': None, 'version': None, 'cpu_core_count': 2, 'scan_dns_record_id': None, 'node_count': None}]</td>
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
        <td>domain</td>
        <td>
            <div>The domain name for the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansiblevcn955.ansiblevcn955.oraclevcn.com</td>
        </tr>

        <tr>
        <td>data_storage_percentage</td>
        <td>
            <div>The percentage assigned to DATA storage</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>80</td>
        </tr>

        <tr>
        <td>reco_storage_size_in_gb</td>
        <td>
            <div>RECO/REDO storage size, in GBs, that is currently allocated to the DB system. This is applicable only for VM-based DBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>1024</td>
        </tr>

        <tr>
        <td>database_edition</td>
        <td>
            <div>The Oracle Database Edition that applies to all the databases on the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>STANDARD_EDITION</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the DB System was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the DB System</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.DenseIO1.36</td>
        </tr>

        <tr>
        <td>disk_redundancy</td>
        <td>
            <div>The type of redundancy configured for the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>NORMAL</td>
        </tr>

        <tr>
        <td>last_patch_history_entry_id</td>
        <td>
            <div>The OCID of the last patch history. This is updated as soon as a patch operation is started.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.lastpatchhistory.aaaa</td>
        </tr>

        <tr>
        <td>license_model</td>
        <td>
            <div>The Oracle license model that applies to all the databases on the DB System</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>LICENSE_INCLUDED</td>
        </tr>

        <tr>
        <td>lifecycle_details</td>
        <td>
            <div>Additional information about the current lifecycle state.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>details</td>
        </tr>

        <tr>
        <td>data_storage_size_in_gbs</td>
        <td>
            <div>Data storage size, in GBs, that is currently available to the DB system. This is applicable only for VM-based DBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2048</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The identifier of the DB System</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dbsystem.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>listener_port</td>
        <td>
            <div>The port number configured for the listener on the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>1521</td>
        </tr>

        <tr>
        <td>lifecycle_state</td>
        <td>
            <div>The current state of the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain where the DB System is located.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>IwGV:US-ASHBURN-AD-2</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>The user-friendly name for the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-db-system</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the DB System</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>subnet_id</td>
        <td>
            <div>The OCID of the subnet the DB System is associated with.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.subnet.aaaa</td>
        </tr>

        <tr>
        <td>scan_dns_record_id</td>
        <td>
            <div>The OCID of the DNS record for the SCAN IP addresses that are associated with the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid.dnsrecord.aaaa</td>
        </tr>

        <tr>
        <td>hostname</td>
        <td>
            <div>The user-friendly name for the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>db-system</td>
        </tr>

        <tr>
        <td>ssh_public_keys</td>
        <td>
            <div>The public key portion of one or more key pairs used for SSH access to the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>['ssh-rsa 3NzaC1y']</td>
        </tr>

        <tr>
        <td>vip_ids</td>
        <td>
            <div>The OCID of the virtual IP (VIP) addresses associated with the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>['159.28.0.1']</td>
        </tr>

        <tr>
        <td>cluster_name</td>
        <td>
            <div>Cluster name for Exadata and 2-node RAC DB Systems</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>db-cluster</td>
        </tr>

        <tr>
        <td>scan_ip_ids</td>
        <td>
            <div>The OCID of the Single Client Access Name (SCAN) IP addresses associated with the DB System. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Clusterware directs the requests to the appropriate nodes in the cluster. For a single-node DB System, this list is empty.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.scanip.aaaa</td>
        </tr>

        <tr>
        <td>version</td>
        <td>
            <div>The version of the DB System.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>12.2.0.1</td>
        </tr>

        <tr>
        <td>cpu_core_count</td>
        <td>
            <div>The number of CPU cores to enable.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2</td>
        </tr>

        <tr>
        <td>node_count</td>
        <td>
            <div>Number of nodes in this DB system. For RAC DBs, this will be greater than 1.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2</td>
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
