.. _oci_customer_secret_key_facts:


oci_customer_secret_key_facts - Retrieve details of customer secret keys for a specified user
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves details of customer secret keys of a specified user. The returned object contains the customer secret key's OCID, but not the password itself. The actual password is returned only upon creation of a customer secret key using the :ref:`oci_customer_secret_key <oci_customer_secret_key>` module.



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
    <td>customer_secret_key_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the customer secret key. Required when facts about a specific customer secret key for the specified user needs to be obtained.</div>
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

    <tr>
    <td>user_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the user</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    - name: Get details of all the customer secret keys of the specified user
      oci_customer_secret_key_facts:
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"

    - name: Get details of a specific customer secret key of a user
      oci_customer_secret_key_facts:
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
        id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"


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
    <td>customer_secret_keys</td>
    <td>
        <div>Information about one or more customer secret keys in the specified user</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>{'customer_secret_keys': [{'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'display_name': 'My first customer secret key description', 'user_id': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx', 'time_expires': 'None', 'id': 'ocid1.credential.oc1..xxxxxEXAMPLExxxxx', 'time_created': '2018-01-08T04:44:17.784000+00:00'}]}</td>
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
            <div>The password's current state.</div>
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
        <td align=center>only when the I(lifecycle_state) is 'INACTIVE'</td>
        <td align=center>string</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>user_id</td>
        <td>
            <div>The OCID of the user the customer secret key belongs to.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.user.oc1..xxxxxEXAMPLExxxxx'</td>
        </tr>

        <tr>
        <td>description</td>
        <td>
            <div>The description that was assigned to the Customer secret key.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>My first customer secret key description'</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the Customer secret key:.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.credential.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time the Customer secret key object was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>expires_on</td>
        <td>
            <div>Date and time when this secret key will expire, in the format defined by RFC3339. Null if it never expires.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
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

    * Sivakumar Thyagarajan (@sivakumart)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
