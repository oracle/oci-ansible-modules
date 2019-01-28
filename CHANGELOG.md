# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2019-01-28

### Added
- Modules to manage
    - [FastConnect](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm) resources
- Added the following features in existing modules:
    - [Pre-Authenticated Requests](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) in Object Storage Service.
    - `force` option in `oci_bucket` now also supports automatic deletion of bucket-level PARs
    - Support for listing multi-part uploads and multi-part upload parts, aborting a multi-part upload in `oci_object_facts` and `oci_object` modules
    - In modules having a module option that supports a list of items, a `delete_*` option is now supported to delete specified list items. See `delete_security_rules` in `oci_security_list` for an example
    - Options in `oci_tag` module to apply tags
    - Option to filter by `display_name` in `oci_instance_configuration_facts` module
- Added the following features in OCI dynamic inventory script:
    - Option to build inventory from multiple regions

### Changed
- Minimum supported OCI Python SDK to `2.1.3`

## [1.4.0] - 2018-12-19

### Added
- Modules to manage
    - [Cost tracking tags](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm#UsingCostTrackingTags)
    - [Retrieving initial credentials of Windows instances](https://docs.cloud.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm)
- Added the following features in existing modules:
    - Support for creating nested compartments and deleting compartments in `oci_compartment` module
    - Support for retrieving information of nested compartments in `oci_compartment_facts` module 
    - Support specification of cost-tracking during tag definition creation in the `oci_tags` module
    - Support for multi-part uploads and parallel uploads in `oci_object` module
- Added the following features in OCI dynamic inventory script:
    - Options to parallelise the inventory generation
    - Options to build inventory of only specific tagged instances
    - Option to build inventory of entire hierarchy under a given compartment
- Samples to demonstrate:
  - how to give compute instances private access to OCI Object Storage using Service Gateway
  - how to enable internet access to a private instance using NAT Gateway

## [1.3.0] - 2018-11-16

### Added
- Modules to manage
  - [NAT gateways](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)
  - [Volume groups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm)
  - [Volume group backups](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup)
  - [Policy-based volume backups](https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  - [Auth Tokens](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm?Highlight=Auth%20tokens#two)
  - [Instance console connections](https://docs.cloud.oracle.com/iaas/Content/Compute/References/serialconsole.htm)
  - [Serial console data/Console history](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/displayingconsole.htm)
  - [Instance Configurations and Instance Pools](https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm)
- Support for the following services:
  - [Oracle Cloud Infrastructure File Storage Service](https://docs.cloud.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm)
  - [Oracle Cloud Infrastructure Email Delivery Service](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm)
- Added the following features in existing modules:
  - Options in `oci_boot_volume` module to support creating boot volumes
  - Option in `oci_volume` module to support assigning a backup policy while creating a volume
  - Enhanced wait support in `oci_node_pool` module
  - Provision and terminate `exact_count` instances in parallel in the `oci_instance` module
  - `oci_route_table` and `oci_security_list` supports the specification of a Service (via a Service Gateway) as a
    destination/source for route and security rules.
  - The `oci_inventory.py` dynamic inventory script supports Instance Principal authorization.
- Samples to demonstrate:
  - creating a File System and mounting it in a Compute instance and how to create a File system snapshot
  - how a File System can be exported using two different export paths on two different mount targets
  - how a Serial and VNC connection can be created for a compute instance
  - how to create an instance pool to launch a set of compute instances based on an instance configuration

### Changed
- Minimum supported OCI Python SDK to `2.1.0`
- Type of module option `block_traffic` in oci_service_gateway module changed to `bool`

### Deprecated
- The `oci_swift_password` and `oci_swift_password_facts` modules have been deprecated. Use `oci_auth_token` and `oci_auth_token_facts` instead.
- The `cidr_block` sub-option in the `route_rules` option of `oci_route_rules` is deprecated. Use `destination` and `destination_type` (equal to `CIDR_BLOCK`) instead to specify a destination IP address in CIDR notation as the destination target for a route rule.

## [1.2.0] - 2018-10-03

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
