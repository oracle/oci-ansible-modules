# OCI Ansible Modules Known Issues

1. Use of `exact_count` with `enable_parallel_requests=True` in `oci_instance` sometimes results in a play execution hanging

When an error occurs during instance provisioning, when `enable_parallel_requests` is set to `True` and an `exact_count` is specified in `oci_instance`, the play execution sometimes hangs. This is a known issue and is tracked through [issue #16](https://github.com/oracle/oci-ansible-modules/issues/16). A list of workarounds is documented in [the issue](https://github.com/oracle/oci-ansible-modules/issues/16#issuecomment-447619908)
