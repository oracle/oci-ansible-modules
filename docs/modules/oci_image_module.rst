.. _oci_image:


oci_image - Create, import, update and delete OCI Compute images
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module allows the user to create an image, import an exported image, update an image and delete OCI Compute Images.



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
        <div>The OCID of the compartment containing the instance that needs to be used as the basis for the image. Required when an image needs to be created with <em>state=present</em>.</div>
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
    <td>defined_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
    </td>
    </tr>

    <tr>
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A user-friendly name to be associated with the image. This does not have to be unique, and can be changed later. An Oracle-provided image name cannot be used as the name for a custom image's name.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>force_create<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
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
    <td>image_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the image. Required while updating an image using <em>state=present</em>, and deleting an existing image using <em>state=absent</em>.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">image_source_details<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for creating an image through import. Either <code>instance_id</code> or <code>image_source_details</code> needs to be specified while creating an image using <em>state=present</em>.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object image_source_details</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>source_type<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The source type for the image. Use 'objectStorageTuple' to get the image from an object in Object Storage and specify <code>namespace</code>, <code>bucket</code>, and <code>object</code>. Use 'objectStorageUri' when specifying an Object Storage URL to get the image, and specify <code>source_uri</code>.</div>
        </td>
        </tr>

        <tr>
        <td>source_uri<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The Object Storage URL for the image. See Object Storage URLs at <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs'>https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs</a> and pre-authenticated requests at <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth'>https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth</a> for constructing URLs for image import/export. Required when creating an image using <em>state=present</em> and the <em>source_type=objectStorageUri</em> under <code>image_source_details</code>.</div>
        </td>
        </tr>

        <tr>
        <td>bucket_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The Object Storage bucket for the image. Required when creating an image using <em>state=present</em> and the <em>source_type=objectStorageTuple</em> under <code>image_source_details</code>.</div>
        </td>
        </tr>

        <tr>
        <td>object_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The Object Storage name for the image. Required when creating an image using <em>state=present</em> and the <em>source_type=objectStorageTuple</em> under <code>image_source_details</code>.</div>
        </td>
        </tr>

        <tr>
        <td>namespace_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The Object Storage namespace for the image. Required when creating an image using <em>state=present</em> and the <em>source_type=objectStorageTuple</em> under <code>image_source_details</code>.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the instance that needs to be used as the basis for the image. Either <code>instance_id</code> or <code>image_source_details</code> needs to be specified while creating an image using <em>state=present</em>.</div>
    </td>
    </tr>

    <tr>
    <td>key_by<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
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
        <div>The state of the image that must be asserted to. When <em>state=present</em>, and the image doesn't exist, the image is created with the specified details. When <em>state=absent</em>, the image is deleted.</div>
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

    
    - name: Create a new image from a specified instance
      oci_image:
        name: my_custom_image_1
        compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
        instance_id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....dszaitd3da"

    - name: Create a new image by importing an exported image, where the image is placed in a bucket in Object Storage
            Service
      oci_image:
            name: my_custom_image_2
            compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
            image_source_details:
                source_type: "objectStorageTuple"
                bucket: "my_bucket"
                namespace: "my_namespace"
                object: "image-to-import.qcow2"

    - name: Create a new image by importing an exported image, where the image is available through an Object Storage
            Service URL
      oci_image:
            name: my_custom_image_3
            compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
            image_source_details:
                source_type: "objectStorageUri"
                source_uri: "https://objectstorage.us-phoenix-1.oraclecloud.com/n/my_namespace/b/my_bucket/o/image-to-impor
                            t.qcow2"

    - name: Update an image's display name
      oci_image:
            id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
            name: my_new_image_name

    - name: Delete an image
      oci_image:
            id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
            state: "absent"


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
    <td>oci_image</td>
    <td>
        <div>Details of the image</div>
    </td>
    <td align=center>On success</td>
    <td align=center>dict</td>
    <td align=center>{'lifecycle_state': 'AVAILABLE', 'operating_system_version': '16.04', 'operating_system': 'Canonical Ubuntu', 'display_name': 'my-image-1', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....lwbvm62xq', 'base_image_id': 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....qcsa7klnoa', 'time_created': '2017-11-24T13:18:31.579000+00:00', 'create_image_allowed': True, 'id': 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx.....dgb3pmci2q'}</td>
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
