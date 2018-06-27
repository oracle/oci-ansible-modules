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
module: oci_load_balancer_certificate
short_description: Add or remove a SSL certificate from a load balancer in
                   OCI Load Balancing Service
description:
    - Add a SSL certificate to OCI Load Balancer
    - Delete a SSL certificate, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer in which the certificate belongs
        required: true
        aliases: ['id']
    name:
        description: The name of the certificate  to add to the load balancer.
        required: true
    ca_certificate:
        description: The Certificate Authority certificate, or any interim certificate,
                     that you received from your SSL certificate provider. The absolute
                     path of the certificate file should be provided.
        required: false
    passphrase:
        description: A passphrase for encrypted private keys. This is needed only if you
                     created your certificate with a passphrase.
        required: false
    private_key :
        description: The SSL private key for your certificate, in PEM format.The absolute
                     path of the private key file should be provided.
        required: false
    public_certificate:
        description: The public certificate, in PEM format, that you received
                     from your SSL certificate provider. The absolute
                     path of the public certificate file should be provided.
        required: false
    state:
        description: Create or  delete certificate. For I(state=present),
                     if it does not exists, it gets added.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
'''

EXAMPLES = '''
# Note: These examples do not set authentication details.
# Add a certificate bundle (without passphrase) to a loadbalancer
- name: Add a certificate bundle (without passphrase) to a loadbalancer
  oci_load_balancer_certificate:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_certtificate"
    ca_certificate: "certificate_src/ca_cert.pem"
    private_key: "certificate_src/private_key.pem"
    public_certificate: "certificate_src/cert.pem"
    state: 'present'
# Add a certificate bundle (with a passphrase for encrypted private keys) to a load balancer
- name: Create certificate with Passphrase
  oci_load_balancer_certificate:
    name: "ansible_cert_with_passphrase"
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    ca_certificate: "certificate_src/ca_cert.pem"
    passphrase: "ansible"
    private_key: "certificate_src/private_key_with_passphrase.pem"
    public_certificate: "certificate_src/cert_with_passphrase.pem"
    state: 'present'
# Delete a SSL Certificate from a load balancer
- name: Delete a SSL certificate
  oci_load_balancer_certificate:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_certtificate"
    state: 'absent'
'''

RETURN = '''
    certificate:
        description: Attributes of the created certificate.
                     For delete, deleted certificate description will
                     be returned.
        returned: success
        type: complex
        contains:
            certificate_name:
                description: Name of the certificate
                returned: always
                type: string
                sample: ansible_certificate
            ca_certificate:
                description: The Certificate Authority certificate, or any interim certificate,
                             that you received from your SSL certificate provider.
                returned: always
                type: string
                sample: -----BEGIN CERTIFICATE-----
                            MIIDlTCCA
                        -----END CERTIFICATE-----
            public_certificate:
                description: The public certificate, in PEM format, that you received from
                             your SSL certificate provider.
                returned: always
                type: string
                sample: -----BEGIN CERTIFICATE-----
                            MIIDlTCCAn
                        -----END CERTIFICATE-----
        sample: {
                    "ca_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDlTCCAn2gAw\\n-----END CERTIFICATE-----",
                    "certificate_name":"ansible_cert",
                    "public_certificate":"-----BEGIN CERTIFICATE-----\\nMIIDPjCCAiYCCQC5OEUUNtrC\\n-----END CERTIFICATE-----"
                }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils


