.. _oci_load_balancer_facts:


oci_load_balancer_facts - Fetches details of the OCI Load Balancer
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of the OCI Load Balancer.



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
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the compartment in which this Load Balancer exists</div>
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
    <td>DEFAULT</td>
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
        <div>Identifier of the Load Balancer whose details needs to be fetched.</div>
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

    </table>
    </br>

Examples
--------

 ::

    
    #Fetch Load Balancer
    - name: List Load Balancer
      oci_load_balancer_facts:
          compartment_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

    #Fetch specific Load Balancer
    - name: List a specific Load Balancer
      oci_load_balancer_facts:
          load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'


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
    <td>load_balancers</td>
    <td>
        <div>Attributes of the  Load Balancers.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'lifecycle_state': 'ACTIVE', 'display_name': 'ansible_lb955', 'shape_name': '100Mbps', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'ip_addresses': [{'is_public': True, 'ip_address': '129.213.72.32'}], 'time_created': '2018-01-06T18:22:17.198000+00:00', 'id': 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx', 'listeners': {'listener1': {'ssl_configuration': None, 'protocol': 'HTTP', 'name': 'listerner1', 'default_backend_set_name': 'backend1', 'connection_configuration': {'idle_timeout': 1200}, 'port': 80}}, 'certificates': {'certs1': {'certificate_name': 'certs1', 'public_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n- ----END CERTIFICATE-----', 'ca_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n-----END CERTIFICATE -----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----'}}, 'subnet_ids': ['ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx'], 'backend_sets': {'backend1': {'ssl_configuration': None, 'backends': [{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}], 'health_checker': {'retries': 3, 'protocol': 'HTTP', 'response_body_regex': '^(500|40[1348])$', 'return_code': 200, 'timeout_in_millis': 6000, 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080}, 'name': 'backend1', 'policy': 'LEAST_CONNECTIONS', 'session_persistence_configuration': None}}, 'path_route_sets': {'ansible_path_route_set': {'path_routes': [{'path': '/example/user', 'backend_set_name': 'ansible_backend_set', 'path_match_type': {'match_type': 'EXACT_MATCH'}}]}}, 'is_private': False}]</td>
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
        <td align=center>ACTIVE</td>
        </tr>

        <tr>
        <td>display_name</td>
        <td>
            <div>Name assigned to the Load Balancer during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_lb</td>
        </tr>

        <tr>
        <td>shape_name</td>
        <td>
            <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress).</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>100Mbps</td>
        </tr>

        <tr>
        <td>compartment_id</td>
        <td>
            <div>The identifier of the compartment containing the Load Balancer</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>time_created</td>
        <td>
            <div>Date and time when the Load Balancer was created, in the format defined by RFC3339</div>
        </td>
        <td align=center>always</td>
        <td align=center>datetime</td>
        <td align=center>2016-08-25 21:10:29.600000</td>
        </tr>

        <tr>
        <td>id</td>
        <td>
            <div>Identifier of the Load Balancer</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</td>
        </tr>

        <tr>
        <td>listeners</td>
        <td>
            <div>The listener configuration details.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'listerner1': {'ssl_configuration': None, 'protocol': 'HTTP', 'name': 'listerner1', 'default_backend_set_name': 'backend1', 'connection_configuration': {'idle_timeout': 1200}, 'port': 80}}</td>
        </tr>

        <tr>
        <td>certificates</td>
        <td>
            <div>The configuration details for a listener certificate bundle.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'certs1': {'certificate_name': 'certs1', 'public_certificate': '-----BEGIN CERTIFICATE----- MIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----', 'ca_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----'}}</td>
        </tr>

        <tr>
        <td>subnet_ids</td>
        <td>
            <div>An array of subnet OCIDs.</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>['ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx']</td>
        </tr>

        <tr>
        <td>backend_sets</td>
        <td>
            <div>The configuration details for a load balancer backend set</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'backend1': {'backends': [{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}], 'health_checker': {'retries': 3, 'protocol': 'HTTP', 'name': 'backend1', 'response_body_regex': '^(500|40[1348])$', 'return_code': 200, 'ssl_configuration': None, 'timeout_in_millis': 6000, 'policy': 'LEAST_CONNECTIONS', 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080, 'session_persistence_configuration': None}}}</td>
        </tr>

        <tr>
        <td>path_route_sets</td>
        <td>
            <div>The path route sets configuration details.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'ansible_path_route_set': {'path_routes': [{'path': '/example/user', 'backend_set_name': 'ansible_backend_set', 'path_match_type': {'match_type': 'EXACT_MATCH'}}]}}</td>
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
