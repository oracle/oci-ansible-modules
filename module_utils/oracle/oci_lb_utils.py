# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import oci

from ansible.module_utils.oracle import oci_utils
import six
from ansible.module_utils.facts.utils import get_file_content

try:
    from oci.load_balancer.models import BackendDetails, BackendSetDetails, \
        HealthCheckerDetails, SessionPersistenceConfigurationDetails, \
        SSLConfigurationDetails, CertificateDetails, ListenerDetails, \
        ConnectionConfiguration
    from oci.util import to_dict
    from oci.exceptions import ServiceError, ClientError
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

DEFAULT_COMPLETED_STATES = ['SUCCEEDED', 'FAILED']

MAX_WAIT_TIMEOUT_IN_SECONDS = 1200


def verify_work_request(lb_client, response):
    work_request_id = None
    if response is not None:
        work_request_id = response.headers.get('opc-work-request-id')
    oci.wait_until(lb_client, lb_client.get_work_request(work_request_id),
                   evaluate_response=lambda r: r.data.lifecycle_state in ['SUCCEEDED', 'FAILED'])
    response = lb_client.get_work_request(work_request_id)
    if response.data.lifecycle_state == 'FAILED':
        raise ClientError(Exception(response.data.error_details))
    return response


def create_or_update_lb_resources_and_wait(lb_client, resource_type, function, kwargs_function, module,
                                           get_fn, get_param=None, states=None, wait_applicable=True, kwargs_get=None):
    result = dict(resource_type='')
    response = oci_utils.call_with_backoff(function, **kwargs_function)
    work_request_id = response.headers.get('opc-work-request-id')
    if wait_applicable and module.params.get('wait', None):
        if states is None:
            states = module.params.get('wait_until') or DEFAULT_COMPLETED_STATES
        work_request_response = oci_utils.call_with_backoff(lb_client.get_work_request, work_request_id=work_request_id)
        response = oci.wait_until(lb_client, work_request_response,
                                  evaluate_response=lambda r: r.data.lifecycle_state in states,
                                  max_wait_seconds=module.params.get('wait_timeout', MAX_WAIT_TIMEOUT_IN_SECONDS))
        if response.data.lifecycle_state == 'FAILED':
            raise ClientError(Exception(response.data.error_details))
        if kwargs_get:
            result[resource_type] = to_dict(oci_utils.call_with_backoff(get_fn, **kwargs_get).data)
        else:
            result[resource_type] = to_dict(oci_utils.call_with_backoff(
                get_fn, **{get_param: response.data[get_param]}).data)
    result['changed'] = True
    return result


def get_existing_load_balancer(lb_client, module, load_balancer_id):
    existing_lb = None
    if load_balancer_id is None:
        raise ClientError(
            Exception("load_balancer_id is mandatory for update and delete use cases \
                      and must not be empty"))
    try:
        response = lb_client.get_load_balancer(load_balancer_id)
        existing_lb = response.data
    except ServiceError as ex:
        if ex.status != 404:
            module.fail_json(msg=ex.message)
    return existing_lb


def create_listeners(listener_details_dict):
    if listener_details_dict is None:
        return None
    result_listeners = dict()
    attributes = ['default_backend_set_name', 'port', 'protocol']
    for key, value in six.iteritems(listener_details_dict):
        listener_details = ListenerDetails()
        for attribute in attributes:
            if value.get(attribute) is None:
                raise ClientError(
                    Exception(attribute + " is mandatory and must not be empty for listener"))
            listener_details.__setattr__(attribute, value.get(attribute))
        listener_details.ssl_configuration = create_ssl_configuration(
            value.get('ssl_configuration', None))
        listener_details.connection_configuration = create_connection_configuration(
            value.get('connection_configuration', None))
        result_listeners.update({key: listener_details})
    return result_listeners


def create_certificates(certificate_details_dict):
    if certificate_details_dict is None:
        return None
    result_certificates = dict()
    attributes = ['ca_certificate', 'private_key', 'public_certificate']
    for key, value in six.iteritems(certificate_details_dict):
        certificate_details = CertificateDetails()
        certificate_name = value.get('certificate_name')
        if certificate_name is None:
            raise ClientError(
                Exception("certificate_name is mandatory and must not be empty for certificate creation"))
        certificate_details.certificate_name = certificate_name
        certificate_details.passphrase = value.get('passphrase', None)
        for attribute in attributes:
            if value.get(attribute) is not None:
                certificate_details.__setattr__(attribute, get_file_content(
                    value.get(attribute, None)))
        result_certificates.update({key: certificate_details})
    return result_certificates


def create_backend_sets(backend_sets_dicts):
    if backend_sets_dicts is None:
        return None
    result_backend_sets = dict()
    for key, value in six.iteritems(backend_sets_dicts):
        backend_sets_details = BackendSetDetails()
        health_checker = value.get('health_checker', None)
        policy = value.get('policy', None)
        if health_checker is None or policy is None:
            raise ClientError(Exception(
                "health_checker and policy are mandatory attributes for back_end_sets and can not be empty."))
        backend_sets_details.policy = value['policy']
        backend_sets_details.health_checker = create_health_checker(
            health_checker)
        backend_sets_details.backends = create_backends(
            value.get('backends', None))
        backend_sets_details.session_persistence_configuration = \
            create_session_persistence_configuration(
                value.get('session_persistence_configuration', None))
        backend_sets_details.ssl_configuration = create_ssl_configuration(
            value.get('ssl_configuration', None))
        result_backend_sets.update({key: backend_sets_details})
    return result_backend_sets


