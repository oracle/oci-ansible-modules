.. _oci_bucket:


oci_bucket - Create,update and delete oci buckets
+++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Creates OCI bucket if not present.
* Update OCI bucket, if present.
* Delete OCI bucket, if present.



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
        <div>Identifier of the compartment in which the bucket is available or should be available. Mandatory for <em>state=present</em>. Not required for <em>state=absent</em></div>
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
    <td>force<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If <em>force='no'</em> and the bucket contains objects, bucket will not be deleted. To delete a bucket which has objects, <em>force='yes'</em> should be specified.</div>
    </td>
    </tr>

    <tr>
    <td>metadata<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Use defined metadata dict(str,str) for the bucket. Limit is 4KB.</div>
    </td>
    </tr>

    <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the bucket. Bucket name must be unique within a namespace. For naming conventions, refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingbuckets.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingbuckets.htm</a></div>
    </td>
    </tr>

    <tr>
    <td>namespace_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the namespace in which the bucket is available or should be available</div>
    </td>
    </tr>

    <tr>
    <td>public_access_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>NoPublicAccess</td>
    <td><ul><li>ObjectRead</li><li>NoPublicAccess</li></ul></td>
    <td>
        <div>The type of public access  of the bucket. By default, no public access is allowed on the bucket. If <em>public_access_type=ObjectRead</em>, user can perform read operation on the bucket.</div>
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
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Decides whether to create,update or delete bucket. For <em>state=present</em>, if the bucket does not exists, it gets created. If it exists, it gets updated. For <em>state=absent</em>, bucket gets deleted.</div>
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

    
    #Note: These examples do not set authentication details.

    #Bucket creation or update
    - name: Create or Update bucket
      oci_bucket:
        namespace_name: 'ansibletestspace'
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
        name: 'AnsibleTestBucket'
        public_access_type: 'NoPublicAccess'
        metadata:
            project: 'Test Project'
        state: 'present'

    #Delete bucket
    - name: Delete bucket with 'force' to delete the bucket
            along with all the containing objects
      oci_bucket:
        namespace_name: 'ansibletestspace'
        name: 'AnsibleTestBucket'
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
    <td>bucket</td>
    <td>
        <div>Attributes of the created/updated bucket. Applicable only for create and update.</div>
    </td>
    <td align=center>success</td>
    <td align=center>string</td>
    <td align=center>{'name': 'AnsibleTestBucket', 'compartment_id': 'ocid1....62xq', 'namespace': 'ansibletestspace', 'created_by': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx..qndq', 'etag': 'cb734ffe-da3a-48f4-....-161fd4604cf1', 'time_created': '2017-10-01T11:30:33.655000+00:00', 'public_access_type': 'ObjectRead', 'metadata': {}}</td>
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
