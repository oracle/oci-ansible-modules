# Overview

This sample shows how to perform typical Identity and Access Management (IAM) tasks such as managing users, groups, policies through OCI ansible modules. The sample then shows how to execute a playbook or a set of tasks as a different user, and how common IAM tasks such as getting the home-region or picking an availability domain can be performed using the OCI ansible modules.

The sample assumes the default user configured in the OCI configuration user is in the Administrator group or atleast has the required access for managing users, groups, policies. The sample
- creates 2 groups -- `ObjectReaders` and `ObjectWriters`
- Create a policy that allows `ObjectReaders` to list and read buckets and objects, `ObjectWriters` to create, update, list and read buckets and objects in a given compartment
and assign it to those groups
- creates 2 users `alice` and `bob`. Add `alice` to the `ObjectWriters` group and `bob` to the `ObjectReaders` group respectively
- Run as `alice` to create a bucket, and upload a couple of objects to it
- Run as `bob` to list all objects in a bucket

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- sample_compartment_ocid
- sample_object_namespace_name
- tenancy_ocid
