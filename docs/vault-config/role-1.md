# /vault-config/role-1.yml

**Schema location:** [/vault-config/role-1.yml](/schemas/vault-config/role-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /vault-config/role-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| mount | $ref: [auth-1.yml](/docs/vault-config/auth-1.md) | yes |  |  |
| type | string | yes |  |  |
| instance | $ref: [instance-1.yml](/docs/vault-config/instance-1.md) | yes |  |  |
| output_path | string | no |  |  |
| options | [options](#object-options) | yes |  |  |

### <a name="object-options"></a>options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| policies | array of $ref to [policy-1.yml](/docs/vault-config/policy-1.md) | no |  |  |
| token_policies | array of $ref to [policy-1.yml](/docs/vault-config/policy-1.md) | no |  |  |