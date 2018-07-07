.. _oci_user:


oci_user - Create,update and delete OCI user with specified group associations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Creates OCI user, if not present, without any group associations
* Creates OCI user, if not present, with ui password
* Creates OCI user, if not present, with specified group associations
* Update OCI user, if present, with a new description
* Update OCI user, if present, with new group(s) associations
* Update OCI user, if present, removing all group associations
* Update OCI user, if present, and reset the ui password of the user
* Unblock a blocked user
* Delete OCI user, if present.



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
    <td>blocked<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Change the state of an blocked user to unblocked.Only applied on existing blocked user. If the user is already unblocked, then <em>blocked=no</em> will not change the state. <em>blocked=yes</em> is not supported in this version.If the value is not specified explicitly, no action should be taken.</div>
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
    <td>create_or_reset_ui_password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Create UI password for an user who has no UI password or reset password of an user having UI password.</div>
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
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Description of the user. The value could be an empty string. If not provided explicitly while creating an user, the value defaults to an empty string. Not required for <em>state=absent</em></div>
    </td>
    </tr>

    <tr>
    <td>force<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <em>force='no'</em> and if the user is part of a group, user will not be deleted. To delete a user associated with group(s), use <em>state=yes</em>.</div>
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
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the user. Must be unique for a tenancy.</div>
    </td>
    </tr>

    <tr>
    <td>purge_group_memberships<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Purge groups from existing memberships which are not present in provided group memberships. If <em>purge_group_memberships=False</em>, provided groups would be appended to existing group memberships.</div>
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
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create,update or delete user. For <em>state=present</em>, if the user does not exists, it gets created. If exists, it gets updated.. For <em>state=absent</em>, user gets deleted.</div>
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
    <td>user_groups<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>List of groups to which the user should be associated  with.The specified groups must exist while running this task. If a specified group does not exist, this task would fail.If a user already exists, and their current group associations are different from the specified group associations, the task would change the user to ensure that the group associations of the user reflect the specified group associations.</div>
    </td>
    </tr>

    <tr>
    <td>user_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the User. Mandatory for delete and update.</div>
        </br><div style="font-size: small;">aliases: id</div>
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

    # User creation or update
    - name: Create User with ui password and  group memberships
      oci_user:
          name: 'ansible_user'
          description: 'Ansible  User'
          user_groups: ['ansible_group_A']
          freeform_tags:
                usert_type: 'admin'
          defined_tags:
              department:
                  division: 'engineering'
          create_or_reset_ui_password: True
          state: 'present'

    - name: Create user without group memberships
      oci_user:
          name: 'ansible_user'
          description: 'Ansible  User'
          create_or_reset_ui_password: True
          state: 'present'

    - name: Reset ui password of an existing user
      oci_user:
          id: 'ocid1.user..abuwd'
          create_or_reset_ui_password: True
          state: 'present'

    - name: Unblock User
      oci_user:
          id: 'ocid1.user..abuwd'
          blocked: 'no'
          state: 'present'
      register: result

    - name: Update user with removing all group memberships
      oci_user:
          id: 'ocid1.user..abuwd'
          description: 'Ansible  User'
          user_groups: []
          state: 'present'

    - name: Update user by replacing group memberships, after this
            operation user would become member of ansible_group_B
      oci_user:
          user_id: "ocid1.user..abuwd"
          description: 'Ansible User'
          purge_group_memberships: True
          user_groups: ['ansible_group_B']
          create_or_reset_ui_password: True
          state: 'present'


    # Delete group
    - name: Delete user with no force
      oci_user:
          id: 'ocid1.user..abuwd'
          state: 'absent'

    - name: Delete user with  force
      oci_user:
          user_id: 'ocid1.user..abuwd'
          force: 'yes'
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
    <td>user</td>
    <td>
        <div>Attributes of the created/updated user. For delete, deleted user description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'ACTIVE', 'inactive_status': 'None', 'description': 'Ansible User', 'compartment_id': 'ocidv1:tenancy:oc1:arz:1461274726633:aa', 'defined_tags': {'department': {'division': 'engineering'}}, 'freeform_tags': {'user_type': 'admin'}, 'time_created': '2017-11-04T14:45:27.358000+00:00', 'password': 'PJ+p&gt;u1&amp;u', 'id': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx', 'name': 'ansible_user'}</td>
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
        <td>password</td>
        <td>
            <div>The ui password of the user</div>
        </td>
        <td align=center>when I(create_or_reset_ui_password=True) and a new user created and when I(create_or_reset_ui_password=True) and new user created or an existing user is updated</td>
        <td align=center>string</td>
        <td align=center>_09erf4</td>
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
