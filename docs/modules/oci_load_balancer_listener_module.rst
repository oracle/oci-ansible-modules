.. _oci_load_balancer_listener:


oci_load_balancer_listener - Add, modify and remove a listener from a backend set of a load balancer in OCI Load Balancing Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.x




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Add a listener to a backend set in a OCI Load Balancer
* Update a listener in a Load Balancer, if present, with any changed attribute
* Delete a listener from OCI Load Balancer Backends, if present.



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
    <td rowspan="2">connection_configuration<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Configuration details for the connection between the client and backend servers.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object connection_configuration</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>idle_timeout<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>default_backend_set_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the associated backend set. Mandatory for create and update.</div>
    </td>
    </tr>

    <tr>
    <td>hostname_names<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>An array of hostname resource names.</div>
    </td>
    </tr>

    <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer in which the listener belongs.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the listener. It must be unique and it cannot be changed. Mandatory field for all use cases.</div>
    </td>
    </tr>

    <tr>
    <td>path_route_set_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the set of path-based routing rules, PathRouteSet, applied to this listener's traffic.</div>
    </td>
    </tr>

    <tr>
    <td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The communication port for the listener. Mandatory for create and update.</div>
    </td>
    </tr>

    <tr>
    <td>protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The protocol on which the listener accepts connection requests. Mandatory for create and update.</div>
    </td>
    </tr>

    <tr>
    <td>purge_hostname_names<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Purge any Hostname names in the  Listener named <em>name</em> that is not specified in <em>hostname_names</em>. This is only applicable in case of updating Listener.If <em>purge_hostname_names=no</em>, provided <em>hostname_names</em> would be appended to existing <em>hostname_names</em>.</div>
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
    <td rowspan="2">ssl_configuration<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The load balancer SSL handling configuration details</div>
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
        <div>A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters,dashes, and underscores.Certificate bundle names cannot contain spaces.</div>
        </td>
        </tr>

        <tr>
        <td>verify_depth<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The maximum depth for peer certificate chain verification.</div>
        </td>
        </tr>

        <tr>
        <td>verify_peer_certificate<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Whether the load balancer listener should verify peer certificates.</div>
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
        <div>Create,update or delete Load Balancer Backend. For <em>state=present</em>, if it does not exists, it gets added. If exists, it gets updated.</div>
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
    # Create Listener
    - name: Create Listener
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        default_backend_set_name: "ansible_backend_set"
        protocol: "HTTP"
        port: 80
        ssl_configuration:
            certificate_name: 'certs1'
            verify_depth: 1
            verify_peer_certificate: True
        connection_configuration:
            idle_timeout: 1200
        hostname_names: ['hostname_001']
        path_route_set_name: 'path_route_set_001'
        state: 'present'
    # Update Listener
    - name: Update Listener Port
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        default_backend_set_name: "ansible_backend_set"
        protocol: "HTTP"
        port: 82
        state: 'present'

    - name: Update Listener's SSL Configuration
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        default_backend_set_name: "ansible_backend_set"
        protocol: "HTTP"
        port: 80
        ssl_configuration:
            certificate_name: 'certs2'
            verify_depth: 2
            verify_peer_certificate: False
        state: 'present'

    - name: Update Listener's Connection Configuration
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        default_backend_set_name: "ansible_backend_set"
        protocol: "HTTP"
        port: 80
        connection_configuration:
            idle_timeout: 1200
        state: 'present'

    - name: Update Listener's Hostname Names by appending new name
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        hostname_names: ['hostname_002']
        purge_hostname_names: False
        state: 'present'

    - name: Update Listener's Hostname Names by replacing existing names
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        hostname_names: ['hostname_002']
        purge_hostname_names: True
        state: 'present'

    - name: Update Listener's Path Route Set Name
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
        path_route_set_name: 'path_route_set_002'
        state: 'present'

    # Delete listener
    - name: Delete Listener
      oci_load_balancer_listener:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_listener"
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
    <td>listener</td>
    <td>
        <div>Attributes of the created/updated Listener. For delete, deleted Listener description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'path_route_set_name': 'path_route_set_001', 'protocol': 'HTTP', 'name': 'ansible_listener', 'connection_configuration': {'idle_timeout': 1200}, 'ssl_configuration': {'certificate_name': 'certs1', 'verify_depth': 1, 'verify_peer_certificate': True}, 'hostname_names': ['hostname_001'], 'default_backend_set_name': 'ansible_backend', 'port': 87}</td>
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
        <td>path_route_set_name</td>
        <td>
            <div>The name of the set of path-based routing rules, PathRouteSet, applied to this listener's traffic.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>path_route_set_001</td>
        </tr>

        <tr>
        <td>protocol</td>
        <td>
            <div>The protocol on which the listener accepts connection requests.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>HTTP</td>
        </tr>

        <tr>
        <td>name</td>
        <td>
            <div>Name of the Listener</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_listener</td>
        </tr>

        <tr>
        <td>connection_configuration</td>
        <td>
            <div>Configuration details for the connection between the client and backend servers.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'idle_timeout': 1200}</td>
        </tr>

        <tr>
        <td>ssl_configuration</td>
        <td>
            <div>The load balancer SSL handling configuration details</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'certificate_name': 'certs1', 'verify_depth': 1, 'verify_peer_certificate': True}</td>
        </tr>

        <tr>
        <td>hostname_names</td>
        <td>
            <div>An array of hostname resource names.</div>
        </td>
        <td align=center>always</td>
        <td align=center>list</td>
        <td align=center>['hostname_001']</td>
        </tr>

        <tr>
        <td>default_backend_set_name</td>
        <td>
            <div>The name of the associated backend set</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_backend_set</td>
        </tr>

        <tr>
        <td>port</td>
        <td>
            <div>The communication port for the listener.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>80</td>
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
