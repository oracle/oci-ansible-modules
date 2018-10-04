# Overview

This sample shows how to retrieve public and private ip address of a DB System's node in order to access it, through OCI ansible cloud modules. Accessing
DB Node is required for troubleshooting  or patching the DB System using DB CLI. 

The sample 
- Collects DB Node's VNIC information of a specified DB system
- Extracts Public and Private Ip of the DB Node from VNIC 

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- compartment_id
- db_system_id
- host_name

Also ensure you have a valid DB system is provisioned and running whose id should be provided as part of db_system_id.