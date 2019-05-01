:source: cloud/oracle/oci_waas_work_request_facts.py

:orphan:

.. _oci_waas_work_request_facts_module:


oci_waas_work_request_facts - Retrieve details about WAAS policy work requests.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This module retrieves information of a specific work request or lists all the work requests in the given WAAS policy and compartment.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- python >= 2.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <b>api_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user's OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_fingerprint</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair's fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_user_key_pass_phrase</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>auth_type</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this 'auth_type' module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the compartment.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_file_location</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_profile_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>region</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_by</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>id</li>
                                                                                                                                                                                                <li>status</li>
                                                                                                                                                                                                <li>timeAccepted</li>
                                                                                                                                                                                                <li>timeStarted</li>
                                                                                                                                                                                                <li>timeFinished</li>
                                                                                                                                                                                                <li>operationType</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The value by which work requests are sorted in a paginated 'List' call. If unspecified, defaults to timeAccepted.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_order</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>ASC</li>
                                                                                                                                                                                                <li>DESC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The order in which to sort the results.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tenancy</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>waas_policy_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the WAAS policy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>work_request_id</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the work request. Required to retrieve a specific work request.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get all the work requests for a waas policy in a compartment
      oci_waas_work_request_facts:
        waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

    - name: Get all the work requests for a waas policy in a compartment sorted by timeFinished
      oci_waas_work_request_facts:
        waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        sort_by: timeFinished

    - name: Get a specific waas work request using its OCID
      oci_waas_work_request_facts:
        work_request_id: ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <b>waas_work_requests</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of work requests</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{'status': 'IN_PROGRESS', 'time_finished': None, 'errors': [], 'logs': [{'timestamp': '2019-04-10T18:46:05.663000+00:00', 'message': 'addWhitelistOp: start'}, {'timestamp': '2019-04-10T18:46:05.663000+00:00', 'message': 'addWhitelistOp: finished (45% of request completed)'}, {'timestamp': '2019-04-10T18:46:05.403000+00:00', 'message': 'updateProtectionSettingsOp: start'}], 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'operation_type': 'CREATE_WAAS_POLICY', 'percent_complete': 45, 'time_accepted': '2019-04-10T18:45:45.044000+00:00', 'id': 'ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx', 'resources': [{'entity_uri': '/20181116/waasPolicies/ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx', 'identifier': 'ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx', 'action_type': 'CREATED', 'entity_type': 'waas'}], 'time_started': '2019-04-10T18:45:49+00:00'}]</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>status</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The current status of the work request.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">IN_PROGRESS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_finished</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The date and time the work request was fulfilled or terminated, expressed in RFC 3339 timestamp format.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2019-03-22 13:02:59.563000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>errors</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The list of errors that occurred while fulfilling the work request.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>logs</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The list of log entries from the work request workflow.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{'timestamp': '2019-04-10T19:31:57.364000+00:00', 'message': 'Work request complete'}, {'timestamp': '2019-04-10T19:31:57.360000+00:00', 'message': 'PersistWaasOp: start (100% of request completed)'}, {'timestamp': '2019-04-10T19:31:57.261000+00:00', 'message': 'Starting Work Request'}]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>compartment_id</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The OCID of the compartment that contains the work request.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>operation_type</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>A description of the operation requested by the work request.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATE_WAAS_POLICY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>percent_complete</b>
                    <br/><div style="font-size: small; color: red">int</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The percentage of work completed by the work request.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">50</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_accepted</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The date and time the work request was created, in the format defined by RFC3339.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2019-03-22 13:02:55.563000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>id</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The OCID of the work request.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>resources</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The resources being used to complete the work request operation.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{'entity_uri': '/20181116/waasPolicies/ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx', 'identifier': 'ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx', 'action_type': 'CREATED', 'entity_type': 'waas'}]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_started</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The date and time the work request moved from the ACCEPTED state to the IN_PROGRESS state, expressed in RFC 3339 timestamp format.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2019-03-22 13:02:56.563000</div>
                                    </td>
            </tr>
                    
                                        </table>
    <br/><br/>


Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



Author
~~~~~~

- Manoj Meda (@manojmeda)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_waas_work_request_facts.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
