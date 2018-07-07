.. _oci_instance:


oci_instance - Launch, terminate and control the lifecycle of OCI Compute instances
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* This module allows the user to launch/create, terminate and perform other power actions on OCI Compute Service instances. An instance represents a compute host. The image used to launch the instance determines its operating system and other software. The shape specified during the launch process determines the number of CPUs and memory allocated to the instance. For more information, see Overview of the Compute Service at https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm. In experimental mode, this module also allows attaching/detaching volumes and boot volumes to an instance.



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
    <td>availability_domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Availability Domain of the instance. Required when creating a compute instance with <em>state=present</em>.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">boot_volume_details<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for attaching/detaching a boot volume to/from an instance. <em>boot_volume_details</em> is mutually exclusive with <em>image_id</em>. This option is only supported in experimental mode. To use an experimental feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object boot_volume_details</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>attachment_state<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td>
        <div>Attach a boot volume to the instance <em>instance_id</em> with <em>attachment_state=present</em>. Detach a boot volume from the instance <em>instance_id</em> with <em>attachment_state=absent</em>.</div>
        </td>
        </tr>

        <tr>
        <td>boot_volume_id<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the boot volume.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compartment. Required when <em>state=present</em>.</div>
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
    <td>count_tag<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Used with <em>exact_count</em> to determine how many compute instances matching the specific tag criteria <code>count_tag</code> must be running. Only <em>defined_tags</em> associated with an instance are considered for matching against <code>count_tag</code>.</div>
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
        <div>A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. If a <code>display_name</code> is specified, and if <em>exact_count</em> is specified, the display name would be suffixed with an auto-incrementing integer.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>exact_count<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Indicates how many instances that match the <em>count_tag</em> option should be running. This must be used with <em>state=present</em> and a valid <em>count_tag</em>. If the number of compute instances that match <code>count_tag</code> is lesser than <code>exact_count</code>, additional compute instances would be provisioned to match the desired <code>exact_count</code>. If the number of matching compute instances is larger than <code>exact_count</code>, compute instances would be terminated to match the desired <code>exact_count</code>. The latest launch instance(s) from the set of instances that match <code>count_tag</code> are picked for termination. Private IP assignments through <em>private_ip</em>, and specification of <em>hostname_label</em> and <em>volume_details</em> and <em>boot_volume_details</em> is not supported with <em>exact_count</em> and <em>count_tag</em>. By default, an auto-incremented integer value is suffixed to the value of <em>display_name</em> and assigned as the display_name of a newly provisioned instance. For example, if <em>display_name</em> is 'my_web_server', new compute instances would be called 'my_web_server_0', 'my_web_server_1' and so on. To control the generated display name in a fine-grained manner, use &quot;printf&quot; style format in <em>display_name</em> such as 'my_%d_web_server'.</div>
    </td>
    </tr>

    <tr>
    <td>extended_metadata<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Additional metadata key/value pairs that you provide. They serve a similar purpose and functionality from fields in the <em>metadata</em> object. They are distinguished from <em>metadata</em> fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only). If you don't need nested metadata values, it is strongly advised to avoid using this object and use the Metadata object instead.</div>
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
        <div>The OCID of the image used to boot the instance. Required to launch an instance using an image with <em>state=present</em>. <em>image_id</em> is mutually exclusive with <em>boot_volume_details</em>. This can also be provided through <em>source_details</em>.</div>
    </td>
    </tr>

    <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The OCID of the compute instance. Required for updating an existing compute instance when <em>state=present</em>, for performing power actions (such as start, stop, softreset or reset) on an instance, and for terminating an instance <em>state=absent</em>.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>ipxe_script<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>custom iPXE script that will run when the instance boots.</div>
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
    <td>metadata<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A hash/dictionary of custom key/value pairs that are associated with the instance. This option is also used to provide information to cloud-init and specifying &quot;ssh_authorized_keys&quot; for the default user of the instance. This hash is specified as '{&quot;key&quot;:&quot;value&quot;}' and '{&quot;key&quot;:&quot;value&quot;,&quot;key&quot;:&quot;value&quot;}'.</div>
    </td>
    </tr>

    <tr>
    <td>preserve_boot_volume<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to preserve the boot volume when terminating an instance with <em>state=absent</em>.</div>
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
    <td>shape<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The shape of the instance. Required when creating a compute instance with <em>state=present</em>.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">source_details<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object source_details</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>boot_volume_id<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the boot volume used to boot the instance. Required if <em>source_type</em> is &quot;bootVolume&quot;.</div>
        </td>
        </tr>

        <tr>
        <td>image_id<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the image used to boot the instance. Required if <em>source_type</em> is &quot;image&quot;.</div>
        </td>
        </tr>

        <tr>
        <td>source_type<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>image</li><li>bootVolume</li></ul></td>
        <td>
        <div>The source type for the instance. Use image when specifying the image OCID. Use bootVolume when specifying the boot volume OCID.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li><li>running</li><li>reset</li><li>softreset</li><li>stopped</li></ul></td>
    <td>
        <div>The state of the instance that must be asserted to. When <em>state=present</em>, and the compute instance doesn't exist, the instance is launched/created with the specified details. When <em>state=absent</em>, the compute instance is terminated. When <em>state=stopped</em>, the compute instance is powered off. When <em>state=running</em>, the compute instance is powered on. When <em>state=softreset</em>, an ACPI shutdown is initiated and the compute instance is powered on. When <em>state=reset</em>, the compute instance is powered off and then powered on. Note that <em>state=softreset</em> and <em>state=reset</em> states are not idempotent. Every time a play is executed with these <code>state</code> options, a shutdown and a power on sequence is executed against the instance.</div>
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
    <td rowspan="2">vnic<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for the primary VNIC that is automatically created and attached when the instance is launched. Required when creating a compute instance with <em>state=present</em>.</div>
        </br><div style="font-size: small;">aliases: create_vnic_details</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object vnic</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>skip_source_dest_check<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Determines whether the source/destination check is disabled on the VNIC. Defaults to false, which means the check is performed.</div>
        </td>
        </tr>

        <tr>
        <td>name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A user-friendly name for the VNIC. Does not have to be unique.</div>
        </td>
        </tr>

        <tr>
        <td>hostname_label<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.</div>
        </td>
        </tr>

        <tr>
        <td>assign_public_ip<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Determines whether the VNIC should be assigned a public IP address.  If not set and the VNIC is being created in a private subnet (that is, where <em>prohibitPublicIpOnVnic = true</em> in the Subnet), then no public IP address is assigned. If not set and the subnet is public <em>prohibitPublicIpOnVnic = false</em>, then a public IP address is assigned. If set to true and <em>prohibitPublicIpOnVnic = true</em>, an error is returned.</div>
        </td>
        </tr>

        <tr>
        <td>subnet_id<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the subnet to create the VNIC in.</div>
        </td>
        </tr>

        <tr>
        <td>private_ip<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The private IP to assign to the VNIC. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC's primary private IP address.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td rowspan="2">volume_details<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Details for attaching or detaching a volume to an instance with <em>state=present</em> or <em>state=RUNNING</em>. This option is only supported in experimental mode. To use an experimental feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object volume_details</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>attachment_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.</div>
        </td>
        </tr>

        <tr>
        <td>attachment_state<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td>
        <div>Attach a volume to the instance <em>instance_id</em> with <em>attachment_state=present</em>. Detach a volume from the instance <em>instance_id</em> with <em>attachment_state=absent</em>.</div>
        </td>
        </tr>

        <tr>
        <td>type<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>iscsi</td>
        <td><ul><li>iscsi</li></ul></td>
        <td>
        <div>The type of volume. The only supported value is &quot;iscsi&quot;.</div>
        </td>
        </tr>

        <tr>
        <td>volume_id<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The OCID of the volume to be attached to or detached from the instance <em>instance_id</em>.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
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

    
    - name: Launch/create an instance using an image, with custom metadata and a private IP assignment
      oci_instance:
         name: myinstance1
         availability_domain: "BnQb:PHX-AD-1"
         compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
         image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...sa7klnoa"
         shape: "BM.Standard1.36"
         metadata:
            foo: bar
            baz: quux
         volume_details:
            attachment_state: present
            volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
         vnic:
            hostname_label: "myinstance1"
            private_ip: "10.0.0.5"
            subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

    - name: Launch/create an instance using a boot volume, a private IP assignment and attach a volume
      oci_instance:
         name: myinstance2
         availability_domain: "BnQb:PHX-AD-1"
         source_details:
            source_type: bootVolume
            boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
         compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
         shape: "BM.Standard1.36"
         volume_details:
            attachment_state: present
            volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
         vnic:
            hostname_label: "myinstance2"
            private_ip: "10.0.0.6"
            subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

    - name: Update an instance's name
      oci_instance:
         name: myinstance1-new-name
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"

    - name: Detach a volume from an instance
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         volume_details:
            attachment_state: absent
            volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

    - name: Stop an instance
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "stopped"

    - name: Stop an instance and detach boot volume
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "stopped"
         boot_volume_details:
            boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
            attachment_state: absent

    - name: Attach a boot volume & Start an instance
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "running"
         boot_volume_details:
            boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx

    - name: Reset an instance
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "reset"

    - name: Terminate/delete an instance
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "absent"

    - name: Terminate/delete an instance and preserve boot volume
      oci_instance:
         id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
         state: "absent"
         preserve_boot_volume: yes

    - name: Ensure 3 web-server instances with the defined tag namespace "TagNamespace1", tag key "Application" and
            value "App1" are running
      oci_instance:
         name: my-web-server
         availability_domain: "BnQb:PHX-AD-1"
         compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
         image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx...sa7klnoa"
         shape: "BM.Standard1.36"
         vnic:
            subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
         defined_tags:
            TagNamespace1: { Application: App1 }
         exact_count: 3
         count_tag:
            TagNamespace1: { Application: App1 }



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
    <td>added_instances</td>
    <td>
        <div>Details of newly added compute instances</div>
    </td>
    <td align=center>On successful addition of new compute instances</td>
    <td align=center>complex</td>
    <td align=center>Same as the instances sample</td>
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
            <div>The current state of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>TERMINATED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>extended_metadata</td>
        <td>
            <div>Additional key-value pairs associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq</td>
        </tr>

        <tr>
        <td>region</td>
        <td>
            <div>The region that contains the Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>phx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the instance was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-instance-968</td>
        </tr>

        <tr>
        <td>image_id</td>
        <td>
            <div>The OCID of the image that the instance is based on</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.Standard1.36</td>
        </tr>

        <tr>
        <td>ipxe_script</td>
        <td>
            <div>A custom iPXE script that will run when the instance boots</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>volume_attachments</td>
        <td>
            <div>List of information about volume attachments</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>complex</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>boot_volume_attachment</td>
        <td>
            <div>Information of the boot volume attachment.</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Custom metadata that was associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        </table>
    </td>
    </tr>

    <tr>
    <td>instance</td>
    <td>
        <div>Details of the OCI compute instance launched, updated or terminated as a result of the current operation</div>
    </td>
    <td align=center>On successful operation (create, update and terminate) on a single Compute instance</td>
    <td align=center>complex</td>
    <td align=center></td>
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
            <div>The current state of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>TERMINATED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>extended_metadata</td>
        <td>
            <div>Additional key-value pairs associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq</td>
        </tr>

        <tr>
        <td>region</td>
        <td>
            <div>The region that contains the Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>phx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the instance was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-instance-968</td>
        </tr>

        <tr>
        <td>image_id</td>
        <td>
            <div>The OCID of the image that the instance is based on</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.Standard1.36</td>
        </tr>

        <tr>
        <td>ipxe_script</td>
        <td>
            <div>A custom iPXE script that will run when the instance boots</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>volume_attachments</td>
        <td>
            <div>List of information about volume attachments</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>complex</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>boot_volume_attachment</td>
        <td>
            <div>Information of the boot volume attachment.</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Custom metadata that was associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        </table>
    </td>
    </tr>

    <tr>
    <td>terminated_instances</td>
    <td>
        <div>Details of terminated compute instances</div>
    </td>
    <td align=center>On successful termination of compute instances</td>
    <td align=center>complex</td>
    <td align=center>Same as the instances sample</td>
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
            <div>The current state of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>TERMINATED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>extended_metadata</td>
        <td>
            <div>Additional key-value pairs associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq</td>
        </tr>

        <tr>
        <td>region</td>
        <td>
            <div>The region that contains the Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>phx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the instance was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-instance-968</td>
        </tr>

        <tr>
        <td>image_id</td>
        <td>
            <div>The OCID of the image that the instance is based on</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.Standard1.36</td>
        </tr>

        <tr>
        <td>ipxe_script</td>
        <td>
            <div>A custom iPXE script that will run when the instance boots</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>volume_attachments</td>
        <td>
            <div>List of information about volume attachments</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>complex</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>boot_volume_attachment</td>
        <td>
            <div>Information of the boot volume attachment.</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Custom metadata that was associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        </table>
    </td>
    </tr>

    <tr>
    <td>instances</td>
    <td>
        <div>List of details of the OCI compute instances launched or terminated as a result of the current operation</div>
    </td>
    <td align=center>On successful operation (launch, update and terminate) of compute instances. For 'exact_count' scenarios, details of all matching instances are returned for this key.</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'RUNNING', 'availability_domain': 'BnQb:PHX-AD-1', 'extended_metadata': {}, 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq', 'region': 'phx', 'time_created': '2017-11-14T16:09:07.557000+00:00', 'display_name': 'ansible-test-968', 'image_id': 'ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....7klnoa', 'shape': 'BM.Standard1.36', 'ipxe_script': None, 'volume_attachments': [{'lifecycle_state': 'ATTACHED', 'availability_domain': 'BnQb:PHX-AD-1', 'display_name': 'ansible_volume_attachment', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'chap_username': None, 'time_created': '2017-11-23T11:17:50.139000+00:00', 'id': 'ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx', 'instance_id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx', 'iqn': 'iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3', 'ipv4': '169.254.2.2', 'volume_id': 'ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx', 'attachment_type': 'iscsi', 'port': 3260, 'chap_secret': None}], 'boot_volume_attachment': {'boot_volume_id': 'ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx', 'availability_domain': 'IwGV:US-ASHBURN-AD-1', 'display_name': 'Remote boot attachment for instance', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'lifecycle_state': 'ATTACHED', 'time_created': '2018-01-15T07:23:10.838000+00:00', 'instance_id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx', 'id': 'ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx'}, 'id': 'ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....lxiggdq', 'metadata': {'foo': 'bar', 'baz': 'quux'}}]</td>
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
            <div>The current state of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>TERMINATED</td>
        </tr>

        <tr>
        <td>availability_domain</td>
        <td>
            <div>The Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BnQb:PHX-AD-1</td>
        </tr>

        <tr>
        <td>extended_metadata</td>
        <td>
            <div>Additional key-value pairs associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
        <td align=center>{'foo': 'bar'}</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The OCID of the compartment that contains the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq</td>
        </tr>

        <tr>
        <td>region</td>
        <td>
            <div>The region that contains the Availability Domain the instance is running in.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>phx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>The date and time the instance was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>2017-11-20 04:52:54.541000</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>A user-friendly name for the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible-instance-968</td>
        </tr>

        <tr>
        <td>image_id</td>
        <td>
            <div>The OCID of the image that the instance is based on</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>shape</td>
        <td>
            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>BM.Standard1.36</td>
        </tr>

        <tr>
        <td>ipxe_script</td>
        <td>
            <div>A custom iPXE script that will run when the instance boots</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>None</td>
        </tr>

        <tr>
        <td>volume_attachments</td>
        <td>
            <div>List of information about volume attachments</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>complex</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>boot_volume_attachment</td>
        <td>
            <div>Information of the boot volume attachment.</div>
        </td>
        <td align=center>In experimental mode.</td>
        <td align=center>dict</td>
        <td align=center></td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>The OCID of the instance.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>metadata</td>
        <td>
            <div>Custom metadata that was associated with the instance</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict(str, str)</td>
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

    * Sivakumar Thyagarajan (@sivakumart)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
