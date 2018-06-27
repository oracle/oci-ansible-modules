.. _oci_load_balancer_work_request_facts:


oci_load_balancer_work_request_facts - Fetch details of all work_requests of a load balancer
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetch details of all work_requests of a load balancer.



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
    <td></td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
    </td>
    </tr>

    <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer to which the Work Requests belongs. Mutually exclusive with work_request_id.</div>
        </br><div style="font-size: small;">aliases: id</div>
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
    <td>tenancy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
    </td>
    </tr>

    <tr>
    <td>work_request_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Work Request whose details needs to be fetched.</div>
    </td>
    </tr>

    </table>
    </br>

Examples
--------

 ::

    
    #Fetch details of all Work Request of a Load Balancer
    - name: List all Work Requests
      oci_load_balancer_work_request_facts:
          load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

    #Fetch details of a specific Work Request in a Load Balancer
    - name: List a specific Work Request
      oci_load_balancer_work_request_facts:
          work_request_id: 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx'


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
    <td>work_requests</td>
    <td>
        <div>Attributes of the Work Requests fecthed.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'SUCCEEDED', 'time_finished': '2018-06-22T09:02:54.687000+00:00', 'time_accepted': '2018-06-22T09:02:38.505000+00:00', 'error_details': [], 'load_balancer_id': 'ocid1.loadbalancer..aaaa', 'message': {'eventId': '43644f81-8724-44b0-a13', 'workRequestId': 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx', 'workflowName': 'AddHostnameWorkflow', 'loadBalancerId': 'ocid1.loadbalancer..aaaa', 'message': 'OK', 'type': 'SUCCESS'}, 'type': 'CreateHostname', 'id': 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx'}, {'lifecycle_state': 'SUCCEEDED', 'time_finished': '2018-06-22T09:06:10.111000+00:00', 'time_accepted': '2018-06-22T09:05:56.508000+00:00', 'error_details': [], 'load_balancer_id': 'ocid1.loadbalancer..aaaa', 'message': {'eventId': '43644f81-8724-44b0-a13', 'workRequestId': 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx', 'workflowName': 'AddHostnameWorkflow', 'loadBalancerId': 'ocid1.loadbalancer..aaaa', 'message': 'OK', 'type': 'SUCCESS'}, 'type': 'CreateHostname', 'id': 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx'}]</td>
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
            <div>The current state of the Load Balancer</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ACCEPTED</td>
        </tr>

        <tr>
        <td>time_finished</td>
        <td>
            <div>The date and time the work request was completed, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2018-06-26T21:112:29.600Z</td>
        </tr>

        <tr>
        <td>time_accepted</td>
        <td>
            <div>The date and time the work request was created, in the format defined by RFC3339.</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2018-06-26 21:10:29.600000</td>
        </tr>

        <tr>
        <td>error_details</td>
        <td>
            <div>Error details of the work request</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'errorCode': 'BAD_INPUT', 'message': "Default Listener on port '80' refer to VIP 'private-vip' twice"}]</td>
        </tr>

        <tr>
        <td>load_balancer_id</td>
        <td>
            <div>The OCID of the load balancer the Work Request is associated with.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>message</td>
        <td>
            <div>A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure. Possible data elements include - workflow name - event ID - work request ID - load balancer ID - workflow completion message</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>{'eventId': '43644f81-8724-1324', 'workRequestId': 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx', 'workflowName': 'AddHostnameWorkflow', 'loadBalancerId': 'ocid1.loadbalancer..aaaa', 'message': 'OK', 'type': 'SUCCESS'}</td>
        </tr>

        <tr>
        <td>type</td>
        <td>
            <div>The type of action the work request represents.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>CreateListener</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Work Request</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.loadbalancerworkrequest.oc1.axdf</td>
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

    * Debayan Gupta(@debayan_gupta)




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



For help in developing on modules, should you be so inclined, please read :doc:`../../community`, :doc:`../../dev_guide/testing` and :doc:`../../dev_guide/developing_modules`.
