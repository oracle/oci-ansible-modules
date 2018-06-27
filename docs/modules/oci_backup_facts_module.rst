.. _oci_backup_facts:


oci_backup_facts - Fetches details of one or more Database Backups
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of the Database Backups.



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
    <td>backup_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Database Backup whose details needs to be fetched.</div>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the compartment from which the details of the Database Backups should be fetched</div>
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
    <td>database_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Database whose Backups should be fetched.</div>
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

    
    #Fetch Database Backup for a Compartment
    - name: List all Database Backups in a Compartment
      oci_backup_facts:
          compartment_id: 'ocid1.compartment..xcds'
    #Fetch Database Backup for a Database
    - name: List all Database Backups of a Database
      oci_database_facts:
          database_id: 'ocid1.database..xcds'
    #Fetch a specific Database Backup
    - name: List a specific Database Backup
      oci_database_facts:
          backup_id: 'ocid1.backup..xcds'


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
    <td>backups</td>
    <td>
        <div>Attributes of the Fetched Database Backup.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'AVAILABLE', 'availability_domain': 'IwGV:US-ABC-AD-1', 'display_name': 'ansible-backup-one', 'time_started': '2018-02-23T06:37:58.669000+00:00', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'time_ended': '2018-02-23T13:50:57.211000+00:00', 'database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'lifecycle_details': 'The backup operation  run successfully.', 'type': 'FULL', 'id': 'ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx'}, {'lifecycle_state': 'AVAILABLE', 'availability_domain': 'IwGV:US-ABC-AD-1', 'display_name': 'ansible-backup-two', 'time_started': '2018-02-24T06:37:58.669000+00:00', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'time_ended': '2018-02-24T13:50:57.211000+00:00', 'database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'lifecycle_details': 'The backup operation  run successfully.', 'type': 'FULL', 'id': 'ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
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
            <div>The current state of the Database Backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ACTIVE</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The name of the Availability Domain that the backup is located in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>IwGV:US-ABC-AD-1</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>The user-friendly name for the Database Backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-backup</td>
        </tr>

        <tr>
        <td>time_started</td>
        <td>
            <div>The date and time the Database Backup starts.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2018-02-23 06:37:58.669000</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the DB System where the Database resides, whose backup has to be created.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>time_ended</td>
        <td>
            <div>The date and time the Database Backup was completed.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2018-02-23 13:50:57.211000</td>
        </tr>

        <tr>
        <td>database_id</td>
        <td>
            <div>The identifier of the Database whose backup has to be created.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>lifecycle_details</td>
        <td>
            <div>Additional information about the current lifecycle_state of the Database Backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>The backup operation cannot run successfully because the node is STOPPING or STOPPED</td>
        </tr>

        <tr>
        <td>type</td>
        <td>
            <div>The type of Database Backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>FULL</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Database Backup.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.backup.oc1.iad.xxxxxEXAMPLExxxxx</td>
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
