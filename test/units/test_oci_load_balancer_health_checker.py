# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer_health_checker
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.load_balancer.models import HealthChecker
    from oci.exceptions import ServiceError, ClientError
except ImportError:
    raise SkipTest("test_oci_load_balancer_health_checker.py requires `oci` module")


class FakeModule(object):
    def __init__(self, **kwargs):
        self.params = kwargs

    def fail_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs
        raise Exception(kwargs['msg'])

    def exit_json(self, *args, **kwargs):
        self.exit_args = args
        self.exit_kwargs = kwargs


@pytest.fixture()
def lb_client(mocker):
    mock_lb_client = mocker.patch(
        'oci.load_balancer.load_balancer_client.LoadBalancerClient')
    return mock_lb_client.return_value



@pytest.fixture()
def get_existing_health_checker_patch(mocker):
    return mocker.patch.object(oci_load_balancer_health_checker, 'get_existing_health_checker')


@pytest.fixture()
def verify_work_request_patch(mocker):
    return mocker.patch.object(oci_lb_utils, 'verify_work_request')

def setUpModule():
    logging.basicConfig(filename='/tmp/oci_ansible_module.log',
                        filemode='a', level=logging.INFO)
    oci_load_balancer_health_checker.set_logger(logging)


def test_update_health_checker(lb_client, verify_work_request_patch, get_existing_health_checker_patch):
    module = get_module()
    health_checker = get_health_checker()
    get_existing_health_checker_patch.return_value = health_checker
    lb_client.update_health_checker.return_value = get_response(204, None, health_checker, None)
    result = oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    assert result['changed'] is True

def test_update_health_checker_no_change(lb_client, verify_work_request_patch, get_existing_health_checker_patch):
    additional_properties = dict({'port': 82})
    module = get_module(additional_properties)
    health_checker = get_health_checker()
    get_existing_health_checker_patch.return_value = health_checker
    lb_client.update_health_checker.return_value = get_response(204, None, health_checker, None)
    result = oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    assert result['changed'] is False

def test_update_health_checker_service_error(lb_client, verify_work_request_patch, get_existing_health_checker_patch):
    error_message = "Internal Server Error"
    module = get_module()
    health_checker = get_health_checker()
    get_existing_health_checker_patch.return_value = health_checker
    lb_client.update_health_checker.side_effect = ServiceError(
        499, 'InternalServerError', dict(), error_message)
    try:
        oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]

def test_update_health_checker_client_error(lb_client, verify_work_request_patch, get_existing_health_checker_patch):
    error_message = 'Work Request Failed'
    module = get_module()
    health_checker = get_health_checker()
    get_existing_health_checker_patch.return_value = health_checker
    lb_client.update_health_checker.return_value = get_response(204, None, health_checker, None)
    verify_work_request_patch.side_effect = ClientError(Exception('Work Request Failed'))
    try:
        oci_load_balancer_health_checker.update_health_checker(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]

def test_get_existing_health_checker(lb_client):
    module = get_module()
    health_checker = get_health_checker()
    lb_client.get_health_checker.return_value = get_response(200, None, health_checker, None)
    result = oci_load_balancer_health_checker.get_existing_health_checker(
        lb_client, module, 'ocid1.loadbalancer.aaaa', 'backend_set')
    assert result.protocol == health_checker.protocol


def test_get_existing_health_checker_not_found(lb_client):
    module = get_module()
    health_checker = get_health_checker()
    lb_client.get_health_checker.side_effect = ServiceError(
        404, 'NotFound', dict(), None)
    result = oci_load_balancer_health_checker.get_existing_health_checker(
        lb_client, module, 'ocid1.loadbalancer.aaaa', 'backend_set')
    assert result is None

def test_get_existing_health_checker_service_error(lb_client):
    error_message = "Internal Server Error"
    module = get_module()
    lb_client.get_health_checker.side_effect = ServiceError(
        499, 'NotFound', dict(), error_message)
    try:
        oci_load_balancer_health_checker.get_existing_health_checker(
        lb_client, module, 'ocid1.loadbalancer.aaaa', 'backend_set')
    except Exception as ex:
        assert error_message in ex.args[0]


def get_health_checker():
    health_checker = HealthChecker()
    health_checker.interval_in_millis = 30000
    health_checker.port = 82
    health_checker.protocol = 'HTTP'
    health_checker.response_body_regex = '^(500|40[1348])$'
    health_checker.retries = 3
    health_checker.return_code = 200
    health_checker.timeout_in_millis = 6000
    health_checker.url_path = '/healthcheck'
    return health_checker

def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties=None):
    params = {
        "load_balancer_id" : "ocid1.loadbalancer.oc1.iad.aaaa",
        "backend_set_name" : "test_backend",
        "interval_in_millis":30000,
        "port":8080,
        "protocol":"HTTP",
        "retries":3,
        "timeout_in_millis":6000,
        "return_code":200,
        "url_path":"/healthcheck"
    }
    if additional_properties is not None:
        params.update(additional_properties)
    module = FakeModule(**params)
    return module