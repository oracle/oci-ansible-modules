# OCI Ansible Modules Frequently Asked Questions (FAQs)

**1. How do I install the latest released version of the Ansible Cloud Modules?**

- Uninstall the current installed version of the modules using the `uninstall.py` script in the directory you had earlier cloned the OCI Ansible Cloud Modules repo to.
```sh
$ ./uninstall.py
```
- Perform a `git pull` on your local git repo to fetch and merge all changes in the OCI Ansible Cloud Modules Github repo at https://github.com/oracle/oci-ansible-modules.
```sh
$ git pull
```

- Checkout the tag corresponding to the latest release. The latest Ansible modules  releases are available at
[https://github.com/oracle/oci-ansible-modules/releases](https://github.com/oracle/oci-ansible-modules/releases).

```sh
$ git checkout <release>
```

- Install the latest release
```sh
$ ./install.py
```

**2. How do I get web-documentation for the OCI Ansible Cloud Modules?**

> _Please stay tuned. This is work-in-progress._

Until this is available, to obtain access to detailed information about using Ansible modules  in the CLI, including documentation of a module's configurable options, samples, return values, and so forth, use the ansible-doc command on the module's name. For example, to get the documentation for the oci_bucket_facts module, execute the following command:

```sh
$ ansible-doc oci_bucket_facts
```

**3. How do I enable `debug` mode for the OCI Ansible Cloud Modules?**

-  Set the `log_requests` variable in your ~/.oci/config to `True` to enable Request logging in the OCI python SDK as described in https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst
-  Export an environment variable to enable DEBUG mode for our Ansible modules
```sh
$ export LOG_LEVEL="DEBUG"
```

All subsequent debug messages from an ansible playbook execution using the OCI Ansible Cloud Modules
```sh
$ ansible-playbook ....
```
would go to `/tmp/oci_ansible_module.log` (the default logging location for our modules).

**4. In a Mac OSX controller node, I am seeing "ImportError: No module named yaml" when executing a playbook, in spite of observing that I have ansible and its requirements including PyYAML installed in my python setup.**

If you are running on macOS, and you have python installed by brew, you may see a ImportError(for example: `ImportError: No module named yaml`).
To resolve this, you must override the `ansible_python_interpreter` configuration option. Setting the inventory variable `ansible_python_interpreter` on any host will allow Ansible to auto-replace the interpreter used when executing python modules.

`ansible_python_interpreter` configuration option can be set in inventory file. For example:

```sh
[control-node]
localhost ansible_python_interpreter="/usr/local/Cellar/python/2.7.14_3/bin/python2.7"
```

OR `ansible_python_interpreter` configuration option can be set using `-e` command line option:

```sh
$ ansible-playbook sample-playbook.yml -e 'ansible_python_interpreter=/usr/local/Cellar/python/2.7.14_3/bin/python2.7'
```

**5. `ansible-doc` fails with an error when using the modules through an ansible role**

`ansible-doc` fails with a documentation error when using the Ansible Cloud Modules through the `oci-ansible-modules` ansible role.

```sh
$ ansible-doc oci_bucket_facts
[ERROR]: module oci_bucket_facts has a documentation error formatting or is missing documentation
```

The documentation fragments shipped by an ansible module that is delivered by an ansible role, is not consulted by `ansible-doc`. To get around this problem, use the installer script to install the OCI Ansible Cloud Modules.

**6. How do I use the `oci_inventory.py` dynamic inventory script?**

In addition to the OCI Ansible Cloud Modules, this project also provide a [dynamic inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html) script for OCI that you can use to construct a dynamic inventory of your OCI compute instances. For more details, see our how-to documentation at [using the dynamic inventory script](dynamic-inventory-script.md).

**7. Any security guidelines or best practices?**

The OCI Ansible Cloud Modules uses the authentication information specified in the standard OCI SDK configuration file (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#configuring-the-sdk) while creating and configuring OCI resources.

> *Caution*: IAM credentials referenced in the OCI SDK configuration file, grants access to resources. It is important to secure these credentials to prevent unauthorized access to Oracle Cloud Infrastructure resources. Follow the guidelines in https://docs.us-phoenix-1.oraclecloud.com/Content/Security/Reference/iam_security.htm#IAMCredentials to secure the IAM credentials in the controller node where you run ansible playbooks that uses these modules.

The OCI Ansible Cloud Modules allows the authentication information specified in the OCI SDK configuration file to be overridden using module options and environment variables. Please refer to the ansible module documentation of the OCI Ansible Cloud Modules for more details. Oracle recommends the use of OCI SDK configuration file to specify authentication information. Use the "profiles" feature in the OCI SDK configuration file to support different users. The use of environment variables and ansible module options to override Authentication information must be avoided in production scenarios. While distributing roles that use the OCI Ansible Cloud Modules, ensure that no IAM credentials are included with the roles.
