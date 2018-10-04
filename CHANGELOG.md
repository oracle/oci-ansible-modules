# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2018-10-04

### Added
- Modules to manage
  - [Dynamic Routing Gateways(DRGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm)
  - [Customer Premises Equipments(CPEs)](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Cpe/)
  - [IPSec Connections](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)
  - [Local Peering Gateways(LPGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm)
  - [Remote Peering Connections(RPCs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
  - [Service Gateways](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)
- Support for the following services:
    - [Oracle Cloud Infrastructure Autonomous Transaction Processing](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/atpoverview.htm)
    - [Oracle Cloud Infrastructure Autonomous Data Warehouse](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adwoverview.htm)
    - [Oracle Cloud Infrastructure Search](https://docs.cloud.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm)
- Samples to demonstrate:
    - provisioning and managing an Oracle Cloud Infrastructure Autonomous Transaction Processing Database and an
      Autonomous Data Warehouse
    - provisioning a virtual cloud network (VCN) with private subnets and an IPSec VPN(using a dynamic routing gateway,
      a customer premises equipment and an IPSec connection)
- Fact modules now support additional filter options (where applicable) for you to filter resources

## [1.1.0] - 2018-09-06

### Added
- Support for following services:
  - [Oracle Container Engine for Kubernetes Service (OKE)](https://docs.cloud.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm)
  - [Oracle Domain Name System (DNS) Service](https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
- Modules to manage [IAM dynamic groups](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
- Support for [instance principal authorization](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm)
- Support wait options in load balancer service modules
- Support filtering of resources in facts modules using `display_name` or `name`
- Support to automatically redirect IAM operations to home region of tenancy
- Support for [Fault Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)
- Added samples to demonstrate:
  - the use of instance principal authorization
  - setting up prerequisites for OKE, provisioning OKE cluster and deploying a sample application
  - provisioning of a load balancer component in the Secure MongoDB deployment solution

### Changed
- Minimum supported OCI Python SDK to 2.0.2

## [1.0.0] - 2018-07-09

### Added
- In this first release of the OCI Ansible modules, the following Services are supported:
  - Compute
  - Block Storage
  - Object Storage
  - Networking
  - Load Balancer
  - Database Service
  - Identity and Access Management
- Provides a dynamic inventory script `oci_inventory.py` that helps you fetch the latest set of OCI compute instances and make them available for your playbooks to be executed upon.
- Includes a catalog of Oracle Cloud Infrastructure Ansible module samples, in the [samples](samples) directory, that illustrate using the modules to carry out common infrastructure provisioning and configuration tasks. 

