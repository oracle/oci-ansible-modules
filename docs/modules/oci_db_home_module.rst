.. _oci_db_home:


oci_db_home - Create,update and delete a DB Home in OCI Database Cloud Service.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Create an OCI DB Home
* Update an OCI DB Home, if present
* Delete an OCI DB Home, if present.
* Since all operations of this module takes a long time, it is recommended to set the ``wait`` to False. Use :ref:`oci_db_home_facts <oci_db_home_facts>` to check the status of the operation as a separate task.



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
    <td rowspan="2">database<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The details of the databse to be created under the db home. Mandatory for create operation.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object database</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>backup_id<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The backup OCID. This parameter only valid for <em>source=DB_BACKUP</em>.</div>
        </td>
        </tr>

        <tr>
        <td>ncharacter_set<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>National character set for the database.The default is AL16UTF16. Allowed values are AL16UTF16 or UTF8. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        <tr>
        <td>backup_tde_password<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The password to open the TDE wallet. This parameter only valid for <em>source=DB_BACKUP</em>.</div>
        </td>
        </tr>

        <tr>
        <td>pdb_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>pluggable database name.It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        <tr>
        <td>db_workload<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Database workload type with allowed values OLTP and DSS. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        <tr>
        <td>db_name<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The name of the database name. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        <tr>
        <td>admin_password<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase,two lowercase, two numbers, and two special characters. This parameter valid for <em>source=NONE</em> and <em>source=DB_BACKUP</em>.</div>
        </td>
        </tr>

        <tr>
        <td>db_backup_config<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Consists of the option 'auto_backup_enabled' to determine whether to configures automatic backups of the databse. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        <tr>
        <td>character_set<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The character set for the database. The default is AL32UTF8. This parameter only valid for <em>source=NONE</em>.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>db_home_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The identifier of the db home. Mandatory for update and delete.</div>
    </td>
    </tr>

    <tr>
    <td>db_system_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the  DB System under which the DB Home should exist. Mandatory for create.</div>
    </td>
    </tr>

    <tr>
    <td>db_version<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A valid Oracle database version. Mandatory for create.</div>
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
    <td>force_create<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
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
    <td rowspan="2">patch_details<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The patch version and what actions to perform with that, on specified DB Home. This is required only for the update use case.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object patch_details</b></caption>

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
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
    </td>
    </tr>

    <tr>
    <td>source<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>NONE</td>
    <td><ul><li>NONE</li><li>DB_BACKUP</li></ul></td>
    <td>
        <div>Source of database. <em>source=NONE</em> for creating a new database <em>source=DB_BACKUP</em> for creating a new database by restoring a backup.</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create,update or delete DB Home. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
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
    # Create DB Home from No Source
    - name: Create DB Home From No Source
      oci_db_home:
        db_system_id: "ocid1.dbsystem.aaaa"
        display_name: "db50"
        source: "NONE"
        database:
          admin_password: 'BEstr0ng_#1'
          character_set: 'AL32UTF8'
          db_backup_config:
            auto_backup_enabled: False
          db_name: 'dbone{{random_suffix_1024}}'
          db_workload: 'OLTP'
          ncharacter_set: 'AL16UTF16'
        db_version: "12.2.0.1"
        wait: False
        state: 'present'
    # Create DB Home from DB Backup
    - name: Create DB Home From DB Backup
      oci_db_home:
        db_system_id: "ocid1.dbsystem.aaaa"
        display_name: "db50"
        source: "DB_BACKUP"
        database:
           backup_id: 'ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx'
           backup_tde_password: 'BEstr0ng_#1'
           admin_password: 'BEstr0ng_#1'
        state: 'present'
    # Precheck a patch on DB Home
    - name: Precheck a patch on DB Home
      oci_db_home:
        db_home_id: "ocid1.dbhome.aaaa"
        patch_details:
           patch_id: "ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx"
           action: 'PRECHECK'
        state: 'present'
    # Apply a patch on DB Home
    - name: Apply a patch on DB Home
      oci_db_home:
        db_home_id: "ocid1.dbhome.aaaa"
        patch_details:
           patch_id: "ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx"
           action: 'APPLY'
        state: 'present'
    # Delete DB Home
      oci_db_home:
        db_home_id: "ocid1.dbhome.aaaa"
        state: 'absense'


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
    <td>db_home</td>
    <td>
        <div>Attributes of the created/updated DB Home. For delete, deleted DB Home description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'db_version': '12.2.0.1.1', 'display_name': 'ansible-db', 'compartment_id': 'ocid1.compartment.aaaa', 'lifecycle_state': 'AVAILABLE', 'last_patch_history_entry_id': 'ocid1.dbpatchhistory.aaaa', 'time_created': '2018-02-16T08:44:32.779000+00:00', 'db_system_id': 'ocid1.dbsystem.aaaa', 'id': 'ocid1.dbhome.aaaa'}</td>
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
        <td>db_version</td>
        <td>
            <div>Oracle database version.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>12.2.0.1.1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>The user-friendly name for the DB Home.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-db-home</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the DB Home</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
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
        <td>time_created</td>
        <td>
            <div>Date and time when the DB System was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
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
        <td>db_system_id</td>
        <td>
            <div>Identifier of the  DB System under which the DB Home should exists.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the DB Home.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx</td>
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
