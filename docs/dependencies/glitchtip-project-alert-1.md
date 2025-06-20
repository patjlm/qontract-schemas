# /dependencies/glitchtip-project-alert-1.yml

**Schema location:** [/dependencies/glitchtip-project-alert-1.yml](/schemas/dependencies/glitchtip-project-alert-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/glitchtip-project-alert-1.yml |  |
| labels | labels | no |  |  |
| name | identifier | yes |  |  |
| description | string | yes |  |  |
| quantity | positiveInteger | yes |  |  |
| timespanMinutes | positiveInteger | yes |  |  |
| recipients | array of [recipients](#array-recipients) | yes |  |  |

### <a name="array-recipients"></a>recipient
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | no |  |  |
| url | string | no |  |  |
| urlSecret | vaultSecret | no |  |  |