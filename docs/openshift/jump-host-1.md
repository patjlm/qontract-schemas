# /openshift/jump-host-1.yml

**Schema location:** [/openshift/jump-host-1.yml](/schemas/openshift/jump-host-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/jump-host-1.yml |  |
| labels | labels | yes |  |  |
| hostname | string | yes |  |  |
| knownHosts | resourceref | yes |  |  |
| user | string | yes |  |  |
| port | integer | no |  |  |
| remotePort | integer | no |  |  |
| identity | vaultSecret | yes |  |  |