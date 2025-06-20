# /app-sre/schedule-1.yml

**Schema location:** [/app-sre/schedule-1.yml](/schemas/app-sre/schedule-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/schedule-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| schedule | array of [schedule](#array-schedule) | yes |  |  |

### <a name="array-schedule"></a>schedule
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| start | string | yes |  |  |
| end | string | yes |  |  |
| users | array of $ref to [user-1.yml](/docs/access/user-1.md) | yes |  |  |