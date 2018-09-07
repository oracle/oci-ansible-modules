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
module: oci_object
short_description: Manage objects in OCI Object Storage Service
description:
    - Create, read, update or delete an object in OCI. This module allows the user to store a file as an object in OCI
      or download an object from OCI to a local file.
version_added: "2.5"
options:
    bucket_name:
        description: Name of the bucket in which the object exists.
        required: true
        aliases: [ 'bucket' ]
    content_encoding:
        description: The content encoding of the object to be uploaded.
        required: false
    content_language:
        description: The content language of the object to be uploaded.
        required: false
    content_length:
        description: The content length of the object body to be uploaded.
        required: false
    content_md5:
        description: The base-64 encoded MD5 hash of the body to be uploaded.
        required: false
    content_type:
        description: The content type of the object to be uploaded.
        required: false
        default: "application/octet-stream"
    dest:
        description: The destination file path when downloading an object. Use with I(state=present) to download an
                     object. This option is mutually exclusive with I(src).
        required: false
    force:
        description: Force overwriting existing local file when downloading or existing remote object when uploading.
        required: false
        default: true
        type: bool
        aliases: [ 'overwrite' ]
    namespace_name:
        description: Name of the namespace in which the object exists.
        required: true
        aliases: [ 'namespace' ]
    object_name:
        description: Name of the object. For naming convention, refer
                     U(https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingobjects.htm#namerequirements).
        required: true
        aliases: [ 'name', 'object' ]
    opc_client_request_id:
        description: The client request ID for tracing.
        required: false
    opc_meta:
        description: User-defined metadata dict(str,str) for the object to be uploaded.
        required: false
        aliases: [ 'metadata' ]
    src:
        description: The source file path when uploading an object. Use with I(state=present) to upload
                     an object. This option is mutually exclusive with I(dest).
        required: false
    state:
        description: The final state of the object after the task.
                     Use I(state=absent) with I(object) to delete a specific object.
                     Use I(state=present) with I(dest) to download an object.
                     Use I(state=present) with I(src) to upload an object.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
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
'''

RETURN = '''
object:
    description: OCI object details
    returned: On successful operation
    type: dict
    sample: {
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "POST,PUT,GET,HEAD,DELETE,OPTIONS",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Expose-Headers": "Access-Control-Allow-Credentials,Access-Control-Allow-Methods,
             Access-Control-Allow-Origin,Content-Length,Content-MD5,Content-Type,ETag,Last-Modified,opc-client-info,
             opc-meta-author,opc-meta-doc-genre,opc-request-id",
            "Connection": "keep-alive",
            "Content-Length": "165661",
            "Content-MD5": "3zBENq6MBnedDrpl2+SttQ==",
            "Content-Type": "image/png",
            "Date": "Tue, 10 Oct 2017 13:58:02 GMT",
            "ETag": "5B3287C054A51CB6E053824310AC257B",
            "Last-Modified": "Tue, 10 Oct 2017 13:57:20 GMT",
            "opc-meta-author": "RC",
            "opc-request-id": "79bcd894-8a9d-fbfe-3717-fd92d518d0a1"
        }
'''

from ansible.module_utils.basic import AnsibleModule
import base64
import os

try:
    from oci.object_storage.object_storage_client import ObjectStorageClient
    from oci.exceptions import ServiceError
    from ansible.module_utils.oracle import oci_utils

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_object(object_storage_client, module):
    namespace = module.params['namespace_name']
    bucket = module.params['bucket_name']
    obj = module.params['object_name']
    changed = False
    result = dict()
    head_obj = head_object(object_storage_client, module)
    if head_obj is not None:
        try:
            oci_utils.call_with_backoff(object_storage_client.delete_object,
                                        namespace_name=namespace,
                                        bucket_name=bucket,
                                        object_name=obj)
            result['object'] = dict(head_obj.headers)
            changed = True
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    result['changed'] = changed
    return result


def get_object(object_storage_client, module):
    namespace = module.params['namespace_name']
    bucket = module.params['bucket_name']
    obj = module.params['object_name']
    dest = module.params['dest']

    result = dict()

    try:
        response = oci_utils.call_with_backoff(object_storage_client.get_object,
                                               namespace_name=namespace,
                                               bucket_name=bucket,
                                               object_name=obj)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Check if file exists with the same checksum. Get md5 hexdigest of the file content, convert it to binary and then
    #  get base-64 encoded MD5 hash.
    dest_md5 = base64.b64encode(base64.b16decode(module.md5(dest), True)).decode('ascii')
    if os.path.isfile(dest) and dest_md5 == response.headers['Content-MD5']:
        changed = False
    else:
        with open(dest, 'wb') as dest_file:
            dest_file.write(response.data.content)
            changed = True
            result['object'] = dict(response.headers)

    result['changed'] = changed

    return result


def head_object(object_storage_client, module):
    namespace = module.params['namespace_name']
    bucket = module.params['bucket_name']
    obj = module.params['object_name']

    try:
        response = oci_utils.call_with_backoff(object_storage_client.head_object,
                                               namespace_name=namespace,
                                               bucket_name=bucket,
                                               object_name=obj)
    except ServiceError:
        return None

    return response


def put_object(object_storage_client, module):
    namespace = module.params['namespace_name']
    bucket = module.params['bucket_name']
    obj = module.params['object_name']
    src = module.params['src']
    content_type = module.params['content_type']
    content_length = module.params['content_length']
    content_md5 = module.params['content_md5']
    content_language = module.params['content_language']
    content_encoding = module.params['content_encoding']

    opc_meta = dict()

    if module.params['opc_meta'] is not None:
        opc_meta = module.params['opc_meta']

    result = dict(changed=False)

    # Check if the object exists with same checksum.
    remote_object = head_object(object_storage_client, module)

    src_md5 = base64.b64encode(base64.b16decode(module.md5(src), True)).decode('ascii')

    # ENHANCEMENT_OVER_SDK: This is a EoU enhancement to make it easier for an Ansible user to provide
    # content for their object
    #
    if remote_object is not None and src_md5 == remote_object.headers['Content-MD5']:
        changed = False
    else:
        with open(src, 'rb') as src_file:
            put_object_body = src_file.read()

        try:
            response = oci_utils.call_with_backoff(object_storage_client.put_object,
                                                   namespace_name=namespace,
                                                   bucket_name=bucket,
                                                   object_name=obj,
                                                   put_object_body=put_object_body,
                                                   content_encoding=content_encoding,
                                                   content_language=content_language,
                                                   content_length=content_length,
                                                   content_md5=content_md5,
                                                   content_type=content_type,
                                                   opc_meta=opc_meta)
            changed = True
            result['object'] = dict(response.headers)

        except ServiceError as ex:
            module.fail_json(msg=ex.message)

    result['changed'] = changed
    return result


def src_is_valid(module, src):
    if not os.path.isfile(src):
        module.fail_json(msg="The source path %s must be a file." % src)

    if not os.access(src, os.R_OK):
        module.fail_json(msg="Failed to access %s. Make sure the file exists and that you have "
                             "read access." % src)

    return True


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type='str', required=True, aliases=['namespace']),
            bucket_name=dict(type='str', required=True, aliases=['bucket']),
            object_name=dict(type='str', required=True, aliases=['object', 'name']),
            src=dict(type='str', required=False),
            dest=dict(type='str', required=False),
            state=dict(type='str', required=False, default='present', choices=['absent', 'present']),
            force=dict(type='bool', required=False, default=True, aliases=['overwrite']),
            content_length=dict(type='str', required=False),
            opc_client_request_id=dict(type='str', required=False),
            content_md5=dict(type='str', required=False),
            content_type=dict(type='str', required=False, default="application/octet-stream"),
            content_language=dict(type='str', required=False),
            content_encoding=dict(type='str', required=False),
            opc_meta=dict(type=dict, required=False, aliases=['metadata'])
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=['src', 'dest']
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module')

    object_storage_client = oci_utils.create_service_client(module, ObjectStorageClient)

    state = module.params['state']
    src = module.params['src']
    dest = module.params['dest']
    force = module.params['force']
    obj = module.params['object_name']
    result = dict(
        changed=False
    )

    if state == 'present' and dest is not None:
        if force is True or not os.path.isfile(dest):
            result = get_object(object_storage_client, module)
        else:
            result['msg'] = "Destination %s already exists. Use force option to overwrite." % dest

    elif state == 'present' and src is not None:
        if src_is_valid(module, src):
            if force is True or head_object(object_storage_client, module) is None:
                result = put_object(object_storage_client, module)
            else:
                result['msg'] = "Object %s already present in bucket. Use force option to overwrite." % obj

    elif state == 'absent':
        result = delete_object(object_storage_client, module)

    else:
        module.fail_json(msg="Missing either src or dest option.")

    module.exit_json(**result)


if __name__ == '__main__':
    main()
