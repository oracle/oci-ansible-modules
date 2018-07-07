.. _oci_policy_facts:


oci_policy_facts - Retrieve details about a policy or policies attached to a compartment or tenancy in OCI Identity and Access Management service
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves a specific policy or all the policies attached to a specified compartment in OCI Identity and Access Management service.



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
        <div>The OCID of the compartment (remember that the tenancy is simply the root compartment). Required to list all the policies in a compartment.</div>
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
    <td>policy_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the policy. Required when retrieving a specific policy.</div>
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

    
    - name: Get all the policies attached to a compartment or tenancy
      oci_policy_facts:
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

    - name: Get details of a specific policy
      oci_policy_facts:
        id: ocid1.policy.oc1..xxxxxEXAMPLExxxxx


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
    <td>policies</td>
    <td>
        <div>Information of one or more policies</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'ACTIVE', 'inactive_status': None, 'statements': ['Allow group GroupAdmins to manage users in compartment Project-A'], 'name': 'mypolicy', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'time_created': '2017-11-01T14:59:51.728000+00:00', 'version_date': '2017-11-01T00:00:00+00:00', 'id': 'ocid1.policy.oc1..xxxxxEXAMPLExxxxx', 'description': 'GroupAdmins can add/remove users in Project-A compartment'}]</td>
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
            <div>The policy's current state.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ACTIVE</td>
        </tr>

        <tr>
        <td>inactive_status</td>
        <td>
            <div>The detailed status of INACTIVE lifecycleState.</div>
        </td>
        <td align=center>always</td>
        <td align=center>int</td>
        <td align=center>5</td>
        </tr>

        <tr>
        <td>statements</td>
        <td>
            <div>A list of one or more policy statements written in the policy language.</div>
        </td>
        <td align=center>always</td>
        <td align=center>list[string]</td>
        <td align=center>['Allow group GroupAdmins to manage users in compartment Project-A']</td>
        </tr>

        <tr>
        <td>name</td>
        <td>
            <div>The name assigned to the policy during creation.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>mypolicy</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment containing the policy (either the tenancy or another compartment).</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time the policy was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2017-11-01 14:59:51.728000</td>
        </tr>

        <tr>
        <td>version_date</td>
        <td>
            <div>The version of the policy. If null or set to an empty string, when a request comes in for                         authorization, the policy will be evaluated according to the current behavior of the services                         at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated                         according to the behavior of the services on that date.</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2017-11-01 00:00:00</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the policy.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.policy.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>description</td>
        <td>
            <div>The description assigned to the policy.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>GroupAdmins can add/remove users in Project-A compartment</td>
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

    * Rohit Chaware (@rohitChaware)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
