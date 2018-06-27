.. _oci_data_guard_association:


oci_data_guard_association - Create a Data Guard Association and, perform various Database role transitions of Databases associated with a Data Guard Association in OCI Database Cloud Service.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Create an OCI Data Guard Association
* Perform a switchover between Databases associated in a Data Guard Association
* Perform a failover on standby Database associated in a Data Guard Association
* Perform a reinstate on a disabled standby Database associated in a Data Guard Association
* Since all operations of this module takes a long time, it is recommended to set the ``wait`` to False. Use :ref:`oci_data_guard_association_facts <oci_data_guard_association_facts>` to check the status of the operation as a separate task.



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
    <td>creation_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>ExistingDbSystem</td>
    <td><ul><li>ExistingDbSystem</li></ul></td>
    <td>
        <div>Specifies where to create the associated database ExistingDbSystem is the only supported  value.</div>
    </td>
    </tr>

    <tr>
    <td>data_guard_association_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The identifier of the Data Guard Association. Mandatory for role transition of the Databases associated with a specified Data Guard Association.</div>
    </td>
    </tr>

    <tr>
    <td>database_admin_password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase,two lowercase, two numbers, and two special characters.</div>
    </td>
    </tr>

    <tr>
    <td>database_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Database to which the Data Guard should be Associated.</div>
    </td>
    </tr>

    <tr>
    <td>protection_mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>MAXIMUM_AVAILABILITY</li><li>MAXIMUM_PERFORMANCE</li><li>MAXIMUM_PROTECTION</li></ul></td>
    <td>
        <div>The protection mode to set up between the primary and standby databases. The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE. Allowed values are MAXIMUM_AVAILABILITY, MAXIMUM_PERFORMANCE, MAXIMUM_PROTECTION</div>
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
    <td><ul><li>present</li><li>switchover</li><li>failover</li><li>reinstate</li></ul></td>
    <td>
        <div>Create a new dataguard association or perform role transitions within associated databases of a dataguard association. For <em>state=present</em>, it gets created. For <em>state=switchover</em>, <em>state=failover</em>, <em>state=reinstate</em>, switchover, failover and reinstate on databases gets performed respectively.</div>
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
    <td>transport_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>SYNC</li><li>ASYNC</li><li>FASTSYNC</li></ul></td>
    <td>
        <div>The redo transport type to use for this Data Guard association. The only transport type currently supported by the Database Service is ASYNC. Allowed values are SYNC, ASYNC, FASTSYNC.</div>
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
    # Create Data Guard Association
    - name: Create Data Guard Association
      oci_data_guard_association:
          database_id: 'ocid1.database..abuw'
          creation_type: 'ExistingDbSystem'
          database_admin_password: 'pasword#_'
          protection_mode: 'MAXIMUM_PERFORMANCE'
          transport_type: 'ASYNC'
          peer_db_system_id: 'ocid1.dbsystem.xdvf'
          wait: False
          state: 'present'

    # Perform switchover action on Data Guard Association
    - name: Perform switchover operation to make the primary database to secondary
      oci_data_guard_association:
          database_id: 'ocid1.database.abuw'
          data_guard_association_id: 'ocid1.dgassociation.abuw'
          database_admin_password: 'pasword#_'
          state: 'switchover'

    # Perform failover action on Data Guard Association
    - name: Perform failover operation to make the standby database to primary
      oci_data_guard_association:
          database_id: 'ocid1.database.abuw'
          data_guard_association_id: 'ocid1.dgassociation.abuw'
          database_admin_password: 'pasword#_'
          state: 'failover'

    # Perform reinstate action on Data Guard Association
    - name: Perform reinstate operation to make the disable standby database to standby
      oci_data_guard_association:
          database_id: 'ocid1.database.abuw'
          data_guard_association_id: 'ocid1.dgassociation.abuw'
          database_admin_password: 'pasword#_'
          state: 'reinstate'


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
    <td>data_guard_association</td>
    <td>
        <div>Attributes of the Data Guard Association.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'peer_db_home_id': 'ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx', 'lifecycle_state': 'PROVISIONING', 'peer_data_guard_association_id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'peer_role': 'STANDBY', 'time_created': '2018-03-03T06:55:49.463000+00:00', 'id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'role': 'PRIMARY', 'peer_database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'transport_type': 'ASYNC', 'lifecycle_details': None, 'apply_rate': '15 KByte/s', 'apply_lag': '7 seconds', 'peer_db_system_id': 'ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx', 'protection_mode': 'MAXIMUM_PERFORMANCE'}</td>
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
            <div>The current state of the Data Guard Association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>peer_data_guard_association_id</td>
        <td>
            <div>Identifier of the peer database's Data Guard association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>peer_role</td>
        <td>
            <div>The role of the peer database in this Data Guard association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>STANDBY</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the Data Guard Association was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Data Guard Association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>database_id</td>
        <td>
            <div>Identifier of the  reporting Database.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>role</td>
        <td>
            <div>The role of the reporting database in this Data Guard Association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>PRIMARY</td>
        </tr>

        <tr>
        <td>peer_database_id</td>
        <td>
            <div>Identifier of the associated peer database.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>transport_type</td>
        <td>
            <div>The redo transport type used by this Data Guard Association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ASYNC</td>
        </tr>

        <tr>
        <td>lifecycle_details</td>
        <td>
            <div>Additional information about the current lifecycle_state, if available.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>Details of lifecycle state</td>
        </tr>

        <tr>
        <td>apply_rate</td>
        <td>
            <div>The rate at which redo logs are synced between the associated databases.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>17.00 KByte/s</td>
        </tr>

        <tr>
        <td>apply_lag</td>
        <td>
            <div>The lag time between updates to the primary database and application of the redo data on the standby database, as computed by the reporting database.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>9 seconds</td>
        </tr>

        <tr>
        <td>peer_db_system_id</td>
        <td>
            <div>Identifier of the  DB System containing the associated peer database.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>protection_mode</td>
        <td>
            <div>The protection mode of this Data Guard association.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>MAXIMUM_PERFORMANCE</td>
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
