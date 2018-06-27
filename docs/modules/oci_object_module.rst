.. _oci_object:


oci_object - Manage objects in OCI Object Storage Service
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Create, read, update or delete an object in OCI. This module allows the user to store a file as an object in OCI or download an object from OCI to a local file.



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
    <td>bucket_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the bucket in which the object exists.</div>
        </br><div style="font-size: small;">aliases: bucket</div>
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
    <td>content_encoding<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The content encoding of the object to be uploaded.</div>
    </td>
    </tr>

    <tr>
    <td>content_language<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The content language of the object to be uploaded.</div>
    </td>
    </tr>

    <tr>
    <td>content_length<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The content length of the object body to be uploaded.</div>
    </td>
    </tr>

    <tr>
    <td>content_md5<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The base-64 encoded MD5 hash of the body to be uploaded.</div>
    </td>
    </tr>

    <tr>
    <td>content_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>application/octet-stream</td>
    <td></td>
    <td>
        <div>The content type of the object to be uploaded.</div>
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The destination file path when downloading an object. Use with <em>state=present</em> to download an object. This option is mutually exclusive with <em>src</em>.</div>
    </td>
    </tr>

    <tr>
    <td>force<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Force overwriting existing local file when downloading or existing remote object when uploading.</div>
        </br><div style="font-size: small;">aliases: overwrite</div>
    </td>
    </tr>

    <tr>
    <td>namespace_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the namespace in which the object exists.</div>
        </br><div style="font-size: small;">aliases: namespace</div>
    </td>
    </tr>

    <tr>
    <td>object_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the object. For naming convention, refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingobjects.htm#namerequirements'>https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingobjects.htm#namerequirements</a>.</div>
        </br><div style="font-size: small;">aliases: name, object</div>
    </td>
    </tr>

    <tr>
    <td>opc_client_request_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The client request ID for tracing.</div>
    </td>
    </tr>

    <tr>
    <td>opc_meta<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>User-defined metadata dict(str,str) for the object to be uploaded.</div>
        </br><div style="font-size: small;">aliases: metadata</div>
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
    <td>src<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The source file path when uploading an object. Use with <em>state=present</em> to upload an object. This option is mutually exclusive with <em>dest</em>.</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>The final state of the object after the task. Use <em>state=absent</em> with <em>object</em> to delete a specific object. Use <em>state=present</em> with <em>dest</em> to download an object. Use <em>state=present</em> with <em>src</em> to upload an object.</div>
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

    
    - name: Create/upload an object
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: mydata.txt
        src: /usr/local/myfile.txt
        opc_meta: {language: english}

    - name: Get/download an object to a file
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: key.txt
        dest: /usr/local/new_file.txt

    - name: Avoid overwriting an existing file when downloading an object. The task would fail if the local file pointed
            to by I(dest) already exists
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: key.txt
        dest: /usr/local/myfile.txt
        force: false

    - name: Delete an object
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: key.txt
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
    <td>object</td>
    <td>
        <div>OCI object details</div>
    </td>
    <td align=center>On successful operation</td>
    <td align=center>dict</td>
    <td align=center>{'Content-Length': '165661', 'opc-request-id': '79bcd894-8a9d-fbfe-3717-fd92d518d0a1', 'Access-Control-Expose-Headers': 'Access-Control-Allow-Credentials,Access-Control-Allow-Methods, Access-Control-Allow-Origin,Content-Length,Content-MD5,Content-Type,ETag,Last-Modified,opc-client-info, opc-meta-author,opc-meta-doc-genre,opc-request-id', 'opc-meta-author': 'RC', 'Content-MD5': '3zBENq6MBnedDrpl2+SttQ==', 'Last-Modified': 'Tue, 10 Oct 2017 13:57:20 GMT', 'Connection': 'keep-alive', 'ETag': '5B3287C054A51CB6E053824310AC257B', 'Access-Control-Allow-Credentials': 'true', 'Date': 'Tue, 10 Oct 2017 13:58:02 GMT', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST,PUT,GET,HEAD,DELETE,OPTIONS', 'Content-Type': 'image/png'}</td>
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
