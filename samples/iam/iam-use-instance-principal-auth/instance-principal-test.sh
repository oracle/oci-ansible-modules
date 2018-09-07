#!/bin/bash

# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


# This script runs an ansible-playbook using OCI ansible modules to list
# all compute instances in the current compartment. It employs the instance
# principal for authentication

# This script assumes an Centos/RHEL/Oracle Linux instance

# install pre-reqs (python, git, oci SDK, oci ansible modules)
sudo yum install -y python-pip
sudo yum install -y git
sudo yum install -y jq

sudo pip install virtualenv

# setup a virtualenv
virtualenv -p `which python` /tmp/mypyenv
source /tmp/mypyenv/bin/activate
python --version
pip --version
which python
which pip

# install oci SDK library
pip install oci

# install ansible
pip install ansible

ansible --version

# get and install latest OCI ansible modules
git clone https://github.com/oracle/oci-ansible-modules.git
cd oci-ansible-modules
python install.py

# -- pre-requisites installation complete.

# attempt to get a list of compute instances in the specfied compartment through an ansible playbook
cd samples/iam/iam-use-instance-principal-auth

# get the compartment id of the current instance using the instance metadata
# endpoint https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm
export SAMPLE_COMPARTMENT_OCID=$(curl -Ls http://169.254.169.254/opc/v1/instance | jq -r '.compartmentId')

# Set the ansible auth_type to "instance_principal" to have the OCI ansible modules
# use the instance principal associated with this instance, to interact with the
# OCI APIs
OCI_ANSIBLE_AUTH_TYPE="instance_principal" ansible-playbook list-compute-instances.yaml
