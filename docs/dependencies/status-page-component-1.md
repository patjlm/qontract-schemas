# /dependencies/status-page-component-1.yml

**Schema location:** [/dependencies/status-page-component-1.yml](/schemas/dependencies/status-page-component-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/status-page-component-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| displayName | string | yes |  |  |
| description | string | no |  |  |
| instructions | string | yes |  |  |
| groupName | string | no |  |  |
| page | $ref: [status-page-1.yml](/docs/dependencies/status-page-1.md) | yes |  |  |
| status | array | no |  | a list of providers that can influence the status of this<br>status page component |