# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
from nose.plugins.skip import SkipTest
import logging
from ansible.modules.cloud.oracle import oci_load_balancer
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    import oci
    from oci.util import to_dict
    from oci.load_balancer.models import LoadBalancer, WorkRequest
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_load_balancer.py requires `oci` module")


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
def oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, 'wait_until')


@pytest.fixture()
def list_all_resources_patch(mocker):
    return mocker.patch.object(oci_utils, 'list_all_resources')


@pytest.fixture()
def get_existing_load_balancer_patch(mocker):
    return mocker.patch.object(oci_lb_utils, 'get_existing_load_balancer')


@pytest.fixture()
def create_load_balancer_patch(mocker):
    return mocker.patch.object(oci_load_balancer, 'create_load_balancer')


@pytest.fixture()
def update_load_balancer_patch(mocker):
    return mocker.patch.object(oci_load_balancer, 'update_load_balancer')


@pytest.fixture()
def check_and_create_resource_patch(mocker):
    return mocker.patch.object(oci_utils, 'check_and_create_resource')

@pytest.fixture()
def get_existing_resource_patch(mocker):
    return mocker.patch.object(oci_utils, 'get_existing_resource')

def setUpModule():
    logging.basicConfig(filename='/tmp/oci_ansible_module.log',
                        filemode='a', level=logging.INFO)
    oci_load_balancer.set_logger(logging)


def test_create_or_update_lb_create(lb_client, check_and_create_resource_patch):
    module = get_module(dict())
    load_balancer = get_load_balancer()
    check_and_create_resource_patch.return_value = {'load_balancer': to_dict(load_balancer), 'changed': True}
    result = oci_load_balancer.create_or_update_lb(lb_client, module)
    assert result['load_balancer']['id'] == load_balancer.id


def test_create_or_update_lb_update(lb_client, get_existing_resource_patch, update_load_balancer_patch):
    module = get_module(dict(load_balancer_id='ocid1.loadbalancer..xdvf'))
    load_balancer = get_load_balancer()
    get_existing_resource_patch.return_value = load_balancer
    update_load_balancer_patch.return_value = True, load_balancer
    result = oci_load_balancer.create_or_update_lb(lb_client, module)
    assert result['load_balancer']['id'] == load_balancer.id


def test_create_or_update_lb_service_error(lb_client, get_existing_resource_patch, update_load_balancer_patch):
    error_message = 'Internal Server Error'
    module = get_module(dict(load_balancer_id='ocid1.loadbalancer..xdvf'))
    load_balancer = get_load_balancer()
    get_existing_resource_patch.return_value = load_balancer
    update_load_balancer_patch.side_effect = ServiceError(
        500, 'InternalServerError', dict(), error_message)
    try:
        oci_load_balancer.create_or_update_lb(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]


def test_create_load_balancer(lb_client, oci_wait_until_patch):
    module = get_module(dict())
    work_request_response_header = dict(
        {'opc-work-request-id': 'ABE00987F'})
    work_request = WorkRequest()
    work_request.load_balancer_id = 'ocid.loadbalancer.cvghs'
    work_request.lifecycle_state = 'SUCCEEDED'
    lb_client.create_load_balancer.return_value = get_response(
        204, work_request_response_header, work_request, None)
    lb_client.get_work_request.return_value = get_response(
        200, None, work_request, None)
    load_balancer = LoadBalancer()
    load_balancer.id = 'ocid.loadbalancer.cvghs'
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None)
    result = oci_load_balancer.create_load_balancer(lb_client, module)
    assert result['load_balancer']['id'] == load_balancer.id


