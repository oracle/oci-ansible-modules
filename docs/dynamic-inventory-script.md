# Oracle Cloud Infrastructure(OCI) Ansible Dynamic Inventory Script

If you use Ansible to work with hosts provisioned in OCI, using a [static inventory file](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html) may not work well, as OCI compute instances may get provisioned and terminated over time, or be created or managed by other external tools (API, console, SDK, Terraform etc). Using the OCI [dynamic inventory script](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html) will help ensure that the latest set of OCI compute instances are dynamically fetched and available for your playbooks to be executed upon.

To use the OCI dynamic inventory script, grab the script and the default configuration files from
- [inventory-script/oci_inventory.py](inventory-script/oci_inventory.py)
- [inventory-script/oci_inventory.ini](inventory-script/oci_inventory.ini)
to a local directory.

## Dynamic Inventory Script

### Prerequisites

> Note: Before using the script, please ensure that you have a valid OCI SDK configuration. Refer [OCI SDK Configuration documentation](https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm) for details on how to configure `~/.oci/config`.


### Script and Configuration Details

The `oci_inventory.py` script uses the OCI Python SDK to query OCI compute instances in your tenancy, and builds a dynamic inventory that can then be used in your Ansible playbooks. Arguments to the `oci_inventory.py` can help you control the configuration profile to use, the compartment to limit your search to, etc.

The `oci_inventory.ini` configuration file can be optionally used to configure the OCI configuration profile to use, control how the inventory details are cached, and how hosts are named in your inventory.

The `oci_inventory.py` script accepts the following command line arguments:
```
usage: oci_inventory.py [-h] [--list] [--host HOST] [-config CONFIG_FILE]
              [--profile PROFILE] [--compartment COMPARTMENT]
              [--refresh-cache] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --list                List instances (default: True)
  --host HOST           Get all information about a compute instance
  -config CONFIG_FILE, --config-file CONFIG_FILE
                        OCI config file location
  --profile PROFILE     OCI config profile for connecting to OCI
  --compartment COMPARTMENT
                        Name of the compartment
  --refresh-cache, -r   Force refresh of cache by making API requests to OCI
                        (default: False - use cache files)
  --debug               Send debug messages to STDERR
```

The `oci_inventory.py` script also accepts the following environment variables:

| Environment Variable | Description |
| -------------------- | ----------- |
| OCI_CONFIG_FILE | Specifies the OCI SDK configuration file to use. |
| OCI_INI_PATH | Specifies the inventory script's configuration file to use. |
| OCI_CONFIG_PROFILE | Specifies the profile in the OCI SDK configuration file, to be used. |
| OCI_USER_ID | Specifies the OCID of the OCI user to use to fetch the inventory. |
| OCI_USER_FINGERPRINT | Specifies the OCI user's key-pair's fingerprint being used to use to fetch the inventory. |
| OCI_USER_KEY_FILE | Specifies the full path including the filename of the private key of the OCI user being used to use to fetch the inventory. |
| OCI_TENANCY | Specifies the OCID of the tenancy to use to fetch the inventory |
| OCI_REGION |  Specifies the OCI Region to use to fetch the inventory |
| OCI_USER_KEY_PASS_PHRASE | Specifies the passphrase of the key (if encrypted), to use to fetch the inventory. |
| OCI_CACHE_DIR | Specifies the directory where cache files of the inventory script will reside. A file named "ansible-oci.cache" will be written to this directory. |
| OCI_CACHE_MAX_AGE |  The number of seconds a cache file is considered valid. To disable caching and get the latest inventory from OCI, set this value to 0. |
| OCI_HOSTNAME_FORMAT | Host naming format to use in the generated inventory. Use 'fqdn' to list hosts using the instance's Fully Qualified Domain Name (FQDN). Use 'public_ip' to list hosts using public IP address. Use 'private_ip' to list hosts using private IP address.|

The order of precedence for the configuration used by the inventory script is:
1. command line arguments
1. environment variables
1. options in script configuration file.

The configuration file used for the script defaults to `./oci_inventory.ini` file. The OCI SDK configuration file defaults to `~/.oci/config` file. The script uses the `DEFAULT` profile from the config file if no profile name is specified.

