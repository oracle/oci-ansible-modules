.. _oci_load_balancer:


oci_load_balancer - Create, update and delete load balancers in OCI Load Balancing Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Creates OCI Load Balancers
* Update OCI Load Balancers, if present, with a new display name
* Delete OCI Load Balancers, if present.



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
    <td rowspan="2">backend_sets<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The configuration details for a load balancer's backend sets</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object backend_sets</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>policy<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The load balancer policy for the backend set.</div>
        </td>
        </tr>

        <tr>
        <td>ssl_configuration<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The load balancer's SSL handling configuration details. This should be specified as a dict/hash with the following keys [certificate_name describes a friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.Certificate bundle names cannot contain spaces. required - true], ['verify_depth'  describes the maximum depth for peer certificate chain verification. required - false], ['verify_peer_certificate'  describes whether the load balancer listener should verify peer certificates. required - false]</div>
        </td>
        </tr>

        <tr>
        <td>backends<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A list of configurations related to Backends that are part of a backend set. Each Backend's configuration should be a dict/hash that consist of the following keys ['backup' option specifies whether the load balancer should treat this server as a backup unit. If true, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as &quot;backup&quot; fail the health check policy. required - false],['drain' option specifies whether the load balancer should drain this server. Servers marked &quot;drain&quot; receive no new incoming traffic. required - false], [ip_address describes the IP address of the backend server. required - true], ['offline' ensures whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. required - false], ['port'  describes the communication port for the backend server. required - true], [ 'weight' describes the load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections as a server weighted '1'. required - false]</div>
        </td>
        </tr>

        <tr>
        <td>health_checker<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>Describes the health check policy for a backend set. This should be a dict/hash that consists of the following keys ['interval_in_millis' describes the interval between health checks, in milliseconds. required - false], [ 'port' describes the backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the backends mentioned above. required - false], ['protocol' describes the protocol the health check must use, either HTTP or TCP. required - true], [ 'response_body_regex' describes a regular expression for parsing the response body from the backend server. required - false], ['retries' describes the number of retries to attempt before a backend server is considered unhealthy. required - false], ['return_code' describes the status code a healthy backend server should return. required - false], ['timeout_in_millis' describes the maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. required - false], ['url_path' describes the path against which to run the health check. required - true]</div>
        </td>
        </tr>

        <tr>
        <td>session_persistence_configuration<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The configuration details for implementing session persistence. Session persistence enables the Load Balancing Service to direct any number of requests that originate from a single logical client to a single backend web server. This should be specified as a dict/hash with the following keys ['cookie_name' describes the name of the cookie used to detect a session initiated by the backend server. Use '*' to specify that any cookie set by the backend causes the session to persist. required - true], ['disable_fallback' describes Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false. required - false]</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td rowspan="2">certificates<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The configuration details for a listener certificate bundle.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object certificates</b></caption>

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
        <div>A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces.</div>
        </td>
        </tr>

        <tr>
        <td>private_key<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The SSL private key for your certificate, in PEM format.</div>
        </td>
        </tr>

        <tr>
        <td>ca_certificate<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.</div>
        </td>
        </tr>

        <tr>
        <td>passphrase<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.</div>
        </td>
        </tr>

        <tr>
        <td>public_certificate<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The public certificate, in PEM format, that you received from your SSL certificate provider.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>compartment_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the compartment under which this Load Balancer would be created. Mandatory for create operation.Optional for delete and update. Mutually exclusive with <code>oci_load_balancer_id</code>.</div>
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
    <td>display_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Name of the Load Balancer. A user friendly name. Does not have to be unique, and could be changed. Mandatory for create and update.</div>
        </br><div style="font-size: small;">aliases: name</div>
    </td>
    </tr>

    <tr>
    <td>force_create<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">hostnames<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The details of a hostname resource associated with a load balancer.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object hostnames</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>hostname<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>A virtual hostname.</div>
        </td>
        </tr>

        <tr>
        <td>name<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The name of the hostname resource.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>is_private<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Defines whether the load balancer has a VCN-local (private) IP address.</div>
    </td>
    </tr>

    <tr>
    <td>key_by<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">listeners<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The listener configuration details.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object listeners</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>ssl_configuration<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>The load balancer SSL handling configuration details. Consists of following options, ['certificate_name' describes a friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.Certificate bundle names cannot contain spaces. required - true],['verify_depth'  describes the maximum depth for peer certificate chain verification. required - false], ['verify_peer_certificate' describes whether the load balancer listener should verify peer certificates. required - false]</div>
        </td>
        </tr>

        <tr>
        <td>connection_configuration<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Configuration details for the connection between the client and backend servers. Consists of following options, ['idle_timeout' describes The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.]</div>
        </td>
        </tr>

        <tr>
        <td>protocol<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The protocol on which the listener accepts connection requests.</div>
        </td>
        </tr>

        <tr>
        <td>port<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The communication port for the listener.</div>
        </td>
        </tr>

        <tr>
        <td>default_backend_set_name<br/><div style="font-size: small;"></div></td>
        <td>yes</td>
        <td></td>
        <td></td>
        <td>
        <div>The name of the associated backend set.</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer. Mandatory for delete and update.</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">path_route_sets<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The configuration details for a load balancer's path route sets</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object path_route_sets</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>path_routes<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>A list of configurations related to Path Routes that are part of a path route set. Each Path Route's configuration should be a dict/hash that consist of the following keys ['backend_set_name' option specifies The name of the target backend set for requests where the incoming URI matches the specified path.required - true],['path' option specifies the path string to match against the incoming URI path. required - true], ['path_match_type' describes the type of matching to apply to incoming URIs.The value of this attribute is another dict/hash with 'match_type' is key and value is one of EXACT_MATCH, FORCE_LONGEST_PREFIX_MATCH, PREFIX_MATCH, SUFFIX_MATCH. required - true]</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
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
    <td>shape_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress).</div>
    </td>
    </tr>

    <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create,update or delete Load Balancer. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
    </td>
    </tr>

    <tr>
    <td>subnet_ids<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>An array of subnet OCIDs.</div>
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
    # Create Load Balancer
    - name: Create Load Balancer
      oci_load_balancer:
        compartment_id: "ocid1.compartment.xvds"
        name: "ansible_lb"
        backend_sets:
         backend1:
          backends:
              - ip_address: "10.159.34.21"
                port: "8080"
          health_checker:
              interval_in_millis: "30000"
              port: "8080"
              protocol: "HTTP"
              response_body_regex: "^(500|40[1348])$"
              retries: "3"
              timeout_in_millis: "6000"
              return_code: "200"
              url_path: "/healthcheck"
          policy: "LEAST_CONNECTIONS"
        shape_name: "100Mbps"
        listeners:
          listerner1:
            default_backend_set_name: "backend1"
            port: "80"
            protocol: "HTTP"
        subnet_ids:
            - "ocid1.subnet.ad1"
            - "ocid1.subnet.ad2"
        certificates:
            certs1:
                ca_certificate: "fullchain.pem"
                private_key: "privkey.pem"
                public_certificate: "ca_cert.pem"
                certificate_name: "certs1"
        path_routes:
              - backend_set_name: "backend1"
                path: "/admin"
                path_match_type:
                     match_type: 'EXACT_MATCH'
        hostnames:
           ansible_hostname:
               name: 'ansible_hostname'
               hostname: 'myapp.example.com'
        state: 'present'
    # Update Load Balancer
    - name: Update Load Balancer
      oci_load_balancer:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_lb_updated"
        state: 'present'
    # Deleted Load Balancer
    - name: Update Load Balancer
      oci_load_balancer:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
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
    <td>load_balancer</td>
    <td>
        <div>Attributes of the created/updated Load Balancer. For delete, deleted Load Balancer description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'lifecycle_state': 'ACTIVE', 'display_name': 'ansible_lb955', 'shape_name': '100Mbps', 'compartment_id': 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx', 'ip_addresses': [{'is_public': True, 'ip_address': '129.213.72.32'}], 'time_created': '2018-01-06T18:22:17.198000+00:00', 'id': 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx', 'listeners': {'listerner1': {'ssl_configuration': None, 'protocol': 'HTTP', 'name': 'listerner1', 'default_backend_set_name': 'backend1', 'connection_configuration': {'idle_timeout': 1200}, 'port': 80}}, 'hostnames': {'ansible_hostname': {'hostname': 'app.example.com', 'name': 'ansible_hostname'}}, 'certificates': {'certs1': {'certificate_name': 'certs1', 'public_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n- ----END CERTIFICATE-----', 'ca_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n-----END CERTIFICATE -----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----'}}, 'subnet_ids': ['ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx', 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx'], 'backend_sets': {'backend1': {'ssl_configuration': None, 'backends': [{'drain': False, 'name': '10.159.34.21:8080', 'weight': 1, 'ip_address': '10.159.34.21', 'offline': False, 'backup': False, 'port': 8080}], 'health_checker': {'retries': 3, 'protocol': 'HTTP', 'response_body_regex': '^(500|40[1348])$', 'return_code': 200, 'timeout_in_millis': 6000, 'interval_in_millis': 30000, 'url_path': '/healthcheck', 'port': 8080}, 'name': 'backend1', 'policy': 'LEAST_CONNECTIONS', 'session_persistence_configuration': None}}, 'path_route_sets': {'ansible_path_route_set': {'path_routes': [{'path': '/example/user', 'backend_set_name': 'ansible_backend_set', 'path_match_type': {'match_type': 'EXACT_MATCH'}}]}}, 'is_private': False}</td>
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
        <td align=center>ocid1.compartment.oc1.xzvf..oifds</td>
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
        <td>sample</td>
        <td>
        </td>
        <td align=center></td>
        <td align=center></td>
        <td align=center></td>
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
        <td>hostnames</td>
        <td>
            <div>The details of a hostname resource associated with a load balancer.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'ansible_hostname': {'hostname': 'app.example.com', 'name': 'ansible_hostname'}}</td>
        </tr>

        <tr>
        <td>certificates</td>
        <td>
            <div>The configuration details for a listener certificate bundle.</div>
        </td>
        <td align=center>always</td>
        <td align=center>dict</td>
        <td align=center>{'certs1': {'certificate_name': 'certs1', 'public_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----', 'ca_certificate': '-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----'}}</td>
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
        <td align=center></td>
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
