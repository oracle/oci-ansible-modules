.. _oci_bucket_facts:


oci_bucket_facts - Fetches details of a bucket or all available buckets within a namespace
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module retrieves details of a bucket or all the buckets available for specified namespace and compartment identifier.



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
        <div>Identifier of the compartment from which facts of constituent buckets needs to be fetched.                     Required to get details of all buckets in a specified namespace and compartment.</div>
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
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the bucket. Required to fetch details of a specific bucket.</div>
        </br><div style="font-size: small;">aliases: bucket</div>
    </td>
    </tr>

    <tr>
    <td>namespace_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the namespace from which facts of constituent buckets needs to be fetched.</div>
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

    
    #Note: These examples do not set authentication details.

    #Listing facts of all buckets in a given namespace and compartment

    - name: List bucket facts
      oci_bucket_facts:
        namespace_name: 'mynamespace'
        compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

    #Fetch facts of a specific bucket
    - name: Fetch a bucket
      oci_bucket_facts:
        namespace_name: 'mynamespace'
        name: 'Bucket1'


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
    <td>buckets</td>
    <td>
        <div>The specified bucket or a list of all available buckets in the specified namespace and compartment.</div>
    </td>
    <td align=center>on success</td>
    <td align=center>complex</td>
    <td align=center>[{'etag': '7d48fea5-ghfc', 'name': 'Bucket1', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'created_by': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx', 'namespace': 'mynamespace', 'time_created': '2017-10-07T16:20:33.933000+00:00'}, {'etag': '3f0158f2-68ea', 'name': 'Bucket2', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'created_by': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx', 'namespace': 'mynamespace', 'time_created': '2017-10-06T13:47:38.544000+00:00'}]</td>
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
        <td>name</td>
        <td>
            <div>The name of the bucket</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>my-new-bucket1</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The ID of the compartment in which the bucket is authorized</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>namespace</td>
        <td>
            <div>The namespace in which the bucket lives</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>mynamespace</td>
        </tr>

        <tr>
        <td>created_by</td>
        <td>
            <div>The OCID of the user who created the bucket.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.user.oc1..xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>etag</td>
        <td>
            <div>The entity tag for the bucket.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>7d48fea5-ghfc</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the bucket was created, as described in RFC 2616, section 14.29</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-10-07 16:20:33.933000</td>
        </tr>

        <tr>
        <td>public_access_type</td>
        <td>
            <div>The type of public access enabled on this bucket. A bucket is set to NoPublicAccess by                         default, which only allows an authenticated caller to access the bucket and its contents. When                         ObjectRead is enabled on the bucket, public access is allowed for the GetObject, HeadObject,                         and ListObjects operations.</div>
        </td>
        <td align=center>On retrieving a specific bucket</td>
        <td align=center>string</td>
        <td align=center>NoPublicAccess</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Arbitrary string keys and values for user-defined metadata.</div>
        </td>
        <td align=center>On retrieving a specific bucket</td>
        <td align=center>dict(str,str)</td>
        <td align=center>{'foo': 'bar'}</td>
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
