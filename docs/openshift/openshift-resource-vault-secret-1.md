# /openshift/openshift-resource-vault-secret-1.yml

**Schema location:** [/openshift/openshift-resource-vault-secret-1.yml](/schemas/openshift/openshift-resource-vault-secret-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/openshift-resource-vault-secret-1.yml |  |
| provider | string | no | vault-secret |  |
| name | string | no |  |  |
| path | vaultSecretPath | yes |  |  |
| version | integer | yes |  |  |
| labels | labels | no |  |  |
| annotations | annotations | no |  |  |
| type | string | no | Opaque, kubernetes.io/dockercfg, kubernetes.io/dockerconfigjson, kubernetes.io/tls, kubernetes.io/ssh-auth |  |
| validate_alertmanager_config | boolean | no |  |  |
| alertmanager_config_key | string | no |  |  |