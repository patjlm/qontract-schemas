# /app-sre/unleash-instance-1.yml

**Schema location:** [/app-sre/unleash-instance-1.yml](/schemas/app-sre/unleash-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/unleash-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | extendedIdentifier | yes |  |  |
| description | string | yes |  |  |
| url | string | yes |  |  |
| token | vaultSecret | yes |  |  |
| adminToken | vaultSecret | no |  |  |
| allowUnmanagedFeatureToggles | boolean | no |  | Set to true to allow unmanaged/manually created feature toggles |
| notifications | [notifications](#object-notifications) | no |  |  |

### <a name="array-slack"></a>slack
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| workspace | $ref: [slack-workspace-1.yml](/docs/dependencies/slack-workspace-1.md) | yes |  |  |
| channel | string | yes |  |  |
| icon_emoji | string | no |  |  |
| username | string | no |  |  |

### <a name="object-notifications"></a>notifications
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| slack | array of [slack](#array-slack) | no |  |  |