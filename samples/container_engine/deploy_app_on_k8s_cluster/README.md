# Overview

This sample creates a cluster with Oracle Cloud Infrastructure Container Engine for
Kubernetes(OKE) and deploys a sample app on the cluster. This sample is also
documented in this [tutorial](http://www.oracle.com/webfolder/technetwork/tutorials/obe/oci/oke-full/index.html).

This sample:
- creates a configured VCN and related resources required for setting up an OKE cluster
- creates a cluster
- creates a node pool
- downloads the kubeconfig file for the cluster
- deploys a sample app on the cluster
- verifies successful deployment

# Pre-requisites
This sample uses `k8s_raw` module which requires `openshift`. Please install `openshift` through:
> pip install openshift

This sample also requires [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) to be
installed and setup locally.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:
- ad1: Name of the first availability domain.
- ad2: Name of the second availability domain.
- ad3: Name of the third availability domain.
- cluster_compartment: OCID of the compartment in which you want to create OKE cluster.
- kubeconfig_path: Path to download the kubeconfig for the created cluster.
