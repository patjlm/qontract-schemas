# App Interface Query Validation

**Schema location:** [/app-interface/query-validation-1.yml](/schemas/app-interface/query-validation-1.yml)

**Description:** Schema for defining query validation configurations in app-interface. 
This includes details about the queries to validate, escalation policies, 
and associated resources.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/query-validation-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | A unique name for the query validation configuration. |
| description | string | yes |  | A description of the queries included in the file. |
| escalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | yes |  | Reference to the escalation policy to be used if validation fails. |
| queries | array of [queries](#array-queries) | yes |  | A list of queries to validate. |
| resources | array | no |  | A list of resources associated with the query validation. |

### <a name="array-queries"></a>query
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | resourceref | yes |  | The path to the resource query to be tested. |