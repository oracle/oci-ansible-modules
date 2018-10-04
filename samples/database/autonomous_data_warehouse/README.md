# Overview

This sample shows how to create an Autonomous Data Warehouse. To explore more about
Oracle Cloud Infrastructure's Autonomous Data Warehouse Cloud Service, please visit
[here](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adwoverview.htm).

The sample
- sets up an Autonomous Data Warehouse.
- List all the Autonomous Data Warehouses available in the compartment filtered by display name.
- Get facts of a specific Autonomous Data Warehouse.
- Stops and starts an Autonomous Data Warehouse.
- Deletes an Autonomous Data Warehouse.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:
- compartment_ocid
- cpu_core_count
- display_name
- admin_password
- db_name
- data_storage_size_in_tbs
- license_model

Note: The sample, by default, sets up an Autonomous Data Warehouse, prints an information message,
runs a few tests to show it is working, and tears down the Autonomous Data Warehouse. If you want
to experiment with the Autonomous Data Warehouse after it is setup, comment out the invocation
to `teardown.yaml` at the end of `sample.yaml`.
