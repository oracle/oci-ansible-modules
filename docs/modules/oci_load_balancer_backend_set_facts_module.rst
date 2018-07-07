.. _oci_load_balancer_backend_set_facts:


oci_load_balancer_backend_set_facts - Fetches details of backend set(s) that are associated with a load balancer
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Fetches details of all backend sets, or a specific backend set, that are associated with a load balancer.



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
    <td>DEFAULT</td>
    <td></td>
    <td>
        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
    </td>
    </tr>

    <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer where the Backend Set belongs</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the Backend Set</div>
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

    
    #Fetch Load Balancer Backend Set
    - name: List all backend sets that are associated with a load balancer
      oci_load_balancer_backend_facts:
          load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'


    #Fetch specific Load Balancer Backend Set
    - name: List a specific Load Balancer Backend Set
      oci_load_balancer_backend_set_facts:
           name: 'ansible_backend_set'
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
    <td>backend_sets</td>
    <td>
        <div>Attributes of the  Load Balancer Backend Set.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>[{'ssl_configuration': {'certificate_name': 'certs1', 'verify_depth': 3, 'verify_peer_certificate': True}, 'backends': [{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}, {'drain': False, 'name': '10.159.34.21:8282', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8282}], 'health_checker': {'retries': 3, 'protocol': 'HTTP', 'response_body_regex': '^(500|40[1348])$', 'return_code': 500, 'timeout_in_millis': 6000, 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080}, 'name': 'backend_set_1', 'policy': 'IP_HASH', 'session_persistence_configuration': {'cookie_name': 'first_backend_set_cookie_updated', 'disable_fallback': True}}]</td>
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
        <td>ssl_configuration</td>
        <td>
            <div>The load balancer's SSL handling configuration details.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'certificate_name': 'certs1', 'verify_depth': 1, 'verify_peer_certificate': True}</td>
        </tr>

        <tr>
        <td>backends</td>
        <td>
            <div>A list of configurations related to Backends that are part of the backend set</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>[{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}, {'drain': False, 'name': '10.159.34.21:8282', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8282}]</td>
        </tr>

        <tr>
        <td>health_checker</td>
        <td>
            <div>Health check policy for a backend set.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'retries': 3, 'protocol': 'HTTP', 'response_body_regex': '^(500|40[1348])$', 'return_code': 200, 'timeout_in_millis': 6000, 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080}</td>
        </tr>

        <tr>
        <td>name</td>
        <td>
            <div>Name assigned to the Load Balancer Backend Set during creation</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_backend_set</td>
        </tr>

        <tr>
        <td>policy</td>
        <td>
            <div>The load balancer policy for the backend set.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>LEAST_CONNECTIONS</td>
        </tr>

        <tr>
        <td>session_persistence_configuration</td>
        <td>
            <div>The configuration details for implementing session persistence</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'cookie_name': 'first_backend_set_cookie', 'disable_fallback': True}</td>
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
