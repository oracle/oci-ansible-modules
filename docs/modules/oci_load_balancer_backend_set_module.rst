.. _oci_load_balancer_backend_set:


oci_load_balancer_backend_set - Create, update and delete a backend set of a load balancer.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Create an OCI Load Balancer Backend Set
* Update OCI Load Balancers Backend Set, if present.
* Delete OCI Load Balancers Backend Set, if present.



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
    <td rowspan="2">backends<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>A list of configurations related to Backends that are part of a backend set.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object backends</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>drain<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Specifies whether the load balancer should drain this server. Servers marked &quot;drain&quot; receive no new incoming traffic.</div>
        </td>
        </tr>

        <tr>
        <td>weight<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>1</td>
        <td></td>
        <td>
        <div>Describes the load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'.</div>
        </td>
        </tr>

        <tr>
        <td>backup<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Specifies whether the load balancer should treat this server as a backup unit. If true, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as &quot;backup&quot; fail the health check policy.</div>
        </td>
        </tr>

        <tr>
        <td>offline<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Ensures whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.</div>
        </td>
        </tr>

        <tr>
        <td>ip_address<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>IP address of the backend server.</div>
        </td>
        </tr>

        <tr>
        <td>port<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The communication port for the backend server</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
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
    <td rowspan="2">health_checker<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Describes the health check policy for a backend set.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object health_checker</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>retries<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>3</td>
        <td></td>
        <td>
        <div>Describes the number of retries to attempt before a backend server is considered unhealthy.</div>
        </td>
        </tr>

        <tr>
        <td>protocol<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td><ul><li>HTTP</li><li>TCP</li></ul></td>
        <td>
        <div>Describes the protocol the health check must use, either HTTP or TCP.</div>
        </td>
        </tr>

        <tr>
        <td>response_body_regex<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>.*</td>
        <td></td>
        <td>
        <div>Describes a regular expression for parsing the response body from the backend server.</div>
        </td>
        </tr>

        <tr>
        <td>return_code<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>200</td>
        <td></td>
        <td>
        <div>Describes the status code a healthy backend server should return.</div>
        </td>
        </tr>

        <tr>
        <td>timeout_in_millis<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>3000</td>
        <td></td>
        <td>
        <div>Describes the maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period.</div>
        </td>
        </tr>

        <tr>
        <td>interval_in_millis<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>10000</td>
        <td></td>
        <td>
        <div>Describes the interval between health checks, in milliseconds.</div>
        </td>
        </tr>

        <tr>
        <td>url_path<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes the path against which to run the health check.</div>
        </td>
        </tr>

        <tr>
        <td>port<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes the backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the backends.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer. Mandatory for create,delete and update.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the Load Balancer Backend Set. A user friendly name. Does not have to be unique, and could be changed. Mandatory for create and update.</div>
    </td>
    </tr>

    <tr>
    <td>policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The load balancer policy for the backend set. <span class='module'>oci_load_balancer_policy_facts</span> could be used to fetch policy types suupported by OCI Load Balancer Service.</div>
    </td>
    </tr>

    <tr>
    <td>purge_backends<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Purge any backends in the  Backend Set named <em>name</em> that is not specified in <em>backends</em>. If <em>purge_backends=no</em>, provided backends would be appended to existing backends.</div>
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
    <td rowspan="2">session_persistence_configuration<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The configuration details for implementing session persistence. Session persistence enables the Load Balancing Service to direct any number of requests that originate from a single logical client to a single backend web server.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object session_persistence_configuration</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>cookie_name<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes the name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist.</div>
        </td>
        </tr>

        <tr>
        <td>disable_fallback<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>DescribesWhether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td rowspan="2">ssl_configuration<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The load balancer's SSL handling configuration details.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object ssl_configuration</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>certificate_name<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes a friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.Certificate bundle names cannot contain spaces.</div>
        </td>
        </tr>

        <tr>
        <td>verify_depth<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes the maximum depth for peer certificate chain verification.</div>
        </td>
        </tr>

        <tr>
        <td>verify_peer_certificate<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Describeswhether the load balancer listener should verify peer certificates.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create,update or delete Load Balancer Backend Set. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
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

    
    # Note: These examples do not set authentication details.
    # Create Create a backend set named "ansible_backend_set" in a load balancer
    - name: Create Load Balancer Backend Set
      oci_load_balancer_backend_set:
        name: "ansible_backend_set"
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        backends:
              - ip_address: "10.159.34.21"
                port: 8080
        health_checker:
              interval_in_millis: 30000
              port: 8080
              protocol: "HTTP"
              response_body_regex: "^(500|40[1348])$"
              retries: 3
              timeout_in_millis: 6000
              return_code: 200
              url_path: "/healthcheck"
        policy: "LEAST_CONNECTIONS"
        session_persistence_configuration:
          cookie_name: "ansible_backend_set_cookie"
          disable_fallback: True
        ssl_configuration:
          certificate_name: "certs1"
          verify_depth: 3
          verify_peer_certificate: True
        state: 'present'

    # Update Load Balancer Backend Set
    - name: Update Load Balancer Backend Set
      oci_load_balancer_backend_set:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_backend_set"
        backends:
              - ip_address: "10.159.34.25"
                port: 8282
        purge_backends: 'no'
        state: 'present'
    # Deleted Load Balancer Backend Set
    - name: Update Load Balancer Backend Set
      oci_load_balancer_backend_set:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_backend_set"
        state: 'absent'


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
    <td>backend_set</td>
    <td>
        <div>Attributes of the created/updated Load Balancer Backend Set. For delete, deleted Load Balancer Backend Set description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'ssl_configuration': {'certificate_name': 'certs1', 'verify_depth': 1, 'verify_peer_certificate': True}, 'backends': [{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}, {'drain': False, 'name': '10.159.34.21:8282', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8282}], 'health_checker': {'retries': 3, 'protocol': 'HTTP', 'response_body_regex': '^(500|40[1348])$', 'return_code': 500, 'timeout_in_millis': 6000, 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080}, 'name': 'backend_set_1', 'policy': 'IP_HASH', 'session_persistence_configuration': {'cookie_name': 'first_backend_set_cookie_updated', 'disable_fallback': True}}</td>
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