try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import CreateCertificateDetails
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_certificate(lb_client, module):
    certificate = None
    changed = False
    result = dict(
        changed=False,
        certificate=''
    )
    load_balancer_id = module.params.get('load_balancer_id')
    name = module.params.get('name')
    try:
        certificate = get_existing_certificate(
            lb_client, module, load_balancer_id, name)
        create_certificate_details = get_create_certificate_details(
            module, name)
        same_certificate = False
        if certificate is not None:
            same_certificate = is_same_certificate(
                create_certificate_details, certificate)
            if same_certificate:
                get_logger().info("Certificate " + name + " with same attribute values already available")
            else:
                get_logger().error(
                    "Certificate %s with different attribute value already available in load balancer %s", name,
                    load_balancer_id)
                module.fail_json(msg="Certificate " + name + " with different attribute value already available in "
                                                             "load balancer " + load_balancer_id)
        if not same_certificate:
            changed = True
            create_certificate_details = get_create_certificate_details(
                module, name)
            response = oci_utils.call_with_backoff(lb_client.create_certificate,
                                                   create_certificate_details=create_certificate_details,
                                                   load_balancer_id=load_balancer_id)
            oci_lb_utils.verify_work_request(lb_client, response)
            certificate = get_existing_certificate(
                lb_client, module, load_balancer_id, name)
    except ServiceError as ex:
        get_logger().error("Unable to create certificate due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create certificate due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    result['changed'] = changed
    result['certificate'] = to_dict(certificate)

    return result


def get_create_certificate_details(module, name):
    certificate_input_details = dict({'certificate_name': name,
                                      'ca_certificate': module.params.get('ca_certificate'),
                                      'passphrase': module.params.get('passphrase'),
                                      'private_key': module.params.get('private_key'),
                                      'public_certificate': module.params.get('public_certificate')})
    certificate_details = oci_lb_utils.create_certificates(
        dict({name: certificate_input_details})).get(name)
    create_certificate_details = CreateCertificateDetails()
    for attribute in create_certificate_details.attribute_map.keys():
        create_certificate_details.__setattr__(
            attribute, getattr(certificate_details, attribute))
    return create_certificate_details


def get_existing_certificate(lb_client, module, lb_id, name):
    existing_certificate = None
    get_logger().debug(
        "Trying to get Certificate %s in Load Balancer %s", name, lb_id)
    try:
        response = oci_utils.call_with_backoff(lb_client.list_certificates, load_balancer_id=lb_id)
        certificates = response.data
        for certificate in certificates:
            if certificate.certificate_name == name:
                existing_certificate = certificate
                break
    except ServiceError as ex:
        get_logger().error("Failed to perform checking existing Certificates",
                           exc_info=True)
        module.fail_json(msg=ex.message)
    if existing_certificate is None:
        get_logger().debug(
            "Certificate %s does not exist in load balancer %s", name, lb_id)
    return existing_certificate


def is_same_certificate(create_certificate_details, certificate):
    same_certificate = True
    for attribute in certificate.attribute_map.keys():
        if getattr(certificate, attribute) != getattr(create_certificate_details, attribute):
            same_certificate = False
            break
    return same_certificate


def delete_certificate(lb_client, module):
    changed = False
    certificate = None
    result = dict(
        changed=False,
        certificate=''
    )

    load_balancer_id = module.params.get('load_balancer_id')
    name = module.params.get('name')
    try:
        certificate = get_existing_certificate(
            lb_client, module, load_balancer_id, name)
        if certificate:
            get_logger().info("Deleting certificate %s on load balancer %s", name, load_balancer_id)
            response = oci_utils.call_with_backoff(lb_client.delete_certificate,
                                                   load_balancer_id=load_balancer_id, certificate_name=name)
            oci_lb_utils.verify_work_request(lb_client, response)
            changed = True
            get_logger().info("Successfully deleted certificate %s on load balancer %s",
                              name, load_balancer_id)
            result['certificate'] = to_dict(certificate)
    except ServiceError as ex:
        get_logger().error("Failed to delete certificate %s due to: %s", name, ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Failed to delete certificate %s due to: %s", name, str(ex))
        module.fail_json(msg=str(ex))

    if not changed:
        get_logger().info(
            "Unable to delete certificate %s as it is not available", name)
    result['changed'] = changed
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_certificate")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(
        name=dict(type='str', required=True),
        load_balancer_id=dict(type='str', required=True, aliases=['id']),
        ca_certificate=dict(type='str', required=False),
        passphrase=dict(type='str', required=False, no_log=True),
        private_key=dict(type='str', required=False),
        public_certificate=dict(type='str', required=False),
        state=dict(type='str', required=False, default='present',
                   choices=['present', 'absent'])
    ))

    module = AnsibleModule(
        argument_spec=module_args
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg='oci python sdk required for this module')

    lb_client = LoadBalancerClient(oci_utils.get_oci_config(module))
    state = module.params['state']

    if state == 'present':
        result = oci_utils.check_and_create_resource(resource_type='certificate',
                                                     create_fn=create_certificate,
                                                     kwargs_create={'lb_client': lb_client,
                                                                    'module': module},
                                                     list_fn=lb_client.list_certificates,
                                                     kwargs_list={
                                                         'load_balancer_id': module.params.get('load_balancer_id')},
                                                     module=module,
                                                     model=CreateCertificateDetails())
    elif state == 'absent':
        result = delete_certificate(lb_client, module)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
