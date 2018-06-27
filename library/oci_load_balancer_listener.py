#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_load_balancer_listener
short_description: Add, modify and remove a listener from a backend set of a
                   load balancer in OCI Load Balancing Service
description:
    - Add a listener to a backend set in a OCI Load Balancer
    - Update a listener in a Load Balancer, if present, with any changed attribute
    - Delete a listener from OCI Load Balancer Backends, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer in which the listener belongs.
        required: true
        aliases: ['id']
    name:
        description: Name of the listener. It must be unique and it cannot be changed.
                     Mandatory field for all use cases.
        required: true
    default_backend_set_name:
        description: The name of the associated backend set. Mandatory for create and update.
        required: false
    port:
        description: The communication port for the listener. Mandatory for create and update.
        required: false
    protocol:
        description: The protocol on which the listener accepts connection requests.
                     Mandatory for create and update.
        required: false
    ssl_configuration:
        description: The load balancer SSL handling configuration details
        suboptions:
            certificate_name:
               description: A friendly name for the certificate bundle. It must be unique
                            and it cannot be changed. Valid certificate bundle names include
                            only alphanumeric characters,dashes, and underscores.Certificate
                            bundle names cannot contain spaces.
               required: true
            verify_depth:
               description: The maximum depth for peer certificate chain verification.
               required: false
            verify_peer_certificate:
               description: Whether the load balancer listener should verify peer certificates.
               required: false
        required: false
    connection_configuration:
        description: Configuration details for the connection between the client and backend servers.
        suboptions:
            idle_timeout:
               description: The maximum idle time, in seconds, allowed between two successive receive
                            or two successive send operations between the client and backend servers.
                            A send operation does not reset the timer for receive operations. A receive
                            operation does not reset the timer for send operations.
               required: true
        required: false
    state:
        description: Create,update or delete Load Balancer Backend. For I(state=present),
                     if it does not exists, it gets added. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
# Note: These examples do not set authentication details.
# Create Listener
- name: Create Listener
  oci_load_balancer_listener:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_listener"
    default_backend_set_name: "ansible_backend_set"
    protocol: "HTTP"
    port: 80
    ssl_configuration:
        certificate_name: 'certs1'
        verify_depth: 1
        verify_peer_certificate: True
    connection_configuration:
        idle_timeout: 1200
    state: 'present'
# Update Listener
- name: Update Listener Port
  oci_load_balancer_listener:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_listener"
    default_backend_set_name: "ansible_backend_set"
    protocol: "HTTP"
    port: 82
    state: 'present'

- name: Update Listener SSL Configuration
  oci_load_balancer_listener:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_listener"
    default_backend_set_name: "ansible_backend_set"
    protocol: "HTTP"
    port: 80
    ssl_configuration:
        certificate_name: 'certs2'
        verify_depth: 2
        verify_peer_certificate: False
    state: 'present'

- name: Update Listener Connection Configuration
  oci_load_balancer_listener:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_listener"
    default_backend_set_name: "ansible_backend_set"
    protocol: "HTTP"
    port: 80
    connection_configuration:
        idle_timeout: 1200
    state: 'present'

# Delete listener
- name: Delete Listener
  oci_load_balancer_listener:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_listener"
    state: 'absent'
'''

RETURN = '''
    listener:
        description: Attributes of the created/updated Listener.
                    For delete, deleted Listener description will
                    be returned.
        returned: success
        type: complex
        contains:
            name:
                description: Name of the Listener
                returned: always
                type: string
                sample: ansible_listener
            default_backend_set_name:
                description: The name of the associated backend set
                returned: always
                type: string
                sample: ansible_backend_set
            port:
                description: The communication port for the listener.
                returned: always
                type: string
                sample: 80
            protocol:
                description: The protocol on which the listener accepts connection requests.
                returned: always
                type: string
                sample: HTTP
            ssl_configuration:
                description: The load balancer SSL handling configuration details
                returned: always
                type: dict
                sample: {
                            "certificate_name": "certs1",
                            "verify_depth": 1,
                            "verify_peer_certificate": true
                        }
            connection_configuration:
                description: Configuration details for the connection between the client and backend servers.
                returned: always
                type: dict
                sample: {
                            "idle_timeout": 1200
                        }
        sample: {
                    "default_backend_set_name": "ansible_backend",
                    "name": "ansible_listener",
                    "port": 87,
                    "protocol": "HTTP",
                    "ssl_configuration": {
                        "certificate_name": "certs1",
                        "verify_depth": 1,
                        "verify_peer_certificate": true
                    },
                    "connection_configuration": {
                        "idle_timeout": 1200
                    }
               }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils
