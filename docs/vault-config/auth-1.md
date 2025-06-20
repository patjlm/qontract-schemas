# /vault-config/auth-1.yml

**Schema location:** [/vault-config/auth-1.yml](/schemas/vault-config/auth-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /vault-config/auth-1.yml |  |
| labels | labels | yes |  |  |
| _path | string | yes |  |  |
| type | string | yes | approle, github, oidc, kubernetes |  |
| instance | $ref: [instance-1.yml](/docs/vault-config/instance-1.md) | yes |  |  |
| description | string | yes |  |  |
| settings | [settings](#object-settings) | no |  |  |
| policy_mappings | array of [policy_mappings](#array-policy-mappings) | no |  |  |

### <a name="object-settings"></a>settings
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| config | object | no |  |  |

### <a name="array-policy-mappings"></a>policy_mapping
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| github_team |  | yes | [permission-1.yml](/docs/access/permission-1.md) |  |
| policies | array of $ref to  | yes |  |  |