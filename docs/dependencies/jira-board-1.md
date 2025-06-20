# /dependencies/jira-board-1.yml

**Schema location:** [/dependencies/jira-board-1.yml](/schemas/dependencies/jira-board-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/jira-board-1.yml |  |
| labels | labels | yes |  |  |
| name | identifier | yes |  |  |
| description | string | yes |  |  |
| server | $ref: [jira-server-1.yml](/docs/dependencies/jira-server-1.md) | yes |  |  |
| severityPriorityMappings | $ref: [jira-severity-priority-mappings-1.yml](/docs/dependencies/jira-severity-priority-mappings-1.md) | yes |  |  |
| slack | [slack](#object-slack) | no |  |  |
| issueType | string | no |  |  |
| issueResolveState | string | no |  |  |
| issueReopenState | string | no |  |  |
| wontFixResolution | string | no |  |  |
| reopenDuration | string | no |  |  |
| disable | [disable](#object-disable) | no |  |  |
| issueFields | array of [issueFields](#array-issueFields) | no |  |  |

### <a name="object-slack"></a>slack
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| workspace | $ref: [slack-workspace-1.yml](/docs/dependencies/slack-workspace-1.md) | yes |  |  |
| channel | string | no |  |  |

### <a name="object-disable"></a>disable
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| integrations | array | no |  |  |

### <a name="array-issueFields"></a>issueField
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | The Jira field name as shown in the UI |
| value | string | yes |  | The value to set the field to as a string as shown in the UI |