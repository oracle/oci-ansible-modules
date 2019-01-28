# Oracle Cloud Infrastructure Ansible Modules

## About

Oracle Cloud Infrastructure Ansible Modules provide an easy way to create and provision resources in Oracle Cloud Infrastructure (OCI) through Ansible. These modules allow you to author Ansible playbooks that help you automate the provisioning and configuring of Oracle Cloud Infrastructure services and resources, such as Compute, Load Balancing, Database, and other Oracle Cloud Infrastructure services.

**Services supported**
- Block Volume
- Compute
- Container Engine for Kubernetes Service (OKE)
- Database (including support for Autonomous Transaction Processing and Autonomous Data Warehouse Services)
- Domain Name System (DNS)
- IAM
- Load Balancing
- Networking
- Object Storage
- File Storage
- Email Delivery
- Search

The OCI Ansible modules are built using the [Oracle Cloud Infrastructure Python SDK](https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/pythonsdk.htm). The OCI Ansible modules honour the [SDK configuration](https://docs.us-phoenix-1.oraclecloud.com/Content/ToolsConfig.htm) when available.

## Installation

See the [getting started guide](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansiblegetstarted.htm) for instructions on using the installer script to install the Oracle Cloud Infrastructure Ansible Modules and its prerequisites in your host/Ansible controller node.

![Quick Install Screencast](docs/quick-install.gif)

## Samples

This project includes a catalog of Oracle Cloud Infrastructure Ansible module samples that illustrate using the modules to carry out common infrastructure provisioning and configuration tasks in the `samples` directory. The samples are organized in groups associated with Oracle Cloud Infrastructure services:
- Block Volume
- Compute
- Container Engine for Kubernetes Service (OKE)
- Database (including support for Autonomous Transaction Processing and Autonomous Data Warehouse Services)
- Domain Name System (DNS)
- IAM
- Load Balancing
- Networking
- Object Storage
- Search
- File Storage


Begin by reviewing the Readme.md file that you will find in each sample's root directory.

## Documentation

Documentation to get started and details about prerequisites, installation and configuration instructions, can be found [here](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansible.htm).

FAQs, technical design documents and development HOWTOs, and web documentation for the OCI Ansible modules can be found [here](https://oracle-cloud-infrastructure-ansible-modules.readthedocs.io).

## Help

See the ["Questions or Feedback”](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansible.htm) section.

## Changes

See [CHANGELOG](CHANGELOG.md).

## Contributing

`oci-ansible-modules` is an open source project. See [CONTRIBUTING](CONTRIBUTING.md) for details.

Oracle gratefully acknowledges the contributions to `oci-ansible-modules` that have been made by the community.

## Known Issues

You can find information on any known issues with OCI [here](https://docs.us-phoenix-1.oraclecloud.com/Content/knownissues.htm) and known issues with the OCI Ansible Modules under the “Issues” tab of this project's [GitHub repository](https://github.com/oracle/oci-ansible-modules).

## License

Copyright (c) 2018, 2019, Oracle and/or its affiliates.

This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.

See [LICENSE.txt](LICENSE.txt) for more details.
