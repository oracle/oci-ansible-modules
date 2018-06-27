.. _oci_load_balancer_certificate:


oci_load_balancer_certificate - Add or remove a SSL certificate from a load balancer in OCI Load Balancing Service
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5




.. contents::
   :local:
   :depth: 2


Synopsis
--------


* Add a SSL certificate to OCI Load Balancer
* Delete a SSL certificate, if present.



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
    <td>ca_certificate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider. The absolute path of the certificate file should be provided.</div>
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
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Identifier of the Load Balancer in which the certificate belongs</div>
        </br><div style="font-size: small;">aliases: id</div>
    </td>
    </tr>

    <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>The name of the certificate  to add to the load balancer.</div>
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
    <td>private_key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The SSL private key for your certificate, in PEM format.The absolute path of the private key file should be provided.</div>
    </td>
    </tr>

    <tr>
    <td>public_certificate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>The public certificate, in PEM format, that you received from your SSL certificate provider. The absolute path of the public certificate file should be provided.</div>
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
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
    <td><ul><li>present</li><li>absent</li></ul></td>
    <td>
        <div>Create or  delete certificate. For <em>state=present</em>, if it does not exists, it gets added.</div>
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
    # Add a certificate bundle (without passphrase) to a loadbalancer
    - name: Add a certificate bundle (without passphrase) to a loadbalancer
      oci_load_balancer_certificate:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_certtificate"
        ca_certificate: "certificate_src/ca_cert.pem"
        private_key: "certificate_src/private_key.pem"
        public_certificate: "certificate_src/cert.pem"
        state: 'present'
    # Add a certificate bundle (with a passphrase for encrypted private keys) to a load balancer
    - name: Create certificate with Passphrase
      oci_load_balancer_certificate:
        name: "ansible_cert_with_passphrase"
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        ca_certificate: "certificate_src/ca_cert.pem"
        passphrase: "ansible"
        private_key: "certificate_src/private_key_with_passphrase.pem"
        public_certificate: "certificate_src/cert_with_passphrase.pem"
        state: 'present'
    # Delete a SSL Certificate from a load balancer
    - name: Delete a SSL certificate
      oci_load_balancer_certificate:
        load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
        name: "ansible_certtificate"
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
    <td>certificate</td>
    <td>
        <div>Attributes of the created certificate. For delete, deleted certificate description will be returned.</div>
    </td>
    <td align=center>success</td>
    <td align=center>complex</td>
    <td align=center>{'certificate_name': 'ansible_cert', 'public_certificate': '-----BEGIN CERTIFICATE-----\nMIIDPjCCAiYCCQC5OEUUNtrC\n-----END CERTIFICATE-----', 'ca_certificate': '-----BEGIN CERTIFICATE-----\nMIIDlTCCAn2gAw\n-----END CERTIFICATE-----'}</td>
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
        <td>certificate_name</td>
        <td>
            <div>Name of the certificate</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>ansible_certificate</td>
        </tr>

        <tr>
        <td>public_certificate</td>
        <td>
            <div>The public certificate, in PEM format, that you received from your SSL certificate provider.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>-----BEGIN CERTIFICATE----- MIIDlTCCAn -----END CERTIFICATE-----</td>
        </tr>

        <tr>
        <td>ca_certificate</td>
        <td>
            <div>The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.</div>
        </td>
        <td align=center>always</td>
        <td align=center>string</td>
        <td align=center>-----BEGIN CERTIFICATE----- MIIDlTCCA -----END CERTIFICATE-----</td>
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
