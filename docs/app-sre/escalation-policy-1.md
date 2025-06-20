# /app-sre/escalation-policy-1.yml

**Schema location:** [/app-sre/escalation-policy-1.yml](/schemas/app-sre/escalation-policy-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/escalation-policy-1.yml |  |
| labels | labels | no |  |  |
| name | extendedIdentifier | yes |  |  |
| description | string | yes |  |  |
| channels | [channels](#object-channels) | yes |  |  |

### <a name="object-channels"></a>channels
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| slackUserGroup | array of $ref to [permission-1.yml](/docs/access/permission-1.md) | yes |  |  |
| email | array | yes |  |  |
| pagerduty | $ref: [pagerduty-target-1.yml](/docs/dependencies/pagerduty-target-1.md) | no |  |  |
| jiraBoard | array of $ref to [jira-board-1.yml](/docs/dependencies/jira-board-1.md) | yes |  |  |
| jiraComponents | array | no |  | components to set on jira tickets |
| jiraLabels | array | no |  | labels to add on jira tickets |
| nextEscalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | no |  |  |