def test_update_load_balancer(lb_client, oci_wait_until_patch):
    module = get_module(dict())
    work_request_response_header = dict(
        {'opc-work-request-id': 'ABE00987F'})
    work_request = WorkRequest()
    work_request.load_balancer_id = 'ocid.loadbalancer.cvghs'
    work_request.lifecycle_state = 'SUCCEEDED'
    lb_client.update_load_balancer.return_value = get_response(
        204, work_request_response_header, work_request, None)
    lb_client.get_work_request.return_value = get_response(
        200, None, work_request, None)
    load_balancer = LoadBalancer()
    load_balancer.id = 'ocid.loadbalancer.cvghs'
    load_balancer.display_name = 'ansible_lb_updated'
    lb_client.get_load_balancer.return_value = get_response(
        200, None, load_balancer, None)
    changed, result = oci_load_balancer.update_load_balancer(
        lb_client, module, load_balancer)
    assert result.display_name == load_balancer.display_name


def test_delete_load_balancer(lb_client, get_existing_resource_patch, oci_wait_until_patch):
    module = get_module(dict())
    work_request_response_header = dict(
        {'opc-work-request-id': 'ABE00987F'})
    work_request = WorkRequest()
    work_request.load_balancer_id = 'ocid.loadbalancer.cvghs'
    lb_client.delete_load_balancer.return_value = get_response(
        204, work_request_response_header, work_request, None)
    load_balancer = get_load_balancer()
    get_existing_resource_patch.return_value = load_balancer
    result = oci_load_balancer.delete_load_balancer(lb_client, module)
    assert result['changed'] is True


def test_delete_load_balancer_no_existing_lb(lb_client, get_existing_resource_patch):
    module = get_module(dict())
    get_existing_resource_patch.side_effect = ServiceError(
        404, 'NotFound', dict(), None)
    result = oci_load_balancer.delete_load_balancer(lb_client, module)
    assert result['changed'] is False


def test_delete_load_balancer_service_error(lb_client, get_existing_resource_patch):
    error_message = 'Internal Server Error'
    module = get_module(dict())
    get_existing_resource_patch.side_effect = ServiceError(
        500, 'InternalServerError', dict(), error_message)
    try:
        oci_load_balancer.delete_load_balancer(lb_client, module)
    except Exception as ex:
        assert error_message in ex.args[0]

def get_load_balancer():
    load_balancer = LoadBalancer()
    load_balancer.id = 'ocid.loadbalancer.cvghs'
    load_balancer.display_name = 'ansible_lb'
    return load_balancer

def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module(additional_properties):
    params = {"compartment_id": "ocid1.compartment.oc1..aaaaaaaa",
              "display_name": "ansible_lb",
              "is_private": "False",
              "id": "ocid1.loadbalancer.xxcf",
              "backend_sets": {
                  "backend1": {
                      "backends": [
                          {
                              "ip_address": "10.159.34.21",
                              "port": "8080"
                          }
                      ],
                      "health_checker": {
                          "interval_in_millis": "30000",
                          "port": "8080",
                          "protocol": "HTTP",
                          "response_body_regex": "^(500|40[1348])$",
                          "retries": "3",
                          "timeout_in_millis": "6000",
                          "return_code": "200",
                          "url_path": "/healthcheck"
                      },
                      "policy": "LEAST_CONNECTIONS"
                  },
                  "backend2": {
                      "backends": [
                          {
                              "ip_address": "10.159.34.22",
                              "port": "8080"
                          }
                      ],
                      "health_checker": {
                          "interval_in_millis": "30000",
                          "port": "8080",
                          "protocol": "HTTP",
                          "response_body_regex": "^(500|40[1348])$",
                          "retries": "3",
                          "timeout_in_millis": "6000",
                          "return_code": "200",
                          "url_path": "/healthcheck"
                      },
                      "policy": "LEAST_CONNECTIONS"
                  }
              },
              "shape_name": "100Mbps",
              "listeners": {"listerner1": {"default_backend_set_name": "backend2", "port": "80", "protocol": "HTTP", "connection_configuration": {"idle_timeout": 1200}}},
              "subnet_ids": [
                  "ocid1.subnet.oc1.iad.aaaaaaaar",
                  "ocid1.subnet.oc1.iad.aaaaaaaau"
              ],
              "state": "present"
              }
    params.update(additional_properties)
    module = FakeModule(**params)
    return module