The generated inventory is grouped along the following axes:
- region
- compartment_name
- availability domain
- vcn_id
- subnet_id
- security_list_id
- image_id
- instance shape
- freeform tags with group name as "tag_key=value"
- defined tags with group name as "namespace#key=value"
- metadata (key, value) with group name as "key=value"
- extended metadata (key, value) with group name as "key=value"

By default, all non-alphanumeric characters except HASH(#), EQUALS(=), PERIOD(.) and DASH(-) in group names and host names are replaced with an UNDERSCORE(_) when the inventory is generated, so that the names can be used as Ansible groups. To disable this replacement, set sanitize_names to False in the dynamic inventory settings file(default ./oci_inventory.ini). To also replace DASH(-) when sanitize_names is True, set replace_dash_in_names to True in the settings file.

## How to Use

### Using a Dynamic Inventory During Playbook Execution

Ensure that you have correct OCI SDK configuration (and optionally an `oci_inventory.ini`). Invoke the `ansible-playbook` command using
```sh
$ ansible-playbook -i <path-to-inventory-file>/oci_inventory.py <your-playbook-using-the-generated-inventory>
```
or use the [`ANSIBLE_HOSTS`](https://docs.ansible.com/ansible/2.4/config.html#envvar-ANSIBLE_HOSTS) environment variable:
```sh
$ ANSIBLE_HOSTS=<path-to-inventory-file>/oci_inventory.py ansible-playbook <your-playbook-using-the-generated-inventory>
```


### To Disable Cache and Fetch Latest

If you are running the dynamic inventory in a standalone manner, you can use "--refresh"/"-r" to ignore the cached inventory and fetch the latest inventory from OCI:
```sh
$ \<path-to-inventory-file\>/oci_inventory.py --refresh
```

If you are using the inventory script during an ansible-playbook invocation, set the `OCI_CACHE_MAX_AGE` environment variable to "0"(zero) to ignore the cache, and fetch the latest inventory from OCI: 
```sh
$ OCI_CACHE_MAX_AGE=0 ansible-playbook -i <path-to-inventory-file>/oci_inventory.py <your-playbook-using-the-generated-inventory>
```

### Debugging

If you want to look at the dynamic inventory generated by the script, run it in with "--list", and check the output.

```sh
$ <path-to-inventory-file>/oci_inventory.py --list
```

To print additional debug information to STDERR, use
```sh
$ <path-to-inventory-file>/oci_inventory.py --debug
```

### Get a Single Host's Information

The inventory script can also be configured to provide information about a single host. 

```sh
$ <path-to-inventory-file>/oci_inventory.py --host <host's-ip>
```

The script would then return the following variables for the specified host:
```
{
    "availability_domain": "IwGV:US-ASHBURN-AD-1",
    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
    "defined_tags": {},
    "display_name": "ansible-test-instance-448",
    "extended_metadata": {},
    "freeform_tags": {},
    "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
    "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
    "ipxe_script": null,
    "launch_mode": "CUSTOM",
    "launch_options": {
      "boot_volume_type": "ISCSI",
      "firmware": "UEFI_64",
      "network_type": "VFIO",
      "remote_data_volume_type": "ISCSI"
    },
    "lifecycle_state": "AVAILABLE",
    "metadata": {
      "baz": "quux",
      "foo": "bar"
    },
    "region": "iad",
    "shape": "VM.Standard1.1",
    "source_details": {
      "image_id": "ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx",
      "source_type": "image"
    },
    "time_created": "2018-01-16T12:13:35.336000+00:00"
}
```

## FAQs

1. The generated inventory doesn't reflect all the compute instances in my tenancy.

- Check if the OCI user ocid that you are specifying (either via OCI_USER or in the "profile" of your OCI SDK configuration file) has the policy permissions to list those instances. The dynamic inventory script current makes the following API operation calls. Ensure that the [corresponding permissions](https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Reference/corepolicyreference.htm#permissions) are given to the OCI user:
  - ListCompartments
  - ListVNICAttachments
  - GetSubnet
  - GetVCN
  - GetVNIC
  - GetInstance
- The default `OCI_HOSTNAME_FORMAT` is "public_ip" and so the generated inventory would only contain compute instances with public IP. This is useful when your ansible controller node is outside the OCI VCN (as Ansible can only reach instances with public IPs). However if you are running Ansible in a compute instance within your OCI VCN that has access to all subnets within yuor VCN and can reach compute instances with private ips, set `OCI_HOSTNAME_FORMAT` to "private_ip" to fetch nodes with private IPs as well.
