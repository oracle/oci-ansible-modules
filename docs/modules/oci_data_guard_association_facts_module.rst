.. _oci_data_guard_association_facts:


oci_data_guard_association_facts - Fetches details of an OCI Data Guard Association
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* F
* e
* t
* c
* h
* e
* s
*  
* d
* e
* t
* a
* i
* l
* s
*  
* o
* f
*  
* a
* n
*  
* O
* C
* I
*  
* D
* a
* t
* a
*  
* G
* u
* a
* r
* d
*  
* A
* s
* s
* o
* c
* i
* a
* t
* i
* o
* n



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
    <td>data_guard_association_id:<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Data Guard Association whose details needs to be fetched.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>database_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the database whose Data Guard Association details needs to be fetched</div>
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

    
    # Note: These examples do not set authentication details.
    # List all Data Guard Association related to a database
    - name: List all Data Guard Association of a Database
      oci_data_guard_association_facts:
          database_id: 'ocid1.database..abuw'

    # List a specific Data Guard Association related to a database
    - name: List all Data Guard Association of a Database
      oci_data_guard_association_facts:
          database_id: 'ocid1.database..abuw'
          data_guard_association_id: 'ocid1.dgassociation.abuw'


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
    <td align=center>[{'peer_db_home_id': 'ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx', 'lifecycle_state': 'PROVISIONING', 'peer_data_guard_association_id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'peer_role': 'STANDBY', 'time_created': '2018-03-03T06:55:49.463000+00:00', 'id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'role': 'PRIMARY', 'peer_database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'transport_type': 'ASYNC', 'lifecycle_details': None, 'apply_rate': '15 KByte/s', 'apply_lag': '7 seconds', 'peer_db_system_id': 'ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx', 'protection_mode': 'MAXIMUM_PERFORMANCE'}, {'peer_db_home_id': 'ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx', 'lifecycle_state': 'PROVISIONING', 'peer_data_guard_association_id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'peer_role': 'STANDBY', 'time_created': '2018-03-03T06:55:49.463000+00:00', 'id': 'ocid1.dgassociation.oc1.iad.xxxxxEXAMPLExxxxx', 'database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'role': 'PRIMARY', 'peer_database_id': 'ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx', 'transport_type': 'ASYNC', 'lifecycle_details': None, 'apply_rate': '15 KByte/s', 'apply_lag': '7 seconds', 'peer_db_system_id': 'ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx', 'protection_mode': 'MAXIMUM_PERFORMANCE'}]</td>
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
