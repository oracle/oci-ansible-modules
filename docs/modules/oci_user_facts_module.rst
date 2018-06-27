.. _oci_user_facts:


oci_user_facts - Fetches details of all the OCI users of a tenancy and their group memberships
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of all the OCI users of a tenancy and the group memberships.



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
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the user id whose details should be fetched</div>
        </br><div style="font-size: small;">aliases: user_id</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    #Fetch users filtered by user id
    - name: List user filtered by user id
      oci_user_facts:
          user_id: 'ocid1.user.oc1..xxxxxEXAMPLExxxxx'

    #Fetch all existing users
    - name: List all existing users
      oci_user_facts:


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
    <td>users</td>
    <td>
        <div>Attributes of the existing users.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'name': 'ansible_user', 'compartment_id': 'ocidv1:tenancy:oc1:arz:1461274726633:aa', 'defined_tags': {'department': {'division': 'engineering'}}, 'freeform_tags': {'user_type': 'admin'}, 'time_created': '2017-11-04T14:45:27.358000+00:00', 'member_of_groups': [{'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'description': 'Group Two', 'compartment_id': 'ocidv1:tenancy:oc1:arz:146:aaa', 'defined_tags': {'product': {'type': 'server'}}, 'freeform_tags': {'group_name': 'designer'}, 'time_created': '2017-06-22T13:55:21.077000+00:00', 'id': 'ocid1.group.oc1..xxxxxEXAMPLExxxxx', 'name': 'group_two'}, {'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'description': 'Group One', 'compartment_id': 'ocidv1:tenancy:oc1:arz:145', 'defined_tags': {'product': {'type': 'server'}}, 'freeform_tags': {'group_name': 'documentation'}, 'time_created': '2016-12-20T20:29:12.093000+00:00', 'id': 'ocid1.group.oc1..xxxxxEXAMPLExxxxx', 'name': 'group_one'}], 'id': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx', 'description': 'Ansible User'}]</td>
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
            <div>The current state of the user</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ACTIVE</td>
        </tr>

        <tr>
        <td>inactive_status</td>
        <td>
            <div>The detailed status of INACTIVE life cycle state</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>description</td>
        <td>
            <div>The description assigned to the user</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>Ansible User</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the tenancy containing the user</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.tenancy.oc1.xzvf..oifds</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the user was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>member_of_groups</td>
        <td>
            <div>The details of the groups the user has memberships in</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>[{'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'description': 'Group Two', 'compartment_id': 'ocidv1:tenancy:oc1:arz:146:aaa', 'id': 'ocid1.group.oc1..xxxxxEXAMPLExxxxx', 'time_created': '2017-06-22T13:55:21.077000+00:00', 'name': 'group_two'}]</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the user</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.user.oc1.axdf</td>
        </tr>

        <tr>
        <td>name</td>
        <td>
            <div>Name assigned to the user during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_user</td>
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
