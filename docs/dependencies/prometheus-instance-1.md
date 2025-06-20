# /dependencies/prometheus-instance-1.yml

**Schema location:** [/dependencies/prometheus-instance-1.yml](/schemas/dependencies/prometheus-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/prometheus-instance-1.yml |  |
| labels | labels | no |  |  |
| name | identifier | yes |  |  |
| description | string | no |  |  |
| baseUrl | string | yes |  |  |
| queryPath | string | no |  |  |
| auth | [auth](#object-auth) | yes |  |  |

### <a name="object-auth"></a>auth
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | no | bearer, oidc |  |
| token | vaultSecret | no |  |  |
| accessTokenClientId | string | no |  |  |
| accessTokenUrl | string | no |  |  |
| accessTokenClientSecret | vaultSecret | no |  |  |