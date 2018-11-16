#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: oci_instance
short_description: Launch, terminate and control the lifecycle of OCI Compute instances
description:
    - This module allows the user to launch/create, terminate and perform other power actions on OCI Compute Service
      instances. An instance represents a compute host. The image used to launch the instance determines its operating
      system and other software. The shape specified during the launch process determines the number of CPUs and memory
      allocated to the instance. For more information, see Overview of the Compute Service at
      U(https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm). In experimental mode,
      this module also allows attaching/detaching volumes and boot volumes to an instance.
version_added: "2.5"
options:
    availability_domain:
        description: The Availability Domain of the instance. Required when creating a compute instance with
                     I(state=present).
        required: false
    boot_volume_details:
        description: Details for attaching/detaching a boot volume to/from an instance. I(boot_volume_details) is
                     mutually exclusive with I(image_id). This option is only supported in experimental mode. To use
                     an experimental feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        required: false
        suboptions:
            attachment_state:
                description: Attach a boot volume to the instance I(instance_id) with I(attachment_state=present).
                             Detach a boot volume from the instance I(instance_id) with I(attachment_state=absent).
                required: false
                default: present
                choices: ['present', 'absent']
            boot_volume_id:
                description: The OCID of the boot volume.
                required: true
    compartment_id:
        description: The OCID of the compartment. Required when I(state=present).
        required: false
    extended_metadata:
        description: Additional metadata key/value pairs that you provide. They serve a similar purpose and
                     functionality from fields in the I(metadata) object. They are distinguished from I(metadata)
                     fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps
                     only).
                     If you don't need nested metadata values, it is strongly advised to avoid using this object and
                     use the Metadata object instead.
        required: false
    exact_count:
        description: Indicates how many instances that match the I(count_tag) option should be running. This must be
                     used with I(state=present) and a valid I(count_tag). If the number of compute instances that match
                     C(count_tag) is lesser than C(exact_count), additional compute instances would be provisioned to
                     match the desired C(exact_count). If the number of matching compute instances is larger than
                     C(exact_count), compute instances would be terminated to match the desired C(exact_count). The
                     latest launch instance(s) from the set of instances that match C(count_tag) are picked for
                     termination.
                     Private IP assignments through I(private_ip), and specification of I(hostname_label) and
                     I(volume_details) and I(boot_volume_details) is not supported with I(exact_count) and I(count_tag).
                     By default, an auto-incremented integer value is suffixed to the value of I(display_name) and
                     assigned as the display_name of a newly provisioned instance. For example, if I(display_name) is
                     'my_web_server', new compute instances would be called 'my_web_server_0', 'my_web_server_1'
                     and so on. To control the generated display name in a fine-grained manner, use "printf" style
                     format in I(display_name) such as 'my_%d_web_server'.
        required: false
    count_tag:
        description: Used with I(exact_count) to determine how many compute instances matching the specific tag criteria
                     C(count_tag) must be running. Only I(defined_tags) associated with an instance are considered for
                     matching against C(count_tag).
        required: false
    fault_domain:
        description: A fault domain is a grouping of hardware and infrastructure within an availability domain. Each
                     availability domain contains three fault domains. Fault domains let you distribute your instances
                     so that they are not on the same physical hardware within a single availability domain. A hardware
                     failure or Compute hardware maintenance that affects one fault domain does not affect instances in
                     other fault domains. If you do not specify the fault domain, the system selects one for you. To
                     change the fault domain for an instance, terminate it and launch a new instance in the preferred
                     fault domain. To get a list of fault domains, use M(oci_fault_domain_facts).
        required: false
    metadata:
        description: A hash/dictionary of custom key/value pairs that are associated with the instance. This
                     option is also used to provide information to cloud-init and specifying
                     "ssh_authorized_keys" for the default user of the instance. This hash is specified
                     as '{"key":"value"}' and '{"key":"value","key":"value"}'.
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information. If a C(display_name) is specified, and if I(exact_count) is specified, the display name
                     would be suffixed with an auto-incrementing integer.
        required: false
        aliases: ['name']
    image_id:
        description: The OCID of the image used to boot the instance. Required to launch an instance using an image with
                     I(state=present). I(image_id) is mutually exclusive with I(boot_volume_details). This can
                     also be provided through I(source_details).
        required: false
    instance_id:
        description: The OCID of the compute instance. Required for updating an existing compute instance
                     when I(state=present), for performing power actions (such as start, stop, softreset
                     or reset) on an instance, and for terminating an instance I(state=absent).
        required: false
        aliases: [ 'id' ]
    ipxe_script:
        description: custom iPXE script that will run when the instance boots.
        required: false
    preserve_boot_volume:
        description: Whether to preserve the boot volume when terminating an instance with I(state=absent).
        required: false
        default: False
        type: bool
    enable_parallel_requests:
        description: Whether to scale up and down I(exact_count) instances in parallel. By default, I(exact_count)
                     instances are launched or terminated in parallel.
        required: False
        default: True
        type: bool
    max_thread_count:
        description: When I(enable_parallel_requests=True), indicates the number of maximum parallel operations that are
                     used to launch or terminate I(exact_count) instances. The default number of threads used is the
                     number of cores in your machine.
        required: False
        type: int
    shape:
        description: The shape of the instance. Required when creating a compute instance with I(state=present).
        required: false
    source_details:
        description: Details for creating an instance. Use this parameter to specify whether a boot volume or an image
                     should be used to launch a new instance.
        required: true
        suboptions:
            source_type:
                description: The source type for the instance. Use image when specifying the image OCID. Use bootVolume
                             when specifying the boot volume OCID.
                required: true
                choices: ['image', 'bootVolume']
            image_id:
                description: The OCID of the image used to boot the instance. Required if I(source_type) is "image".
                required: false
            boot_volume_id:
                description: The OCID of the boot volume used to boot the instance. Required if I(source_type) is
                             "bootVolume".
                required: false
    state:
        description: The state of the instance that must be asserted to. When I(state=present), and the
                     compute instance doesn't exist, the instance is launched/created with the specified
                     details. When I(state=absent), the compute instance is terminated. When
                     I(state=stopped), the compute instance is powered off. When I(state=running), the
                     compute instance is powered on. When I(state=softreset), an ACPI shutdown is
                     initiated and the compute instance is powered on. When I(state=reset), the
                     compute instance is powered off and then powered on.
                     Note that I(state=softreset) and I(state=reset) states are not idempotent. Every time a play is
                     executed with these C(state) options, a shutdown and a power on sequence is executed against the
                     instance.
        required: false
        default: "present"
        choices: ['present', 'absent', 'running', 'reset', 'softreset', 'stopped']
    volume_details:
        description: Details for attaching or detaching a volume to an instance with I(state=present) or
                     I(state=RUNNING). This option is only supported in experimental mode. To use an experimental
                     feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        required: false
        suboptions:
            attachment_state:
                description: Attach a volume to the instance I(instance_id) with I(attachment_state=present). Detach a
                             volume from the instance I(instance_id) with I(attachment_state=absent).
                required: false
                default: present
                choices: ['present', 'absent']
            attachment_name:
                description: A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering
                             confidential information.
                required: false
            type:
                description: The type of volume. The only supported value is "iscsi".
                required: false
                default: iscsi
                choices: ['iscsi']
            volume_id:
                description: The OCID of the volume to be attached to or detached from the instance I(instance_id).
                required: false
    vnic:
        description: Details for the primary VNIC that is automatically created and attached when the instance is
                     launched. Required when creating a compute instance with I(state=present).
        required: false
        aliases: ['create_vnic_details']
        suboptions:
            assign_public_ip:
                description: Determines whether the VNIC should be assigned a public IP address.  If
                             not set and the VNIC is being created in a private subnet (that is,
                             where I(prohibitPublicIpOnVnic = true) in the Subnet), then no public
                             IP address is assigned. If not set and the subnet is public
                             I(prohibitPublicIpOnVnic = false), then a public IP address is
                             assigned. If set to true and I(prohibitPublicIpOnVnic = true),
                             an error is returned.
                required: false
            hostname_label:
                description: The hostname for the VNIC's primary private IP. Used for DNS. The value
                             is the hostname portion of the primary private IP's fully qualified
                             domain name (FQDN) (for example, bminstance-1 in FQDN
                             bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all
                             VNICs in the subnet and comply with RFC 952 and RFC 1123.
                required: false
            name:
                description: A user-friendly name for the VNIC. Does not have to be unique.
                required: false
            private_ip:
                description: The private IP to assign to the VNIC. Must be an available IP address
                             within the subnet's CIDR. If you don't specify a value, Oracle
                             automatically assigns a private IP address from the subnet. This is
                             the VNIC's primary private IP address.
                required: false
            skip_source_dest_check:
                description: Determines whether the source/destination check is disabled on the VNIC.
                             Defaults to false, which means the check is performed.
                required: false
                default: false
            subnet_id:
                description: The OCID of the subnet to create the VNIC in.
                required: true

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
'''

EXAMPLES = '''
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

- name: Launch/create an instance using a boot volume, a private IP assignment and attach a volume, and a specific
        fault domain
  oci_instance:
     name: myinstance2
     availability_domain: "BnQb:PHX-AD-1"
     fault_domain: "FAULT-DOMAIN-2"
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

'''

RETURN = '''
instance:
    description: Details of the OCI compute instance launched, updated or terminated as a result of the current operation
    returned: On successful operation (create, update and terminate) on a single Compute instance
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of the instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: always
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        fault_domain:
            description: The name of the fault domain the instance is running in. A fault domain is a grouping of
                         hardware and infrastructure within an availability domain. Each availability domain contains
                         three fault domains. Fault domains let you distribute your instances so that they are not on
                         the same physical hardware within a single availability domain. A hardware failure or Compute
                         hardware maintenance that affects one fault domain does not affect instances in other fault
                         domains. If you do not specify the fault domain, the system selects one for you. To change the
                         fault domain for an instance, terminate it and launch a new instance in the preferred fault
                         domain.
            returned: always
            type: string
            sample: "FAULT-DOMAIN-1"
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
            type: complex
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: always
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: always
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: always
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: always
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: always
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
instances:
    description: List of details of the OCI compute instances launched or terminated as a result of the current operation
    returned: On successful operation (launch, update and terminate) of compute instances. For 'exact_count' scenarios,
              details of all matching instances are returned for this key.
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of the instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: always
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        fault_domain:
            description: The name of the fault domain the instance is running in. A fault domain is a grouping of
                         hardware and infrastructure within an availability domain. Each availability domain contains
                         three fault domains. Fault domains let you distribute your instances so that they are not on
                         the same physical hardware within a single availability domain. A hardware failure or Compute
                         hardware maintenance that affects one fault domain does not affect instances in other fault
                         domains. If you do not specify the fault domain, the system selects one for you. To change the
                         fault domain for an instance, terminate it and launch a new instance in the preferred fault
                         domain.
            returned: always
            type: string
            sample: "FAULT-DOMAIN-1"
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
            type: complex
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: always
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: always
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: always
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: always
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: always
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

    sample: [{"availability_domain": "BnQb:PHX-AD-1",
              "boot_volume_attachment": {
                                          "availability_domain": "IwGV:US-ASHBURN-AD-1",
                                          "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                                          "display_name": "Remote boot attachment for instance",
                                          "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "lifecycle_state": "ATTACHED",
                                          "time_created": "2018-01-15T07:23:10.838000+00:00"
              },
             "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq",
             "display_name": "ansible-test-968",
             "extended_metadata": {},
             "fault_domain": "FAULT-DOMAIN-1",
             "id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....lxiggdq",
             "image_id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....7klnoa",
             "ipxe_script": null,
             "lifecycle_state": "RUNNING",
             "metadata": {"baz": "quux", "foo": "bar"},
             "region": "phx",
             "shape": "BM.Standard1.36",
             "time_created": "2017-11-14T16:09:07.557000+00:00",
             "volume_attachments":  [{
                                    "attachment_type": "iscsi",
                                    "availability_domain": "BnQb:PHX-AD-1",
                                    "chap_secret": null,
                                    "chap_username": null,
                                    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                                    "display_name": "ansible_volume_attachment",
                                    "id": "ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx",
                                    "instance_id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx",
                                    "ipv4": "169.254.2.2",
                                    "iqn": "iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3",
                                    "lifecycle_state": "ATTACHED",
                                    "port": 3260,
                                    "time_created": "2017-11-23T11:17:50.139000+00:00",
                                    "volume_id": "ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx"
                                  }]
            }]
added_instances:
    description: Details of newly added compute instances
    returned: On successful addition of new compute instances
    type: complex
    sample: Same as the instances sample
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of the instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: always
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
            type: complex
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: always
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: always
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: always
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: always
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: always
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
terminated_instances:
    description: Details of terminated compute instances
    returned: On successful termination of compute instances
    type: complex
    sample: Same as the instances sample
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of the instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: always
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        fault_domain:
            description: The name of the fault domain the instance is running in. A fault domain is a grouping of
                         hardware and infrastructure within an availability domain. Each availability domain contains
                         three fault domains. Fault domains let you distribute your instances so that they are not on
                         the same physical hardware within a single availability domain. A hardware failure or Compute
                         hardware maintenance that affects one fault domain does not affect instances in other fault
                         domains. If you do not specify the fault domain, the system selects one for you. To change the
                         fault domain for an instance, terminate it and launch a new instance in the preferred fault
                         domain.
            returned: always
            type: string
            sample: "FAULT-DOMAIN-1"
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
            type: complex
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: always
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: always
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: always
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: always
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: always
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle.oci_utils import check_mode

import six
from multiprocessing.dummy import Pool as ThreadPool

try:
    import oci
    from oci.core.compute_client import ComputeClient
    from oci.core.models import AttachBootVolumeDetails
    from oci.core.models import AttachVolumeDetails
    from oci.core.models import LaunchInstanceDetails
    from oci.core.models import UpdateInstanceDetails
    from oci.core.models import CreateVnicDetails
    from oci.core.models import InstanceSourceViaBootVolumeDetails
    from oci.core.models import InstanceSourceViaImageDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "instance"


def get_volume_attachments(compute_client, instance):
    param_map = {'instance_id': instance['id'],
                 'compartment_id': instance['compartment_id']}

    volume_attachments = to_dict(oci_utils.list_all_resources(compute_client.list_volume_attachments,
                                                              **param_map))
    return volume_attachments


def get_boot_volume_attachment(compute_client, instance):
    param_map = {'availability_domain': instance['availability_domain'],
                 'instance_id': instance['id'],
                 'compartment_id': instance['compartment_id']}

    boot_volume_attachments = to_dict(oci_utils.list_all_resources(compute_client.list_boot_volume_attachments,
                                                                   **param_map))

    if boot_volume_attachments:
        return boot_volume_attachments[0]
    return None


def detach_volume(compute_client, module, volume_attachment_id):
    result = dict()
    result['changed'] = False

    try:
        volume_attachment = oci_utils.call_with_backoff(compute_client.get_volume_attachment,
                                                        volume_attachment_id=volume_attachment_id).data
        if volume_attachment.lifecycle_state in {'DETACHING', 'DETACHED'}:
            result['changed'] = False
            result['volume_attachment'] = to_dict(volume_attachment)
        else:
            oci_utils.call_with_backoff(compute_client.detach_volume,
                                        volume_attachment_id=volume_attachment_id)
            response = oci_utils.call_with_backoff(compute_client.get_volume_attachment,
                                                   volume_attachment_id=volume_attachment_id)
            result['volume_attachment'] = to_dict(oci.wait_until(compute_client,
                                                                 response,
                                                                 'lifecycle_state',
                                                                 'DETACHED').data)
            result['changed'] = True
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return result


def get_attach_volume_details(instance_id, volume_id, type, attachment_name=None):
    attach_volume_details = AttachVolumeDetails()
    attach_volume_details.display_name = attachment_name
    attach_volume_details.instance_id = instance_id
    attach_volume_details.type = type
    attach_volume_details.volume_id = volume_id
    return attach_volume_details


def attach_volume(compute_client, module, attach_volume_details):
    result = dict()
    result['changed'] = False

    try:
        response = oci_utils.call_with_backoff(compute_client.attach_volume,
                                               attach_volume_details=attach_volume_details)
        response = oci_utils.call_with_backoff(compute_client.get_volume_attachment,
                                               volume_attachment_id=response.data.id)
        result['volume_attachment'] = to_dict(
            oci.wait_until(compute_client, response, 'lifecycle_state', 'ATTACHED').data)
        result['changed'] = True
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))


def terminate_instance(compute_client, id, module):
    return oci_utils.delete_and_wait(resource_type=RESOURCE_NAME, client=compute_client,
                                     get_fn=compute_client.get_instance,
                                     kwargs_get={"instance_id": id}, delete_fn=compute_client.terminate_instance,
                                     kwargs_delete={"instance_id": id,
                                                    "preserve_boot_volume": module.params['preserve_boot_volume']},
                                     module=module)


def update_instance(compute_client, instance, module):
    result = dict()
    changed = False
    try:
        uid = UpdateInstanceDetails()
        if not oci_utils.are_attrs_equal(current_resource=instance, module=module, attributes=uid.attribute_map.keys()):
            # Update-able attributes are unequal, let us update the resource
            uid = oci_utils.update_model_with_user_options(curr_model=instance, update_model=uid, module=module)

            response = oci_utils.call_with_backoff(compute_client.update_instance, instance_id=instance.id,
                                                   update_instance_details=uid)
            changed = True
            result['instances'] = [to_dict(response.data)]
            result['instance'] = to_dict(response.data)  # retain for backward compat
        else:
            # No change needed, return the current instance
            result['instances'] = [to_dict(instance)]
            result['instance'] = to_dict(instance)  # retain for backward compat
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result['changed'] = changed
    return result


def power_action_on_instance(compute_client, id, desired_state, module):
    result = {}
    changed = False
    # The power action to execute on a compute instance to reach the desired 'state'
    state_action_map = {"stopped": "STOP",
                        "running": "START",
                        "reset": "RESET",
                        "softreset": "SOFTRESET"
                        }
    # The desired lifecycle state for the compute instance to reach the user specified 'state'
    desired_lifecycle_states = {'stopped': 'STOPPED',
                                'running': 'RUNNING',
                                'reset': 'RUNNING',
                                'softreset': 'RUNNING'
                                }
    try:
        response = oci_utils.call_with_backoff(compute_client.get_instance, instance_id=id)
        curr_state = response.data.lifecycle_state

        change_required = False

        # We need to perform a power action if the current state doesn't match the desired state
        if curr_state != desired_lifecycle_states[desired_state]:
            change_required = True

        # Resets also require a change
        if desired_state in ['softreset', 'reset']:
            change_required = True

        if change_required:
            changed = True
            oci_utils.call_with_backoff(compute_client.instance_action, instance_id=id,
                                        action=state_action_map[desired_state])
            response = oci_utils.call_with_backoff(compute_client.get_instance, instance_id=id)
            # for now the power actions on instances do not go through common utilities for wait.
            if module.params.get('wait', None):
                debug("waiting for lifecycle_state to reach {0}".format(desired_lifecycle_states[desired_state]))
                oci.wait_until(compute_client, response, 'lifecycle_state', desired_lifecycle_states[desired_state],
                               max_wait_seconds=module.params.get('wait_timeout',
                                                                  oci_utils.MAX_WAIT_TIMEOUT_IN_SECONDS))
                response = oci_utils.call_with_backoff(compute_client.get_instance, instance_id=id)
            else:
                debug("Not waiting for power action request {0} as 'wait' is false.".format(desired_state))

        result['instances'] = [to_dict(response.data)]
        result['instance'] = to_dict(response.data)  # retain for backward compat
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    result['changed'] = changed
    return result


def launch_instance(compute_client, module, display_name_override=None):
    lid = get_launch_instance_details(module, display_name_override)
    cvd = get_vnic_details(module)
    lid.create_vnic_details = cvd

    debug("Provisioning " + str(lid))
    result = oci_utils.create_and_wait(resource_type=RESOURCE_NAME, client=compute_client,
                                       create_fn=compute_client.launch_instance,
                                       kwargs_create={"launch_instance_details": lid},
                                       get_fn=compute_client.get_instance,
                                       get_param="instance_id",
                                       module=module)
    return result


def get_vnic_details(module):
    vnic_details = module.params.get('vnic', None)
    if not vnic_details:
        # Primary VNIC details(especially subnet_id is required)
        module.fail_json(msg="state is present and instance_id is not specified, but create_vnic_details is not "
                             "specified.")

    cvd = CreateVnicDetails()
    cvd.display_name = vnic_details.get('name', None)
    cvd.assign_public_ip = vnic_details.get('assign_public_ip', None)
    cvd.hostname_label = vnic_details.get('hostname_label', None)
    cvd.private_ip = vnic_details.get('private_ip', None)
    cvd.skip_source_dest_check = vnic_details.get('skip_source_dest_check', None)
    cvd.subnet_id = vnic_details['subnet_id']
    return cvd


def get_launch_instance_details(module, display_name_override=None):
    lid = LaunchInstanceDetails()

    # exact_count may override the user-specified display name with a generated `display_name`
    if display_name_override is not None:
        lid.display_name = display_name_override
    else:
        lid.display_name = module.params['name']

    lid.availability_domain = module.params['availability_domain']
    lid.compartment_id = module.params['compartment_id']

    # 'fault_domain' requires OCI Python SDK 2.0.1
    fault_domain = module.params['fault_domain']
    if fault_domain is not None:
        if 'fault_domain' in lid.attribute_map:
            lid.fault_domain = fault_domain
        else:
            module.fail_json(msg="OCI Python SDK 2.0.1 or above is required to support `fault_domain`. The local SDK"
                                 "version is {0}".format(oci.__version__))

    lid.extended_metadata = module.params['extended_metadata']
    lid.metadata = module.params['metadata']
    lid.ipxe_script = module.params['ipxe_script']
    lid.shape = module.params['shape']
    oci_utils.add_tags_to_model_from_module(lid, module)

    # An instance's source can either be specified by top-level options "image_id" or via "source_details"
    if "image_id" in module.params and module.params["image_id"] is not None:
        lid.source_details = _create_instance_source_via_image(module.params["image_id"])
    elif "source_details" in module.params and module.params["source_details"] is not None:
        source_details = module.params["source_details"]
        source_type = source_details.get("source_type", None)
        if source_type == "image":
            image_id = source_details.get("image_id", None)
            if not image_id:
                module.fail_json(msg="state is present, source_details' type is specified as image, but image_id is not"
                                     "specified")
            lid.source_details = _create_instance_source_via_image(image_id)
        elif source_type == "bootVolume":
            boot_volume_id = source_details.get("boot_volume_id", None)
            if not boot_volume_id:
                module.fail_json(msg="state is present, source_details' type is specified as bootVolume, but "
                                     "boot_volume_id is not specified")
            lid.source_details = _create_instance_source_via_boot_volume(boot_volume_id)
        else:
            module.fail_json(msg="value of source_type must be one of: 'bootVolume', 'image'")

    return lid


def _create_instance_source_via_image(image_id):
    instance_source_details = InstanceSourceViaImageDetails()
    instance_source_details.image_id = image_id
    return instance_source_details


