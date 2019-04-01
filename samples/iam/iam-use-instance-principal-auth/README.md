# Overview

This sample shows how you can authorize compute instances to call services in Oracle Cloud Infrastructure using "Instance Principals". This sample demonstrates how you can create the resources necessary for the Instance principals feature, and how you can get OCI Ansible Modules to use instance-principal based authentication when ansible playbooks are run inside an OCI compute instance.

See [the feature announcement blog](https://blogs.oracle.com/cloud-infrastructure/announcing-instance-principals-for-identity-and-access-management) and [official OCI IAM documentation](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm) for a background on what instance principals are, and how they work.

This sample automates the steps described in https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm?Highlight=instance%20principal#process to setup and use OCI compute instances as principals. 

A dynamic group is created that matches all compute instances within the specified `sample_compartment_ocid`. An IAM policy is then created to ensure that all instances within this dynamic group is allowed to inspect all resources and get information about all compute instances within the specified `sample_compartment_ocid`. A new compute instance is then launched within `sample_compartment_ocid`. A script is provided, that when run within the new compute instance will use instance-principal based authentication to list all compute instances within `sample_compartment_ocid`. 

Note: the playbook `basic-sanity-checks.yaml` created by the script doesn't have any explicit references to instance-principal based authentication (this ensures that the playbook need not be modified if you want to change the authentication type -- say if you want to run the playbook outside the compute instance). To ensure instance-principal based authentication is employed, in this case, ensure that the following environment variable is set before executing the playbook:
> OCI_ANSIBLE_AUTH_TYPE="instance_principal" 

If you want to author a playbook that is tied to, and only needs to use, instance-principal based authentication, you can use the `auth_type` module option and set it to `instance_principal` directly within the playbook.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- `sample_tenancy_ocid`
- `sample_compartment_ocid`
- `sample_image_ocid` (Provide an Oracle Linux(OL) image ocid)
- `sample_ad_name`
