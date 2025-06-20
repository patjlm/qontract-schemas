# /vault-config/secret-engine-1.yml

**Schema location:** [/vault-config/secret-engine-1.yml](/schemas/vault-config/secret-engine-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /vault-config/secret-engine-1.yml |  |
| labels | labels | yes |  |  |
| _path | string | yes |  |  |
| type | string | yes | kv, totp |  |
| instance | $ref: [instance-1.yml](/docs/vault-config/instance-1.md) | yes |  |  |
| description | string | yes |  |  |
| options | object | no |  |  |