import six

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import CreateListenerDetails, UpdateListenerDetails, \
        SSLConfigurationDetails, ConnectionConfiguration
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_listener(lb_client, module):
    listener = None
    result = dict(
        changed=False,
        listener=''
    )
    load_balancer_id = module.params.get('load_balancer_id')
    name = module.params.get('name')
    existing_load_balancer = oci_lb_utils.get_existing_load_balancer(
        lb_client, module, load_balancer_id)
    listener = existing_load_balancer.listeners.get(name)
    try:
        if listener:
            changed, listener = update_listener(
                lb_client, module, listener, load_balancer_id, name)
            result['changed'] = changed
            result['listener'] = to_dict(listener)
        else:
            listeners_list = []
            for _, value in six.iteritems(existing_load_balancer.listeners):
                listeners_list.append(value)
            result = oci_utils.check_and_create_resource(resource_type='listener',
                                                         create_fn=create_listener,
                                                         kwargs_create={'lb_client': lb_client,
                                                                        'module': module,
                                                                        'lb_id': load_balancer_id,
                                                                        'name': name},
                                                         list_fn=None,
                                                         kwargs_list=None,
                                                         existing_resources=listeners_list,
                                                         module=module,
                                                         model=CreateListenerDetails())
    except ServiceError as ex:
        get_logger().error("Unable to create/update listener due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update listener due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_listener(lb_client, module, lb_id, name):
    result = dict()
    listener_input_details = get_listener_input_details(module)
    listener_details = oci_lb_utils.create_listeners(
        {name: listener_input_details}).get(name)
    create_listener_details = CreateListenerDetails()
    create_listener_details.name = name
    for attribute in create_listener_details.attribute_map.keys():
        if attribute == 'name':
            pass
        else:
            create_listener_details.__setattr__(
                attribute, getattr(listener_details, attribute))
    get_logger().info("Creating listener %s in load balancer %s with parameters %s",
                      name, lb_id, str(create_listener_details))
    response = oci_utils.call_with_backoff(lb_client.create_listener, create_listener_details=create_listener_details,
                                           load_balancer_id=lb_id)
    oci_lb_utils.verify_work_request(lb_client, response)
    get_logger().info("Successfully created listener %s in load balancer %s",
                      name, lb_id)
    listener = oci_lb_utils.get_existing_load_balancer(
        lb_client, module, lb_id).listeners.get(name)
    result['changed'] = True
    result['listener'] = to_dict(listener)
    return result


def update_listener(lb_client, module, listener, lb_id, name):
    update_listener_details = UpdateListenerDetails()
    changed = False
    get_logger().info("Updating listener %s in load balancer %s",
                      name, lb_id)
    for attribute in update_listener_details.attribute_map.keys():
        if attribute not in ['ssl_configuration', 'connection_configuration']:
            changed = oci_utils.check_and_update_attributes(
                update_listener_details, attribute, module.params.get(
                    attribute, None), getattr(listener, attribute), changed)
    input_ssl_configuration = oci_lb_utils.create_ssl_configuration(
        module.params.get('ssl_configuration', None))
    ssl_configuration_changed = update_listener_attr_difference(
        update_listener_details, listener, 'ssl_configuration',
        SSLConfigurationDetails, input_ssl_configuration)
    input_connection_configuration = oci_lb_utils.create_connection_configuration(
        module.params.get('connection_configuration', None))
    connection_configuration_changed = update_listener_attr_difference(
        update_listener_details, listener, 'connection_configuration',
        ConnectionConfiguration, input_connection_configuration)
    changed = changed or ssl_configuration_changed or connection_configuration_changed
    get_logger().debug("Existing listener property values: %s, input property values: %s",
                       listener, update_listener_details)
    if changed:
        response = oci_utils.call_with_backoff(lb_client.update_listener,
                                               update_listener_details=update_listener_details, load_balancer_id=lb_id,
                                               listener_name=name)
        oci_lb_utils.verify_work_request(lb_client, response)
        listener = oci_lb_utils.get_existing_load_balancer(
            lb_client, module, lb_id).listeners.get(name)
        get_logger().info("Successfully updated listener %s in load balancer %s",
                          name, lb_id)
    return changed, listener


def update_listener_attr_difference(update_listener_details, listener,
                                    attr_name, attr_class, input_attr_value):
    changed = False
    existing_attr_value = get_hashed_object(
        attr_class, getattr(listener, attr_name))
    if input_attr_value is None:
        update_listener_details.__setattr__(
            attr_name, existing_attr_value)
    else:
        changed = not input_attr_value.__eq__(existing_attr_value)
        if changed:
            update_listener_details.__setattr__(attr_name, input_attr_value)
        else:
            update_listener_details.__setattr__(attr_name, existing_attr_value)

    return changed


def get_hashed_object(class_type, object_with_value):
    if object_with_value is None:
        return None
    HashedClass = oci_lb_utils.generate_subclass(class_type)
    hashed_class_instance = HashedClass()
    for attribute in hashed_class_instance.attribute_map.keys():
        hashed_class_instance.__setattr__(
            attribute, getattr(object_with_value, attribute))
    return hashed_class_instance


def get_listener_input_details(module):
    listener_input_details = dict({'default_backend_set_name': module.params.get('default_backend_set_name'),
                                   'protocol': module.params.get('protocol'),
                                   'port': module.params.get('port'),
                                   'ssl_configuration': module.params.get('ssl_configuration', None),
                                   'connection_configuration': module.params.get('connection_configuration', None)})
    return listener_input_details


def delete_listener(lb_client, module):
    changed = False
    listener = None
    result = dict(
        changed=False,
        listener=''
    )

    load_balancer_id = module.params.get('load_balancer_id')
    name = module.params.get('name')
    listener = oci_lb_utils.get_existing_load_balancer(
        lb_client, module, load_balancer_id).listeners.get(name)
    try:
        if listener:
            get_logger().info("Deleting listener %s from load balancer %s",
                              name, load_balancer_id)
            response = oci_utils.call_with_backoff(lb_client.delete_listener, load_balancer_id=load_balancer_id,
                                                   listener_name=name)
            oci_lb_utils.verify_work_request(lb_client, response)
            changed = True
            get_logger().info("Successfully deleted listener %s in load balancer %s",
                              name, load_balancer_id)
    except ServiceError as ex:
        get_logger().error("Failed to delete listener due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        module.fail_json(msg=str(ex))
    result['changed'] = changed
    result['listener'] = to_dict(listener)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_listener")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(
        load_balancer_id=dict(type='str', required=True, aliases=['id']),
        default_backend_set_name=dict(type='str', required=False),
        name=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present',
                   choices=['present', 'absent']),
        protocol=dict(type='str', required=False),
        port=dict(type=int, required=False),
        ssl_configuration=dict(type=dict, required=False),
        connection_configuration=dict(type=dict, required=False)
    ))

    module = AnsibleModule(
        argument_spec=module_args
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module')

    lb_client = LoadBalancerClient(oci_utils.get_oci_config(module))
    state = module.params['state']

    if state == 'present':
        result = create_or_update_listener(lb_client, module)
    elif state == 'absent':
        result = delete_listener(lb_client, module)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
