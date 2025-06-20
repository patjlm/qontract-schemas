# App Interface Slack Notification

**Schema location:** [/app-interface/app-interface-slack-notification-1.yml](/schemas/app-interface/app-interface-slack-notification-1.yml)

**Description:** Schema for defining a single Slack notification message. 
Notifications can be sent to specific channels or users.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/app-interface-slack-notification-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the Slack notification object. |
| subject | nonEmptyString | yes |  | The subject or title of the Slack notification message. |
| channel | nonEmptyString | no |  | The Slack channel where the notification will be sent. |
| to | [to](#object-to) | yes |  | Recipients of the Slack notification. |
| body | nonEmptyString | yes |  | The body content of the Slack notification message. |

### <a name="object-to"></a>to
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| users | array | no |  | List of Slack users who will receive the notification. |