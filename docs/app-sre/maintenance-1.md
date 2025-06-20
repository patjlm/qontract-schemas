# /app-sre/maintenance-1.yml

**Schema location:** [/app-sre/maintenance-1.yml](/schemas/app-sre/maintenance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/maintenance-1.yml |  |
| name | string | yes |  | the name of the maintenance |
| message | string | yes |  | a message describing the maintenance |
| affectedServices | array of $ref to [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| scheduledStart | string | yes |  |  |
| scheduledEnd | string | yes |  |  |
| announcements | array of [announcements](#array-announcements) | no |  |  |

### <a name="array-announcements"></a>announcement
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | yes | statuspage |  |
| page | $ref: [status-page-1.yml](/docs/dependencies/status-page-1.md) | no |  |  |
| remindSubscribers | boolean | no |  |  |
| notifySubscribersOnStart | boolean | no |  |  |
| notifySubscribersOnCompletion | boolean | no |  |  |