def create_backends(backends_list):
    if backends_list is None:
        return None
    result_backends = list()
    attribute_to_default_value_dict = dict(
        {'backup': False, 'drain': False, 'offline': False, 'weight': 1})
    HashedBackendDetails = oci_utils.generate_subclass(BackendDetails)
    for backend_entry in backends_list:
        backend = HashedBackendDetails()
        ip_address = backend_entry.get('ip_address', None)
        port = backend_entry.get('port', None)
        if ip_address is None or port is None:
            raise ClientError(Exception(
                "ip_address and port are mandatory attributes for back_ends and \
                 can not be empty."))
        backend.ip_address = ip_address
        backend.port = port
        for key, value in six.iteritems(attribute_to_default_value_dict):
            backend.__setattr__(
                key, backend_entry.get(key, value))
        result_backends.append(backend)
    return result_backends


def create_health_checker(health_checker_details):
    if health_checker_details is None:
        return None
    HashedHealthCheckerDetails = oci_utils.generate_subclass(
        HealthCheckerDetails)
    health_checker = HashedHealthCheckerDetails()
    attribute_to_default_value_dict = dict({'interval_in_millis': 10000, 'port': 0,
                                            'response_body_regex': '.*', 'retries': 3,
                                            'return_code': 200, 'timeout_in_millis': 3000})
    protocol = health_checker_details.get('protocol', None)
    url_path = health_checker_details.get('url_path', None)
    if protocol is None or url_path is None:
        raise ClientError(Exception(
            "protocol and url_path are mandatory attributes for health_checker and can not be empty."))
    health_checker.protocol = protocol
    health_checker.url_path = url_path
    for key, value in six.iteritems(attribute_to_default_value_dict):
        health_checker.__setattr__(
            key, health_checker_details.get(key, value))
    return health_checker


def create_session_persistence_configuration(session_persistence_configuration):
    if session_persistence_configuration is None:
        return None
    HashedSessionPersistenceConfigurationDetails = oci_utils.generate_subclass(
        SessionPersistenceConfigurationDetails)
    result_session_persistence_configuration = HashedSessionPersistenceConfigurationDetails()
    cookie_name = session_persistence_configuration.get('cookie_name')
    if cookie_name is None:
        raise ClientError(Exception(
            "cookie_name is mandatory attributes for session_persistence_configuration and \
                 can not be empty."))
    result_session_persistence_configuration.cookie_name = cookie_name
    result_session_persistence_configuration.disable_fallback = \
        session_persistence_configuration.get('disable_fallback', False)
    return result_session_persistence_configuration


def create_ssl_configuration(ssl_configuration_details):
    if ssl_configuration_details is None:
        return None
    HashedSSLConfigurationDetails = oci_utils.generate_subclass(
        SSLConfigurationDetails)
    result_ssl_configuration = HashedSSLConfigurationDetails()
    attributes = ['verify_depth', 'verify_peer_certificate']
    certificate_name = ssl_configuration_details.get('certificate_name')
    if certificate_name is None:
        raise ClientError(Exception(
            "certificate_name is mandatory attributes for ssl_configuration and \
                 can not be empty."))
    result_ssl_configuration.certificate_name = certificate_name
    for attribute in attributes:
        result_ssl_configuration.__setattr__(
            attribute, ssl_configuration_details.get(attribute))
    return result_ssl_configuration


def create_connection_configuration(connection_configuration_details):
    if connection_configuration_details is None:
        return None
    HashedConnectionConfiguration = oci_utils.generate_subclass(
        ConnectionConfiguration)
    result_connection_configuration = HashedConnectionConfiguration()
    idle_timeout = connection_configuration_details.get('idle_timeout')
    if idle_timeout is None:
        raise ClientError(Exception(
            "idle_timeout is mandatory attributes for connection_configuration and can not be empty."))
    result_connection_configuration.idle_timeout = idle_timeout
    return result_connection_configuration


def generic_hash(obj):
    """
    Compute a hash of all the fields in the object
    :param obj: Object whose hash needs to be computed
    :return: a hash value for the object
    """
    sum = 0
    for field in obj.attribute_map.keys():
        sum = sum + hash(getattr(obj, field))
    return sum


def generic_eq(s, other):
    if other is None:
        return False
    return s.__dict__ == other.__dict__


def generate_subclass(parent_class):
    """Make a class hash-able by generating a subclass with a __hash__ method that returns the sum of all fields within
    the parent class"""
    dict_of_method_in_subclass = {
        "__init__": parent_class.__init__,
        "__hash__": generic_hash,
        "__eq__": generic_eq
    }
    subclass_name = "GeneratedSub" + parent_class.__name__
    generated_sub_class = type(
        subclass_name, (parent_class,), dict_of_method_in_subclass)
    return generated_sub_class
