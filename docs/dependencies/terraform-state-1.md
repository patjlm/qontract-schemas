# /dependencies/terraform-state-1.yml

**Schema location:** [/dependencies/terraform-state-1.yml](/schemas/dependencies/terraform-state-1.yml)

**Description:** bucket properties for each integration

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/terraform-state-1.yml |  |
| provider | string | no | s3 |  |
| bucket | string | no |  |  |
| region | string | no |  |  |
| integrations | array of [integrations](#array-integrations) | no |  | holds information which bucket key stores the terraform state per integration |

### <a name="array-integrations"></a>integration
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| integration | string | no |  |  |
| key | string | no |  |  |