.. _oci_db_node:


oci_db_node - Control the lifecycle of a DB Node in OCI's Database Cloud Service.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Stop/start a DB Node
* Reset a DB Node
* Soft-reset a DB Node
* All operations of this module returns after triggering the lifecycle operation. Use :ref:`oci_db_node_facts <oci_db_node_facts>` to check the status of the operation.



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
    <td>db_node_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the DB Node whose lifecycle state is to be controlled.</div>
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
    <td>yes</td>
    <td></td>
    <td><ul><li>stop</li><li>start</li><li>reset</li><li>softreset</li></ul></td>
    <td>
        <div>The state of the DB Node that must be asserted to. When <em>state=stop</em>, specified DB Node is powered off. When <em>state=start</em>, the specified DB Node is powered on. When <em>state=softreset</em>, an ACPI shutdown is initiated and specified DB Node is powered on. When <em>state=reset</em>, specified DB Node is powered off and then powered on. Note that <em>state=softreset</em> and <em>state=reset</em> states are not idempotent. Every time a play is executed with these <code>state</code> options, a shutdown and a power-on sequence is executed against the DB node.</div>
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
    # Assert that the database node is stopped
    - name: Stop a Database Node
      oci_db_node:
        db_node_id: "ocid1.dbnode.aaaa"
        state: 'stop'


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
    <td>db_node</td>
    <td>
        <div>Attributes of the Db Node.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'AVAILABLE', 'hostname': 'db-system-one', 'time_created': '2018-02-17T07:59:04.715000+00:00', 'vnic_id': 'ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx', 'db_system_id': 'ocid1.dbsystem.oc1.ia', 'backup_vnic_id': 'ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx', 'id': 'ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx', 'software_storage_size_in_gb': '1024'}</td>
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
            <div>The current state of the DB Node.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>AVAILABLE</td>
        </tr>

        <tr>
        <td>hostname</td>
        <td>
            <div>The host name for the DB Node.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-db-node</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the DB Node was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>vnic_id</td>
        <td>
            <div>The OCID of the VNIC of this DB Node</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>db_system_id</td>
        <td>
            <div>Identifier of the  DB System under which the DB Node exists.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>backup_vnic_id</td>
        <td>
            <div>The OCID of the backup VNIC of this DB Node</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the DB Node.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.dbnode.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>software_storage_size_in_gb</td>
        <td>
            <div>Storage size, in GBs, of the software volume that is allocated to the DB system. This is applicable only for VM-based DBs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>1024</td>
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
