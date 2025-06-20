# /dependencies/jira-severity-priority-mappings-1.yml

**Schema location:** [/dependencies/jira-severity-priority-mappings-1.yml](/schemas/dependencies/jira-severity-priority-mappings-1.yml)

**Description:** mappings between alert severities and jira ticket priorities

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/jira-severity-priority-mappings-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| mappings | array of [mappings](#array-mappings) | yes |  |  |

### <a name="array-mappings"></a>mapping
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| severity | string | yes |  | alert severity |
| priority | string | yes |  | ticket priority |