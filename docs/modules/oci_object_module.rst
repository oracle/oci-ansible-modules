:source: cloud/oracle/oci_object.py

:orphan:

.. _oci_object_module:


oci_object -- Manage objects in OCI Object Storage Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create, read, update or delete an object in OCI. This module allows the user to store a file as an object in OCI or download an object from OCI to a local file.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <b>api_user</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_fingerprint</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_file</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_pass_phrase</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>auth_type</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible` playbooks within an OCI compute instance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>bucket_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the bucket in which the object exists.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: bucket</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_file_location</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_profile_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>content_encoding</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The content encoding of the object to be uploaded.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>content_language</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The content language of the object to be uploaded.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>content_length</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The content length of the object body to be uploaded.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>content_md5</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The base-64 encoded MD5 hash of the body to be uploaded.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>content_type</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"application/octet-stream"</div>
                                    </td>
                                                                <td>
                                                                        <div>The content type of the object to be uploaded.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>dest</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The destination file path when downloading an object. Use with <em>state=present</em> to download an object. This option is mutually exclusive with <em>src</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>force</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Force overwriting existing local file when downloading or existing remote object when uploading.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: overwrite</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>multipart_upload</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                                <td>
                                                                        <div>Use <em>multipart_upload=True</em> to use multipart upload feature to upload an large object. Disable multipart upload feature with <em>multipart_upload=False</em></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>namespace_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the namespace in which the object exists.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: namespace</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>object_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the object. For naming convention, refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingobjects.htm#namerequirements'>https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingobjects.htm#namerequirements</a>.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: name, object</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>opc_client_request_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The client request ID for tracing.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>opc_meta</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>User-defined metadata dict(str,str) for the object to be uploaded.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: metadata</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>parallel_uploads</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                                <td>
                                                                        <div>Use <em>parallel_uploads=True</em> to use parallel upload feature to upload an object. Disable parallel upload feature with <em>parallel_uploads=False</em>. Parallel upload feature works only when <em>multipart_upload=True</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>region</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>src</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The source file path when uploading an object. Use with <em>state=present</em> to upload an object. This option is mutually exclusive with <em>dest</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>state</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li>abort_multipart_upload</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The final state of the object after the task. Use <em>state=absent</em> with <em>object</em> to delete a specific object. Use <em>state=present</em> with <em>dest</em> to download an object. Use <em>state=present</em> with <em>src</em> to upload an object. Use <em>state=abort_multipart_upload</em> with <em>object</em> and <em>upload_id</em> to abort a specific multipart object upload.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tenancy</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>upload_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The upload ID for a multipart upload. Use with <em>state=abort_multipart_upload</em> to abort an in-progress multipart upload, and delete all the parts that have been uploaded.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
   - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create/upload an object (with multipart and parallel upload)
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: mydata.txt
        src: /usr/local/myfile.txt
        opc_meta: {language: english}

    - name: Create/upload an object without multipart and parallel upload
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: mydata.txt
        src: /usr/local/myfile.txt
        opc_meta: {language: english}
        multipart_upload: False
        parallel_uploads: False

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

    - name: Abort multipart upload
      oci_object:
        namespace: mynamespace
        bucket: mybucket
        object: mydata.txt
        upload_id: 951f4759-f910-50b4-udf99gf
        state: 'abort_multipart_upload'

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

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>object</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>On successful operation</td>
                <td>
                                            <div>OCI object details</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Date&#x27;: &#x27;Tue, 10 Oct 2017 13:58:02 GMT&#x27;, &#x27;Access-Control-Expose-Headers&#x27;: &#x27;Access-Control-Allow-Credentials,Access-Control-Allow-Methods, Access-Control-Allow-Origin,Content-Length,Content-MD5,Content-Type,ETag,Last-Modified,opc-client-info, opc-meta-author,opc-meta-doc-genre,opc-request-id&#x27;, &#x27;Access-Control-Allow-Methods&#x27;: &#x27;POST,PUT,GET,HEAD,DELETE,OPTIONS&#x27;, &#x27;Connection&#x27;: &#x27;keep-alive&#x27;, &#x27;Content-Length&#x27;: &#x27;165661&#x27;, &#x27;opc-meta-author&#x27;: &#x27;RC&#x27;, &#x27;Access-Control-Allow-Origin&#x27;: &#x27;*&#x27;, &#x27;Access-Control-Allow-Credentials&#x27;: &#x27;true&#x27;, &#x27;opc-request-id&#x27;: &#x27;79bcd894-8a9d-fbfe-3717-fd92d518d0a1&#x27;, &#x27;Last-Modified&#x27;: &#x27;Tue, 10 Oct 2017 13:57:20 GMT&#x27;, &#x27;Content-MD5&#x27;: &#x27;3zBENq6MBnedDrpl2+SttQ==&#x27;, &#x27;ETag&#x27;: &#x27;5B3287C054A51CB6E053824310AC257B&#x27;, &#x27;Content-Type&#x27;: &#x27;image/png&#x27;, &#x27;opc-multipart-md5&#x27;: &#x27;eoYNSi2Jkc2gMKksGkXOrQ&#x27;}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is :ref:`maintained by the Ansible Community <modules_support>`. *[community]*





Authors
~~~~~~~

- Rohit Chaware (@rohitChaware)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_object.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
