# /vault-config/instance-auth-1.yml

**Schema location:** [/vault-config/instance-auth-1.yml](/schemas/vault-config/instance-auth-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /vault-config/instance-auth-1.yml |  |
| provider | string | yes |  |  |
| kubeRoleName | string | no |  |  |
| secretEngine | string | yes | kv_v1, kv_v2 |  |
| roleID | vaultSecret | no |  |  |
| secretID | vaultSecret | no |  |  |
| token | vaultSecret | no |  |  |