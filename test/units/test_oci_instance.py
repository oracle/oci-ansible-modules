# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

import pytest
import logging

from nose.plugins.skip import SkipTest

from ansible.modules.cloud.oracle import oci_instance
#from ansible.module_utils.oracle.oci_utils import OCIRetry
from ansible.module_utils.oracle.oci_utils import to_dict

try:
    import oci
    from oci.object_storage.models import Bucket
    from ansible.module_utils.oracle import oci_utils
    from oci.exceptions import ServiceError
except ImportError:
    raise SkipTest("test_oci_bucket.py requires `oci` module")


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


def setup_module():
    logging.basicConfig(filename='/tmp/oci_ansible_module.log',
                        filemode='a', level=logging.INFO)
    oci_instance.set_logger(logging)


@pytest.fixture()
def compute_client(mocker):
    mock_cc = mocker.patch('oci.core.compute_client.ComputeClient')
    return mock_cc.return_value


def get_response(status, header, data, request):
    return oci.Response(status, header, data, request)


def get_module():
    params = {'name': 'myinstance1',
              'availability_domain': 'BnQb:PHX-AD-1',
              'compartment_id': 'ocid1.compartment.oc1.....vm62xq',
              'image_id': 'ocid1.image.oc1.phx....sa7klnoa',
              'fault_domain': 'FAULT-DOMAIN-1',
              'shape': 'BM.Standard1.36',
              'metadata': {'foo': 'bar'},
              'extended_metadata': {'baz': 'quux'},
              'ipxe_script': "",
              'vnic': {
                  'hostname_label': 'myinstance1',
                  'private_ip': '10.0.0.5',
                  'subnet_id': 'ocid1.subnet.oc1.phx....5iddusmpqpaoa'
              },
              "wait": True,
              "wait_timeout": 1200}
    module = FakeModule(**params)
    return module


@pytest.fixture()
def get_call_with_backoff(mocker):
    return mocker.patch.object(oci_utils, 'call_with_backoff')


@pytest.fixture()
def get_oci_wait_until_patch(mocker):
    return mocker.patch.object(oci, 'wait_until')


@pytest.fixture()
def get_ociretry_found_patch(mocker):
    return mocker.patch.object(OCIRetry, "found")

@pytest.fixture()
def get_oci_utils_create_and_wait_patch(mocker):
    return mocker.patch.object(oci_utils, "create_and_wait")


def test_launch_instance_success(compute_client, get_oci_utils_create_and_wait_patch):
    module = get_module()

    inst_created = oci.core.models.Instance()
    inst_created.display_name = module.params['name']
    inst_created.id = "XYZ"
    inst_created.lifecycle_state = "RUNNING"
    get_oci_utils_create_and_wait_patch.return_value = {"changed": True, "instance": to_dict(inst_created)}

    resp = oci_instance.launch_instance(compute_client, module, None)
    assert resp['instance']['lifecycle_state'] == "RUNNING"


# XXX write a new UT to test the new RetryStrategy based retry logic
# def test_stop_running_instance_transient_failure(compute_client, get_oci_wait_until_patch, get_ociretry_found_patch):
#     """Test the retry scenario. Simulate a transient failure while making an API call, and see if the OCIRetry
#     decorator works"""
#     inst = oci.core.models.Instance()
#     running_resp = _get_running(inst)
#     stopped_resp = _get_stopped(inst)
#
#     # retryable errors
#     too_many_reqs = ServiceError("429", "TooManyRequests", {}, "You have issued too many requests to the Oracle Cloud "
#                                                                "Infrastructure APIs in too short of an amount of "
#                                                                "time.")
#     internal_server_error = ServiceError("500", "InternalServerError", {}, "An internal server error occurred. Try your"
#                                                                            "request again in a few minutes.")
#     conflict_error = ServiceError("409", "Conflict", {}, "Conflict")
#
#     # instance_action's returns three retryable service_errors before returning a response
#     compute_client.instance_action.side_effect = [too_many_reqs, internal_server_error, conflict_error,
#                                                   running_resp, stopped_resp]
#     # for get_instance intersperse retryable service errors between returning valid responses
#     compute_client.get_instance.side_effect = [too_many_reqs, running_resp, internal_server_error, running_resp,
#                                                conflict_error, stopped_resp]
#     get_oci_wait_until_patch.return_value = None
#
#     res = oci_instance.power_action_on_instance(compute_client, inst.id, "softreset", get_module())
#     assert res['changed']
#
#     ret_inst = res['instance']
#     # the desired state must be reached
#     assert ret_inst['lifecycle_state'] == 'STOPPED'
#
#     # OCIRetry's found() call count should equal number of Service Errors we are returning
#     # 3 errors during power action on instance and 3 errors during get
#     # instance
#     assert get_ociretry_found_patch.call_count == 6


def _get_running(inst):
    inst.id = 42
    inst.lifecycle_state = "RUNNING"
    running_resp = get_response(200, None, inst, None)
    return running_resp


def _get_stopped(inst):
    stopped = oci.core.models.Instance()
    stopped.id = inst.id
    stopped.lifecycle_state = "STOPPED"
    stopped_resp = get_response(200, None, stopped, None)
    return stopped_resp


def test_stop_running_instance_clean_first_response(compute_client, get_call_with_backoff, get_oci_wait_until_patch):
    inst = oci.core.models.Instance()
    running_resp = _get_running(inst)
    stopped_resp = _get_stopped(inst)

    # The last call to get_instance must return 'stopped'
    get_call_with_backoff.side_effect = [running_resp, running_resp, stopped_resp, stopped_resp]
    compute_client.get_instance.side_effect = [running_resp, running_resp, stopped_resp]
    get_oci_wait_until_patch.return_value = None

    # The 'state' option would be set to "stopped"
    res = oci_instance.power_action_on_instance(compute_client, inst.id, "stopped", get_module())

    # the action to take to reach the desired state must be STOP
    # compute_client.instance_action.assert_called_once_with(inst.id, "STOP")
    assert res['changed']  # there must be a change in state

    ret_inst = res['instance']
    # the desired state must be reached
    assert ret_inst['lifecycle_state'] == 'STOPPED'
