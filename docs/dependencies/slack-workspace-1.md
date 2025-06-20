# /dependencies/slack-workspace-1.yml

**Schema location:** [/dependencies/slack-workspace-1.yml](/schemas/dependencies/slack-workspace-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/slack-workspace-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| token | vaultSecret | yes |  |  |
| api_client | [api_client](#object-api-client) | no |  |  |
| integrations | array of [integrations](#array-integrations) | no |  |  |
| managedUsergroups | array | no |  |  |

### <a name="object-global"></a>global
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| max_retries | integer | no |  |  |
| timeout | integer | no |  |  |

### <a name="array-methods"></a>method
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| args | object | yes |  |  |

### <a name="object-api-client"></a>api_client
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| global | [global](#object-global) | no |  |  |
| methods | array of [methods](#array-methods) | no |  |  |

### <a name="array-integrations"></a>integration
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |