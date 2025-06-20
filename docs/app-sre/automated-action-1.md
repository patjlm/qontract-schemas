# Automated Action

**Schema location:** [/app-sre/automated-action-1.yml](/schemas/app-sre/automated-action-1.yml)

**Description:** Schema for defining automated actions. Automated actions
represent predefined operations that can be executed programmatically,
with configurable retries, operation limits, and descriptions.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/automated-action-1.yml |  |
| labels | labels | no |  |  |
| type | string | yes |  | The automated action type, which indicates the kind of operation<br>being performed. |
| description | string | no |  | A brief description of the automated action, explaining its purpose<br>and functionality. |
| instances | array of $ref to [automated-actions-instance-1.yml](/docs/app-sre/automated-actions-instance-1.md) | yes |  | A list of instances where the automated action can be executed. |
| maxOps | number | yes |  | The maximum number of operations that can be performed per hour. This<br>is used to limit the frequency of the automated action to prevent<br>overloading systems or exceeding quotas. |
| arguments | array of [arguments](#array-arguments) | no |  | Action arguments that can be used to customize the behavior of the action. |

### <a name="array-arguments"></a>argument
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| action_user | string | no |  | The user filter for the action list. |
| max_age_minutes | integer | no |  | The maximum age of actions to include in the list, in minutes. |
| identifier | string | no |  | The RDS identifier regex pattern to match. |
| kind | string | no |  | The kind regex pattern to match. |
| name | string | no |  | The name regex pattern to match. |