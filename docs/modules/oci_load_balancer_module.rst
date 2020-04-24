:source: cloud/oracle/oci_load_balancer.py

:orphan:

.. _oci_load_balancer_module:


oci_load_balancer -- Create, update and delete load balancers in OCI Load Balancing Service
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Creates OCI Load Balancers
- Update OCI Load Balancers, if present, with a new display name
- Delete OCI Load Balancers, if present.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <b>api_user</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>api_user_fingerprint</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>api_user_key_file</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>api_user_key_pass_phrase</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>auth_type</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible` playbooks within an OCI compute instance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>backend_sets</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The configuration details for a load balancer&#x27;s backend sets</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>backends</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of configurations related to Backends that are part of a backend set. Each Backend&#x27;s configuration should be a dict/hash that consist of the following keys [&#x27;backup&#x27; option specifies whether the load balancer should treat this server as a backup unit. If true, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as &quot;backup&quot; fail the health check policy. required - false],[&#x27;drain&#x27; option specifies whether the load balancer should drain this server. Servers marked &quot;drain&quot; receive no new incoming traffic. required - false], [ip_address describes the IP address of the backend server. required - true], [&#x27;offline&#x27; ensures whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic. required - false], [&#x27;port&#x27;  describes the communication port for the backend server. required - true], [ &#x27;weight&#x27; describes the load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted &#x27;3&#x27; receives 3 times the number of new connections as a server weighted &#x27;1&#x27;. required - false]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>health_checker</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Describes the health check policy for a backend set. This should be a dict/hash that consists of the following keys [&#x27;interval_in_millis&#x27; describes the interval between health checks, in milliseconds. required - false], [ &#x27;port&#x27; describes the backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the backends mentioned above. required - false], [&#x27;protocol&#x27; describes the protocol the health check must use, either HTTP or TCP. required - true], [ &#x27;response_body_regex&#x27; describes a regular expression for parsing the response body from the backend server. required - false], [&#x27;retries&#x27; describes the number of retries to attempt before a backend server is considered unhealthy. required - false], [&#x27;return_code&#x27; describes the status code a healthy backend server should return. required - false], [&#x27;timeout_in_millis&#x27; describes the maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. required - false], [&#x27;url_path&#x27; describes the path against which to run the health check. required - true]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>policy</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The load balancer policy for the backend set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>session_persistence_configuration</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration details for implementing session persistence. Session persistence enables the Load Balancing Service to direct any number of requests that originate from a single logical client to a single backend web server. This should be specified as a dict/hash with the following keys [&#x27;cookie_name&#x27; describes the name of the cookie used to detect a session initiated by the backend server. Use &#x27;*&#x27; to specify that any cookie set by the backend causes the session to persist. required - true], [&#x27;disable_fallback&#x27; describes Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false. required - false]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>ssl_configuration</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The load balancer&#x27;s SSL handling configuration details. This should be specified as a dict/hash with the following keys [certificate_name describes a friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.Certificate bundle names cannot contain spaces. required - true], [&#x27;verify_depth&#x27;  describes the maximum depth for peer certificate chain verification. required - false], [&#x27;verify_peer_certificate&#x27;  describes whether the load balancer listener should verify peer certificates. required - false]</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>certificates</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The configuration details for a listener certificate bundle.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>ca_certificate</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>certificate_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>passphrase</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>private_key</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The SSL private key for your certificate, in PEM format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>public_certificate</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The public certificate, in PEM format, that you received from your SSL certificate provider.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>compartment_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the compartment under which this Load Balancer would be created. Mandatory for create operation.Optional for delete and update. Mutually exclusive with <code>oci_load_balancer_id</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>config_file_location</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>config_profile_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defined_tags</b>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>display_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the Load Balancer. A user friendly name. Does not have to be unique, and could be changed. Mandatory for create and update.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>force_create</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn&#x27;t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>freeform_tags</b>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm</a>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>hostnames</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The details of a hostname resource associated with a load balancer.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>hostname</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A virtual hostname.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the hostname resource.</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>is_private</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Defines whether the load balancer has a VCN-local (private) IP address.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>key_by</b>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource except <em>freeform_tags</em> are used to uniquely identify a resource.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>listeners</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The listener configuration details.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>connection_configuration</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Configuration details for the connection between the client and backend servers. Consists of following options, [&#x27;idle_timeout&#x27; describes The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>default_backend_set_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the associated backend set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>hostname_names</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of hostname resource names.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>path_route_set_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the set of path-based routing rules, PathRouteSet, applied to this listener&#x27;s traffic.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>port</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The communication port for the listener.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>protocol</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The protocol on which the listener accepts connection requests.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>ssl_configuration</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The load balancer SSL handling configuration details. Consists of following options, [&#x27;certificate_name&#x27; describes a friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.Certificate bundle names cannot contain spaces. required - true],[&#x27;verify_depth&#x27;  describes the maximum depth for peer certificate chain verification. required - false], [&#x27;verify_peer_certificate&#x27; describes whether the load balancer listener should verify peer certificates. required - false]</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>load_balancer_id</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Identifier of the Load Balancer. Mandatory for delete and update.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>path_route_sets</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The configuration details for a load balancer&#x27;s path route sets</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>path_routes</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of configurations related to Path Routes that are part of a path route set. Each Path Route&#x27;s configuration should be a dict/hash that consist of the following keys [&#x27;backend_set_name&#x27; option specifies The name of the target backend set for requests where the incoming URI matches the specified path.required - true],[&#x27;path&#x27; option specifies the path string to match against the incoming URI path. required - true], [&#x27;path_match_type&#x27; describes the type of matching to apply to incoming URIs.The value of this attribute is another dict/hash with &#x27;match_type&#x27; is key and value is one of EXACT_MATCH, FORCE_LONGEST_PREFIX_MATCH, PREFIX_MATCH, SUFFIX_MATCH. required - true]</div>
                                                        </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>region</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>shape_name</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>state</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Create,update or delete Load Balancer. For <em>state=present</em>, if it does not exists, it gets created. If exists, it gets updated.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>subnet_ids</b>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>An array of subnet OCIDs.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>tenancy</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait</b>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Whether to wait for create or delete operation to complete.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait_timeout</b>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">2000</div>
                                    </td>
                                                                <td>
                                                                        <div>Time, in seconds, to wait when <em>wait=yes</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>wait_until</b>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                            </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The lifecycle state to wait for the resource to transition into when <em>wait=yes</em>. By default, when <em>wait=yes</em>, we wait for the resource to get into ACTIVE/ATTACHED/AVAILABLE/PROVISIONED/ RUNNING applicable lifecycle state during create operation &amp; to get into DELETED/DETACHED/ TERMINATED lifecycle state during delete operation.</div>
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
            hostname_names: ['hostname_001']
            path_route_set_name: 'test_path_route_set'
        subnet_ids:
            - "ocid1.subnet.ad1"
            - "ocid1.subnet.ad2"
        certificates:
            certs1:
                ca_certificate: "fullchain.pem"
                private_key: "privkey.pem"
                public_certificate: "ca_cert.pem"
                certificate_name: "certs1"
        path_route_sets:
              test_path_route_set:
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

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <b>load_balancer</b>
                    <div style="font-size: small; color: purple">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Attributes of the created/updated Load Balancer. For delete, deleted Load Balancer description will be returned.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;listeners&#x27;: {&#x27;listerner1&#x27;: {&#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;name&#x27;: &#x27;listerner1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;port&#x27;: 80, &#x27;connection_configuration&#x27;: {&#x27;idle_timeout&#x27;: 1200}, &#x27;default_backend_set_name&#x27;: &#x27;backend1&#x27;}}, &#x27;hostnames&#x27;: {&#x27;ansible_hostname&#x27;: {&#x27;hostname&#x27;: &#x27;app.example.com&#x27;, &#x27;name&#x27;: &#x27;ansible_hostname&#x27;}}, &#x27;display_name&#x27;: &#x27;ansible_lb955&#x27;, &#x27;certificates&#x27;: {&#x27;certs1&#x27;: {&#x27;public_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n- ----END CERTIFICATE-----&#x27;, &#x27;ca_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n-----END CERTIFICATE -----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----&#x27;, &#x27;certificate_name&#x27;: &#x27;certs1&#x27;}}, &#x27;shape_name&#x27;: &#x27;100Mbps&#x27;, &#x27;lifecycle_state&#x27;: &#x27;ACTIVE&#x27;, &#x27;time_created&#x27;: &#x27;2018-01-06T18:22:17.198000+00:00&#x27;, &#x27;path_route_sets&#x27;: {&#x27;ansible_path_route_set&#x27;: {&#x27;path_routes&#x27;: [{&#x27;backend_set_name&#x27;: &#x27;ansible_backend_set&#x27;, &#x27;path&#x27;: &#x27;/example/user&#x27;, &#x27;path_match_type&#x27;: {&#x27;match_type&#x27;: &#x27;EXACT_MATCH&#x27;}}]}}, &#x27;subnet_ids&#x27;: [&#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;, &#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;], &#x27;ip_addresses&#x27;: [{&#x27;ip_address&#x27;: &#x27;129.213.72.32&#x27;, &#x27;is_public&#x27;: True}], &#x27;backend_sets&#x27;: {&#x27;backend1&#x27;: {&#x27;session_persistence_configuration&#x27;: None, &#x27;backends&#x27;: [{&#x27;weight&#x27;: 1, &#x27;name&#x27;: &#x27;10.159.34.21:8080&#x27;, &#x27;ip_address&#x27;: &#x27;10.159.34.21&#x27;, &#x27;port&#x27;: 8080, &#x27;drain&#x27;: False, &#x27;backup&#x27;: False, &#x27;offline&#x27;: False}], &#x27;name&#x27;: &#x27;backend1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;policy&#x27;: &#x27;LEAST_CONNECTIONS&#x27;, &#x27;health_checker&#x27;: {&#x27;timeout_in_millis&#x27;: 6000, &#x27;retries&#x27;: 3, &#x27;response_body_regex&#x27;: &#x27;^(500|40[1348])$&#x27;, &#x27;url_path&#x27;: &#x27;/healthcheck&#x27;, &#x27;port&#x27;: 8080, &#x27;interval_in_millis&#x27;: 30000, &#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;return_code&#x27;: 200}}}, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;42&#x27;}}, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxEXAMPLExxxxx&#x27;, &#x27;is_private&#x27;: False, &#x27;id&#x27;: &#x27;ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx&#x27;}</div>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>backend_sets</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The configuration details for a load balancer backend set</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;backend1&#x27;: {&#x27;backends&#x27;: [{&#x27;weight&#x27;: 1, &#x27;name&#x27;: &#x27;10.159.34.21:8080&#x27;, &#x27;ip_address&#x27;: &#x27;10.159.34.21&#x27;, &#x27;port&#x27;: 8080, &#x27;drain&#x27;: False, &#x27;backup&#x27;: False, &#x27;offline&#x27;: False}], &#x27;health_checker&#x27;: {&#x27;timeout_in_millis&#x27;: 6000, &#x27;retries&#x27;: 3, &#x27;response_body_regex&#x27;: &#x27;^(500|40[1348])$&#x27;, &#x27;url_path&#x27;: &#x27;/healthcheck&#x27;, &#x27;port&#x27;: 8080, &#x27;interval_in_millis&#x27;: 30000, &#x27;policy&#x27;: &#x27;LEAST_CONNECTIONS&#x27;, &#x27;session_persistence_configuration&#x27;: None, &#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;return_code&#x27;: 200, &#x27;ssl_configuration&#x27;: None, &#x27;name&#x27;: &#x27;backend1&#x27;}}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>certificates</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The configuration details for a listener certificate bundle.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;certs1&#x27;: {&#x27;public_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----&#x27;, &#x27;ca_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE-----\nMIIFKTCCBBGgAwIBAgISBIs5aiZ1fWapuAl2P9POFMXjMA0GCSqGSIb3DQEBCwUA\n -----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----&#x27;, &#x27;certificate_name&#x27;: &#x27;certs1&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>compartment_id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The identifier of the compartment containing the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1.xzvf..oifds</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>display_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Name assigned to the Load Balancer during creation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ansible_lb</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>hostnames</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The details of a hostname resource associated with a load balancer.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;ansible_hostname&#x27;: {&#x27;hostname&#x27;: &#x27;app.example.com&#x27;, &#x27;name&#x27;: &#x27;ansible_hostname&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>id</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Identifier of the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>lifecycle_state</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The current state of the Load Balancer</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>listeners</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The listener configuration details.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;listerner1&#x27;: {&#x27;protocol&#x27;: &#x27;HTTP&#x27;, &#x27;name&#x27;: &#x27;listerner1&#x27;, &#x27;ssl_configuration&#x27;: None, &#x27;port&#x27;: 80, &#x27;connection_configuration&#x27;: {&#x27;idle_timeout&#x27;: 1200}, &#x27;default_backend_set_name&#x27;: &#x27;backend1&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>path_route_sets</b>
                    <div style="font-size: small; color: purple">dictionary</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>The path route sets configuration details.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>sample</b>
                    <div style="font-size: small; color: purple">-</div>
                                    </td>
                <td></td>
                <td>
                                                                                    <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>shape_name</b>
                    <div style="font-size: small; color: purple">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">100Mbps</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>subnet_ids</b>
                    <div style="font-size: small; color: purple">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>An array of subnet OCIDs.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;, &#x27;ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>time_created</b>
                    <div style="font-size: small; color: purple">datetime</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Date and time when the Load Balancer was created, in the format defined by RFC3339</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-08-25 21:10:29.600000+00:00</div>
                                    </td>
            </tr>
                    
                                        </table>
    <br/><br/>


Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is :ref:`maintained by the Ansible Community <modules_support>`. *[community]*





Authors
~~~~~~~

- Debayan Gupta(@debayan_gupta)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/cloud/oracle/oci_load_balancer.py?description=%23%23%23%23%23%20SUMMARY%0A%3C!---%20Your%20description%20here%20--%3E%0A%0A%0A%23%23%23%23%23%20ISSUE%20TYPE%0A-%20Docs%20Pull%20Request%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