def _create_instance_source_via_boot_volume(boot_volume_id):
    instance_source_details = InstanceSourceViaBootVolumeDetails()
    instance_source_details.boot_volume_id = boot_volume_id
    return instance_source_details


def debug(s):
    get_logger().debug(s)


def handle_volume_attachment(compute_client, module, volume_id, instance_id):
    result = dict()
    volume_details = module.params['volume_details']
    compartment_id = module.params['compartment_id']
    if instance_id is None:
        instance_id = module.params['instance_id']

    if compartment_id is None:
        compartment_id = compute_client.get_instance(instance_id).data.compartment_id

    try:
        # Check if volume_id is already attached to instance_id
        volume_attachments = to_dict(compute_client.list_volume_attachments(compartment_id,
                                                                            instance_id=instance_id,
                                                                            volume_id=volume_id).data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Case when volume_id is already ATTACHED or is ATTACHING to instance_id
    for volume_attachment in volume_attachments:
        if volume_attachment['lifecycle_state'] in ["ATTACHING", "ATTACHED"]:
            result['changed'] = False
            return result

    key_list = ["attachment_name", "type"]
    param_map = {k: v for (k, v) in six.iteritems(volume_details) if k in key_list and v is not None}

    attach_volume_details = get_attach_volume_details(instance_id=instance_id,
                                                      volume_id=volume_id,
                                                      **param_map)

    return attach_volume(compute_client, module, attach_volume_details)


def handle_volume_detachment(compute_client, module, volume_id):
    result = dict()
    compartment_id = module.params['compartment_id']
    instance_id = module.params['instance_id']
    if compartment_id is None:
        compartment_id = compute_client.get_instance(instance_id).data.compartment_id

    try:
        # Get the volume attachment with the instance_id & volume_id
        volume_attachments = to_dict(compute_client.list_volume_attachments(compartment_id,
                                                                            instance_id=instance_id,
                                                                            volume_id=volume_id).data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Volume attachment with volume_id & instance_id does not exist

    if not volume_attachments:
        result['changed'] = False
        return result

    for volume_attachment in volume_attachments:
        if volume_attachment['lifecycle_state'] in ["ATTACHED"]:
            volume_attachment_id = volume_attachment['id']
            return detach_volume(compute_client, module, volume_attachment_id)

    # Case when all volume attachments for instance_id & volume_id are in non-ATTACHED state
    result['changed'] = False
    return result


def combine_result(result, attachment_result, boot_volume_attachment_result):
    combined_result = result
    if attachment_result is None:
        attachment_result = {}
    if boot_volume_attachment_result is None:
        boot_volume_attachment_result = {}

    combined_result['changed'] = any([result['changed'], attachment_result.get('changed', False),
                                      boot_volume_attachment_result.get('changed', False)])
    return combined_result


@check_mode
def handle_volume_details(compute_client, module, instance_id=None):
    attachment_result = dict(changed=False)
    volume_details = module.params['volume_details']
    if volume_details:
        if 'attachment_state' in volume_details:
            attachment_state = volume_details['attachment_state']
        else:
            attachment_state = 'present'

        # Check if volume_id is specified
        if 'volume_id' in volume_details and volume_details['volume_id'] is not None:
            volume_id = volume_details['volume_id']
            if attachment_state == 'present':
                attachment_result = handle_volume_attachment(compute_client, module, volume_id, instance_id)
            elif attachment_state == 'absent':
                attachment_result = handle_volume_detachment(compute_client, module, volume_id)
            else:
                module.fail_json(msg="Invalid attachment_state under volume_details")
        else:
            attachment_result['changed'] = False

    return attachment_result


@check_mode
def add_volume_attachment_info(module, compute_client, result):
    if 'instances' in result:
        try:
            instances = result['instances']
            for idx, _ in enumerate(instances):
                vol_attachments = get_volume_attachments(compute_client, instances[idx])
                result['instances'][idx]['volume_attachments'] = vol_attachments
                if 'instance' in result:
                    result['instance']['volume_attachments'] = vol_attachments
        except ServiceError as ex:
            module.fail_json(msg=ex.message)


# Boot volume attachment attach and detach actions do not have separate "wait" related options. They share the
# module's options for wait and wait timeout.
def attach_boot_volume(compute_client, module, attach_boot_volume_details):
    return oci_utils.create_and_wait(resource_type="boot_volume_attachment", client=compute_client,
                                     create_fn=compute_client.attach_boot_volume,
                                     kwargs_create={"attach_boot_volume_details": attach_boot_volume_details},
                                     get_fn=compute_client.get_boot_volume_attachment,
                                     get_param="boot_volume_attachment_id", module=module)


def get_attach_boot_volume_details(instance_id, boot_volume_id, attachment_name=None):
    attach_boot_volume_details = AttachBootVolumeDetails()
    attach_boot_volume_details.display_name = attachment_name
    attach_boot_volume_details.instance_id = instance_id
    attach_boot_volume_details.boot_volume_id = boot_volume_id
    return attach_boot_volume_details


def handle_boot_volume_attachment(compute_client, module, boot_volume_id, instance_id):
    result = dict()

    compartment_id = module.params['compartment_id']
    ad = module.params['availability_domain']
    if instance_id is None:
        instance_id = module.params['instance_id']
    try:
        if compartment_id is None:
            compartment_id = compute_client.get_instance(instance_id).data.compartment_id

        if ad is None:
            ad = compute_client.get_instance(instance_id).data.availability_domain

        # Check if boot_volume_id is already attached to instance_id
        boot_volume_attachments = to_dict(compute_client.list_boot_volume_attachments(ad,
                                                                                      compartment_id,
                                                                                      instance_id=instance_id,
                                                                                      boot_volume_id=boot_volume_id
                                                                                      ).data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Case when boot_volume_id is already ATTACHED or is ATTACHING to instance_id
    for boot_volume_attachment in boot_volume_attachments:
        if boot_volume_attachment['lifecycle_state'] in ["ATTACHING", "ATTACHED"]:
            result['changed'] = False
            return result

    attach_boot_volume_details = get_attach_boot_volume_details(instance_id=instance_id,
                                                                boot_volume_id=boot_volume_id)

    return attach_boot_volume(compute_client, module, attach_boot_volume_details)


def detach_boot_volume(compute_client, module, boot_volume_attachment_id):
    return oci_utils.delete_and_wait(resource_type="boot_volume_attachment", client=compute_client,
                                     get_fn=compute_client.get_boot_volume_attachment,
                                     kwargs_get={"boot_volume_attachment_id": boot_volume_attachment_id},
                                     delete_fn=compute_client.detach_boot_volume,
                                     kwargs_delete={"boot_volume_attachment_id": boot_volume_attachment_id},
                                     module=module)


def handle_boot_volume_detachment(compute_client, module, boot_volume_id):
    result = dict()
    compartment_id = module.params['compartment_id']
    instance_id = module.params['instance_id']
    ad = module.params['availability_domain']
    try:

        if compartment_id is None:
            compartment_id = compute_client.get_instance(instance_id).data.compartment_id

        if ad is None:
            ad = compute_client.get_instance(instance_id).data.availability_domain

        # Get the boot volume attachment with the instance_id & volume_id
        boot_volume_attachments = to_dict(compute_client.list_boot_volume_attachments(ad,
                                                                                      compartment_id,
                                                                                      instance_id=instance_id,
                                                                                      boot_volume_id=boot_volume_id
                                                                                      ).data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Boot volume attachment with volume_id & instance_id does not exist
    if not boot_volume_attachments:
        result['changed'] = False
        return result

    for boot_volume_attachment in boot_volume_attachments:
        if boot_volume_attachment['lifecycle_state'] == "ATTACHED":
            boot_volume_attachment_id = boot_volume_attachment['id']
            return detach_boot_volume(compute_client, module, boot_volume_attachment_id)

    # Case when boot volume attachment for instance_id & volume_id is in non-ATTACHED state
    result['changed'] = False
    return result


@check_mode
def handle_boot_volume_details(compute_client, module, instance_id=None):
    attachment_result = dict(changed=False)
    boot_volume_details = module.params['boot_volume_details']
    if boot_volume_details:
        if 'attachment_state' in boot_volume_details:
            attachment_state = boot_volume_details['attachment_state']
        else:
            attachment_state = 'present'

        # Check if boot_volume_id is specified
        if 'boot_volume_id' in boot_volume_details and boot_volume_details['boot_volume_id'] is not None:
            boot_volume_id = boot_volume_details['boot_volume_id']
            if attachment_state == 'present':
                attachment_result = handle_boot_volume_attachment(compute_client, module, boot_volume_id, instance_id)
            elif attachment_state == 'absent':
                attachment_result = handle_boot_volume_detachment(compute_client, module, boot_volume_id)
            else:
                module.fail_json(msg="Invalid attachment_state under boot_volume_details")

    return attachment_result


@check_mode
def add_boot_volume_attachment_info(module, compute_client, result):
    if 'instances' in result:
        try:
            instances = result['instances']
            for idx, instance in enumerate(instances):
                boot_vol_attachment = get_boot_volume_attachment(compute_client, instance)
                result['instances'][idx]['boot_volume_attachment'] = boot_vol_attachment
                if 'instance' in result:
                    result['instance']['boot_volume_attachment'] = boot_vol_attachment
        except ServiceError as ex:
            module.fail_json(msg=ex.message)


def _get_default_source_details(module):
    """
    Return the user specified value of image_id value as default for source_details.

    The GET model of the Resource API returns `image_id` in the `source_details` section of the Resource. So,
    we construct an equivalent source_details for a user-specified "image_id" and set as the default value for
    the "source_details" object, so that an existing resource with the same state matches.
    """
    if "source_details" in module.params and module.params["source_details"] is not None:
        return module.params["source_details"]

    elif "image_id" in module.params and module.params["image_id"] is not None:
        image_id = module.params["image_id"]
        return {"source_type": "image", "image_id": image_id}

    return None


def _get_default_image_id(module):
    """
    Return the image_id if the image_id was specified through "source_details", or None
    """
    if "source_details" in module.params and module.params["source_details"] is not None:
        source_details = module.params["source_details"]
        source_type = source_details["source_type"]
        if source_type == "image":
            return source_details["image_id"]
    return None


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def _get_exclude_attributes(module):
    # display_name is generated by OCI if unspecified, so always exclude it during matching
    exclude_attributes = {'display_name': True}
    if "source_details" in module.params and module.params["source_details"] is not None:
        source_details = module.params["source_details"]
        if source_details["source_type"] == "bootVolume":
            # if an Instance is being created by a boot volume id, ignore the "image_id" attribute of the existing
            # resources during matching
            exclude_attributes.update({'image_id': True})
    return exclude_attributes


def create_one_instance(compute_client, module, display_name_override=None):
    result = oci_utils.check_and_create_resource(resource_type="instance", create_fn=launch_instance,
                                                 kwargs_create={"compute_client": compute_client, "module": module,
                                                                "display_name_override": display_name_override},
                                                 list_fn=compute_client.list_instances,
                                                 kwargs_list={"compartment_id": module.params['compartment_id']},
                                                 module=module, model=LaunchInstanceDetails(),
                                                 exclude_attributes=_get_exclude_attributes(module),
                                                 default_attribute_values={"ipxe_script": None,
                                                                           "extended_metadata": {},
                                                                           "metadata": {},
                                                                           # during matching, if an existing
                                                                           # resource has the same values as the
                                                                           # current user request, consider it as
                                                                           # a match.
                                                                           "source_details":
                                                                               _get_default_source_details(module),
                                                                           "image_id":
                                                                               _get_default_image_id(module)})
    # Handle volume details when an instance is launched
    vol_attachment_result = {}
    if result['changed']:
        vol_attachment_result = handle_volume_details(compute_client, module, instance_id=result['instance']['id'])
    return result, vol_attachment_result


# For now, the exact_count implementation is simple. It ensures 'exact_count' number of instances are RUNNING in the
# specified compartment and AD. If new instances needs to be provisioned, they are provisioned in the specified AD.
#
# Future versions can enhance this placement behaviour, to support spreading new instances across ADs in a region and/or
# ensuring instances that match count_tag are evenly spread across regions. Future versions could also support cases
# where a user specifies a host-name pattern, private IP CIDR range under 'vnic', a volume attachment pattern etc,
# so that new provisioned instances can have names, IPs, volume attachments generated using that range.
def ensure_exact_count(compute_client, exact_count, count_tag, fault_domain, module):
    """
    Ensure that the exact number of instances specified by 'exact_count' and defined by 'count_tag' are in RUNNING
    state.
    :param fault_domain: An optional fault_domain for the new instances. If no fault_domain is specified, OCI chooses a
    fault_domain.
    :param compute_client: The compute client to use to create/terminate/list instances
    :param exact_count: The count of instances that the user wants to ensure
    :param count_tag: The tag that the `exact_count` instances must be tagged with to be considered as a match
    :param module: An AnsibleModule that represents user's values for module options in a play
    :return: A dict that has the 'change' state and a list of matching resources (instances), and a list of added
             (added_instances) and terminated (terminated_instances) instances
    """
    ad = module.params['availability_domain']
    compartment_id = module.params['compartment_id']

    # get all instances that match `count_tag`
    matching_instances = _get_matching_instances(compute_client, ad, compartment_id, count_tag, fault_domain)
    curr_inst_count = len(matching_instances)
    debug("The number of instances that match count_tag {0} is {1}. Desired exact_count is {2}".format(
        count_tag, curr_inst_count, exact_count))

    result = dict(changed=False)

    if curr_inst_count == exact_count:
        debug("No change required.")
        result['instances'] = to_dict(matching_instances)
    elif curr_inst_count < exact_count:
        to_add = exact_count - curr_inst_count
        debug("Need to create {0} new instances".format(to_add))
        added_instances = []

        # Generate names for the new instances
        names_for_new_instances = []
        current_names = [to_dict(inst)['display_name'] for inst in matching_instances]
        for inst_idx in range(to_add):
            name = module.params['name']
            display_name_override = None
            if name is not None:
                # Get a suffix to add to the new instance's name, so that it doesn't conflict with an existing
                # instance's display_name
                display_name_override = _get_next_available_suffix(current_names, exact_count, name)
            else:
                # Case when display_name is not provided, skip checking for matching existing instances and create an
                # instance, as an unique display_name would be generated by the backend anyway.
                module.params['force_create'] = True

            names_for_new_instances.append(display_name_override)
        debug("Names picked for the new instances {0}".format(names_for_new_instances))

        # construct params map for each new instance creation task.
        common_params = {'added_instances': added_instances, 'compute_client': compute_client,
                         'matching_instances': matching_instances, 'module': module}
        instance_creation_params = []
        for i in range(to_add):
            instance_specific_params = {'inst_idx': i, "display_name_override": names_for_new_instances[i]}
            new_map = common_params.copy()
            new_map.update(instance_specific_params)
            instance_creation_params.append(new_map)

        # execute tasks
        _execute_tasks(_add_one_exact_count_instance_splat, instance_creation_params, module)

        result['changed'] = True
        result['instances'] = to_dict(matching_instances)
        result['added_instances'] = to_dict(added_instances)
    else:
        to_delete = curr_inst_count - exact_count
        debug("Need to terminate {0} existing instances".format(to_delete))

        common_params = {'compute_client': compute_client, 'module': module}
        instance_termination_params = []
        for inst in matching_instances[-to_delete:]:
            instance_specific_params = {'id': to_dict(inst)['id']}
            new_map = common_params.copy()
            new_map.update(instance_specific_params)
            instance_termination_params.append(new_map)

        terminated_results = _execute_tasks(_terminate_instance_splat, instance_termination_params, module)

        result['changed'] = True
        result['instances'] = to_dict(matching_instances[:exact_count])
        result['terminated_instances'] = to_dict(terminated_results)

    return result, None


# Execute a set of launch/terminate tasks either in a parallel or sequential fashion as requested by the user
def _execute_tasks(task_method, list_of_params, module):
    if module.params["enable_parallel_requests"]:

        # construct a ThreadPool
        pool = ThreadPool(module.params['max_thread_count'])
        # run task_method in parallel, collecting results
        results = pool.map(task_method, list_of_params)
        pool.close()

        # wait for all instance creation requests to complete
        pool.join()

        # terminate the pool
        pool.terminate()
    else:
        # perform task_method in a sequential manner
        results = []
        for inst_idx in range(len(list_of_params)):
            results.append(task_method(list_of_params[inst_idx]))

    return results


# Pool.starmap accepts a sequence of argument tuples but only since 3.3, and therefore can't be employed by us. So,
# using an alternative to expand args that passed to Pool.map as discussed in https://stackoverflow.com/a/5442981
def _add_one_exact_count_instance_splat(args):
    _add_one_exact_count_instance(**args)


# Launch a single "exact_count" instance
def _add_one_exact_count_instance(added_instances, compute_client, inst_idx, matching_instances, module,
                                  display_name_override):
    debug("Creating instance # {0}".format(inst_idx))

    created_result, _ = create_one_instance(compute_client, module, display_name_override)
    added_instances.append(created_result['instance'])
    # Add newly created instances to matching_instances list so that subsequent suffix checks will consider it
    matching_instances.append(created_result['instance'])


def _terminate_instance_splat(args):
    terminated_instance = terminate_instance(**args)
    return terminated_instance['instance']


def _get_matching_instances(compute_client, ad, compartment_id, count_tag, fault_domain):
    # Sort instances by time_created in ASC order, so that we can terminate the latest instance easily
    param_map = {'availability_domain': ad, 'compartment_id': compartment_id, 'sort_by': "TIMECREATED",
                 'sort_order': "ASC"}
    curr_instances = oci_utils.list_all_resources(compute_client.list_instances, **param_map)
    return [inst for inst in curr_instances if
            inst.lifecycle_state == "RUNNING" and _does_instance_match_tag(inst, count_tag) and
            _does_instance_match_fault_domain(inst, fault_domain)]


def _does_instance_match_tag(instance, count_tag):
    for namespace in count_tag:
        if namespace in instance.defined_tags:
            tnspace = instance.defined_tags[namespace]
            if not all(tnspace[k] == v for k, v in count_tag[namespace].items()):
                return False
        else:
            # A namespace specified in "count_tag" is not in instance's defined_tags
            return False
    # all count_tag tags present in instance's defined_tags
    return True


def _does_instance_match_fault_domain(inst, fault_domain):
    if fault_domain is not None:
        return inst.fault_domain == fault_domain
    return True


def _get_next_available_suffix(current_names, exact_count, name_prefix):
    for num in range(exact_count):
        candidate_name = _generate_name_for_instance(name_prefix, num)
        if candidate_name not in current_names:
            current_names.append(candidate_name)
            return candidate_name
    return None


def _generate_name_for_instance(name_prefix, suffix):
    # If the 'display_name' is specified as a printf like string, use the user-specified format,
    # else the standard format to generate the name is <name_prefix>-<suffix>
    try:
        return name_prefix % suffix
    except TypeError:
        if name_prefix:
            return name_prefix + "-" + str(suffix)
        return None


def main():
    my_logger = oci_utils.get_logger("oci_instance")
    set_logger(my_logger)

    module_args = oci_utils.get_taggable_arg_spec(supports_create=True, supports_wait=True)
    module_args.update(dict(
        availability_domain=dict(type='str', required=False),
        boot_volume_details=dict(type='dict', required=False),
        compartment_id=dict(type='str', required=False),
        count_tag=dict(type='dict', required=False),
        exact_count=dict(type='int', required=False),
        extended_metadata=dict(type='dict', required=False),
        fault_domain=dict(type='str', required=False),
        instance_id=dict(type='str', required=False, aliases=['id']),
        image_id=dict(type='str', required=False),
        ipxe_script=dict(type='str', required=False),
        max_thread_count=dict(type='int', required=False),
        metadata=dict(type='dict', required=False),
        name=dict(type='str', required=False, aliases=['display_name']),
        preserve_boot_volume=dict(type='bool', required=False, default=False),
        enable_parallel_requests=dict(type='bool', required=False, default=True),
        shape=dict(type='str', required=False),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent', 'running', 'stopped',
                                                                           'reset', 'softreset']),
        volume_details=dict(type='dict', required=False),
        source_details=dict(type='dict', required=False),
        vnic=dict(type='dict', aliases=['create_vnic_details'])
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ['state', 'absent', ['instance_id']],
        ],
        mutually_exclusive=[
            ['boot_volume_details', 'image_id'],
            ['vnic', 'instance_id'],
            ['source_details', 'image_id'],
            ['exact_count', 'volume_details'],
            ['exact_count', 'boot_volume_details']
        ],
        required_together=[['exact_count', 'count_tag']]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module.')

    compute_client = oci_utils.create_service_client(module, ComputeClient)
    state = module.params['state']

    result = dict(changed=False)
    vol_attachment_result = dict(changed=False)
    boot_volume_attachment_result = dict(changed=False)

    id = module.params['instance_id']
    if id is not None:
        inst = None
        try:
            inst = oci_utils.call_with_backoff(compute_client.get_instance, instance_id=id).data
        except ServiceError as se:
            module.fail_json(msg=se.message())

        if state == 'absent':
            if inst is not None:
                terminate_result = terminate_instance(compute_client, id, module)
                result['changed'] = terminate_result['changed']
                result['instances'] = [terminate_result['instance']]
                result['instance'] = terminate_result['instance']  # retain for backward compat
            else:
                pass  # instance is already deleted.
        elif state == 'present':
            result = update_instance(compute_client, inst, module)
            # Handle volume details after update-instance operation
            vol_attachment_result = handle_volume_details(compute_client, module)
            # Handle boot volume details after update-instance operation
            boot_volume_attachment_result = handle_boot_volume_details(compute_client, module)
        else:
            # One of the power actions needs to be applied

            # If a boot volume is to be attached to an instance & the instance should be in RUNNING state,
            # the attachment should be done before the power_action_on_instance.
            if state == "running":
                boot_volume_attachment_result = handle_boot_volume_details(compute_client, module)

            # perform power actions on instance
            result = power_action_on_instance(compute_client, id, state, module)

            # Handle volume details after power action on instance
            vol_attachment_result = handle_volume_details(compute_client, module)

            # If a boot volume is to be detached from an instance & the instance should be in STOPPED state,
            # the detachment should be done after the power_action_on_instance.
            if state == "stopped":
                boot_volume_attachment_result = handle_boot_volume_details(compute_client, module)
    else:
        debug("check and create instances")

        exact_count = module.params.get('exact_count')
        count_tag = module.params.get('count_tag')
        fault_domain = module.params.get('fault_domain')
        if exact_count is not None and count_tag is not None:
            debug("Use exact_count and count_tag to ensure the specified number of instances are RUNNING.")
            result, _ = ensure_exact_count(compute_client, exact_count, count_tag, fault_domain, module)
        else:
            debug("Launch a new instance")
            create_result, vol_attachment_result = create_one_instance(compute_client, module)
            result['changed'] = create_result['changed']
            result['instances'] = [create_result['instance']]
            result['added_instances'] = [create_result['instance']]
            # for backward compatibility reasons, continue to return 'instance'. Eventually drop this deprecated
            # return value.
            result['instance'] = create_result['instance']

    result = combine_result(result, vol_attachment_result, boot_volume_attachment_result)
    add_volume_attachment_info(module, compute_client, result)
    add_boot_volume_attachment_info(module, compute_client, result)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
