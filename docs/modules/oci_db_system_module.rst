.. _oci_db_system:


oci_db_system - Launch,update and terminate a DB System in OCI Database Cloud Service.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Launch an OCI DB System
* Update an OCI DB System, if present, with a new display name
* Terminate an OCI DB System, if present.
* Since all operations of this module takes a long time, it is recommended to set the ``wait`` to False. Use :ref:`oci_db_system_facts <oci_db_system_facts>` to check the status of the operation as a separate task.



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
        <div>The Availability Domain where the DB System is located.</div>
    </td>
    </tr>

    <tr>
    <td>backup_subnet_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the backup network subnet the DB System is associated with. Applicable only to Exadata.</div>
    </td>
    </tr>

    <tr>
    <td>cluster_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Cluster name for Exadata and 2-node RAC DB Systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the compartment under which this DB System would be created. Mandatory for create operation.</div>
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
    <td>cpu_core_count<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The number of CPU cores to enable. For VM DB systems, the core count is inferred from the specific VM shape chosen, so this parameter is not used.</div>
    </td>
    </tr>

    <tr>
    <td>data_storage_percentage<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. This is not applicable for VM based DB systems.</div>
    </td>
    </tr>

    <tr>
    <td>data_storage_size_in_gbs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Size, in GBs, to which the currently attached storage needs to be scaled up to for VM based DB system. This must be greater than current storage size. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume. This option required only for update operation.</div>
    </td>
    </tr>

    <tr>
    <td>database_edition<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>STANDARD_EDITION</li><li>ENTERPRISE_EDITION</li><li>ENTERPRISE_EDITION_EXTREME_PERFORMANCE</li><li>ENTERPRISE_EDITION_HIGH_PERFORMANCE</li></ul></td>
    <td>
        <div>The Oracle Database Edition that applies to all the databases on the DB System. Exadata DB Systems and 2-node RAC DB Systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">db_home<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Details of the DB home to use for this database. DB home is a directory where Oracle database software is installed.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object db_home</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>db_version<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>A valid Oracle database version.</div>
        </td>
        </tr>

        <tr>
        <td>display_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The user-provided name of the database home.</div>
        </td>
        </tr>

        <tr>
        <td>database<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The details of the database to be created under the db home. Consists of the following options, ['admin_password' describes A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. required - true], ['character_set' describes the character set for the database. The default is AL32UTF8. required - false],['freeform_tags' describes Free-form tags for this database. Each tag is a simple key-value pair with no predefined name, type, or namespace. required - false], ['defined_tags' describes Defined tags for this database. Each key is predefined and scoped to a namespace. required - false] ['db_backup_config' consists of the option 'auto_backup_enabled' to determine whether to configures automatic backups of the databse. required - false], ['db_name' describes the name of the database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. required - true],['db_workload' describes database workload type with allowed values OLTP and DSS.required - false], ['ncharacter_set' describes National character set for the database.The default is AL16UTF16. Allowed values are AL16UTF16 or UTF8. required - false],['pdb_name' describes pluggable database name.It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are notpermitted. Pluggable database should not be same as database name. required - false]</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>db_system_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the existing DB System which required to be updated or terminated. Mandatory for terminate and update.</div>
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
    <td>disk_redundancy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>HIGH</li><li>NORMAL</li></ul></td>
    <td>
        <div>The type of redundancy configured for the DB System. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.</div>
    </td>
    </tr>

    <tr>
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The user-friendly name for the DB System. It does not have to be unique.</div>
    </td>
    </tr>

    <tr>
    <td>domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A domain name used for the DB System. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used. Hyphens (-) are not permitted.</div>
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
    <td>hostname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The host name for the DB System. The host name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).The maximum length of the combined hostname and domain is 63 characters. The hostname must be unique within the subnet. If it is not unique, the DB System will fail to provision.</div>
    </td>
    </tr>

    <tr>
    <td>initial_data_storage_size_in_gb<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Size, in GBs, of the initial data volume that will be created and attached to VM-shape based DB system. This storage can later be scaled up if needed. Note that the total storage size attached will be more than what is requested, to account for REDO/RECO space and software volume.</div>
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
    <td>license_model<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>LICENSE_INCLUDED</li><li>BRING_YOUR_OWN_LICENSE</li></ul></td>
    <td>
        <div>The Oracle license model that applies to all the databases on the DB System. The default is LICENSE_INCLUDED.</div>
    </td>
    </tr>

    <tr>
    <td>node_count<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Number of nodes to launch for a VM-shape based RAC DB system.</div>
    </td>
    </tr>

    <tr>
    <td>purge_ssh_public_keys<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td></td>
    <td>
        <div>Purge ssh public keys  from DB System which are not present in the provided ssh public keys. If <em>purge_ssh_public_keys=no</em>, provided ssh public keys would be appended to existing ssh public keys.</div>
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
    <td>shape<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The shape of the DB System. The shape determines resources allocated to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Launch,update or terminate DB System. For <em>state=present</em>, if it does not exist, it gets created. If it exists, it gets updated.</div>
    </td>
    </tr>

    <tr>
    <td>subnet_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the subnet the DB System is associated with.</div>
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
    <td rowspan="2">version<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>This attribute describes the patch version and what actions to perform with that on specified DB system. This is required only for update use case.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object version</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>action<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>APPLY</li><li>PRECHECK</li></ul></td>
        <td>
        <div>The action to perform on the patch.</div>
        </td>
        </tr>

        <tr>
        <td>patch_id<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the patch.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
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
    # Launch DB System
    - name: Create DB System
      oci_db_system:
        compartment_id: "ocid1.compartment.aaaa"
        availability_domain: "AD-2"
        cluster_name: "db-cluster"
        cpu_core_count: 2
        data_storage_percentage: 80
        database_edition: "STANDARD_EDITION"
        db_home:
          database:
            admin_password: 'BEstr0ng_#1'
            character_set: 'AL32UTF8'
            db_backup_config:
             auto_backup_enabled: False
            db_name: 'db15'
            db_workload: 'OLTP'
            ncharacter_set: 'AL16UTF16'
            pdb_name: 'db15'
            freeform_tags:
                deployment: 'production'
            defined_tags:
                target_users:
                    division: 'design'
          db_version: '12.2.0.1'
          display_name: ansible-db-{{random_suffix_1024}}
        disk_redundancy: "NORMAL"
        display_name: "ansibledb"
        hostname: "ansibledbsystem"
        initial_data_storage_size_in_gb: 4096
        license_model: "LICENSE_INCLUDED"
        node_count: 1
        shape: "BM.DenseIO1.36"
        ssh_public_keys: ["/tmp/id_rsa.pub"]
        subnet_id: "ocid1.subnet.aaaa"
        freeform_tags:
            deployment: 'production'
        defined_tags:
            target_users:
                division: 'documentation'
        wait: False
        state: 'present'

    # Perform a patch PRECHECK on the specified database system
    - name: PRECHECK a patch on the DB System
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
        version:
          patch_id: "ocid1.patch.aaaa"
          action: 'PRECHECK'
        state: 'present'

    # APPLY a patch on the specified database system
    - name: APPLY a patch on the DB System
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
        version:
          patch_id: "ocid1.patch.aaaa"
          action: 'APPLY'
        state: 'present'

    # Update a DB System's CPU core count
    - name: Update DB System CPU core count
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
        cpu_core_count: 4
        state: 'present'

    # Update DB System by purging SSH Public keys
    - name: Update DB System by purging SSH Public keys
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
        ssh_public_keys: ["/tmp/id_rsa_updated.pub"]
        purge_ssh_public_keys: True
        state: 'present'

    # Appending SSH public keys to a database system
    - name: Update DB System by appending SSH Public keys
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
        ssh_public_keys: ["/tmp/id_rsa_updated.pub"]
        purge_ssh_public_keys: False
        state: 'present'

    # Terminate DB System
    - name: Terminate DB System
      oci_db_system:
        db_system_id: "ocid1.dbsystem.aaaa"
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
    <td>db_system</td>
    <td>
        <div>Attributes of the launched/updated DB System. For delete, deleted DB System description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'domain': 'ansiblevcn955.ansiblevcn955.oraclevcn.com', 'backup_subnet_id': None, 'reco_storage_size_in_gb': None, 'database_edition': 'STANDARD_EDITION', 'time_created': '2018-02-10T19:21:44.171000+00:00', 'shape': 'BM.DenseIO1.36', 'disk_redundancy': 'NORMAL', 'last_patch_history_entry_id': None, 'license_model': 'LICENSE_INCLUDED', 'lifecycle_details': None, 'data_storage_size_in_gbs': None, 'id': 'ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx', 'listener_port': 1521, 'lifecycle_state': 'PROVISIONING', 'availability_domain': 'IwGV:US-ASHBURN-AD-2', 'display_name': 'ansible-db-system-955', 'data_storage_percentage': 80, 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'subnet_id': 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'defined_tags': {'target_users': {'division': 'accounts'}}, 'hostname': 'db-system-955', 'freeform_tags': {'deployment': 'production'}, 'ssh_public_keys': ['ssh-rsa AAA'], 'vip_ids': None, 'cluster_name': 'db-clus-955', 'scan_ip_ids': None, 'version': None, 'cpu_core_count': 2, 'scan_dns_record_id': None, 'node_count': None}</td>
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
