# /aws/parameter-group-1.yml

**Schema location:** [/aws/parameter-group-1.yml](/schemas/aws/parameter-group-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/parameter-group-1.yml |  |
| name | string | no |  |  |
| identifier | string | no |  |  |
| family | string | yes | mysql5.7, mysql8.0, postgres9.6, postgres10, postgres11, postgres12, postgres13, postgres14, postgres15, postgres16, postgres17, redis5.0, redis6.x, valkey7, valkey8 |  |
| description | string | yes |  |  |
| parameters | array of [parameters](#array-parameters) | yes |  |  |

### <a name="array-parameters"></a>parameter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| value | ['string', 'integer', 'number', 'boolean'] | yes |  |  |
| apply_method | string | no | immediate, pending-reboot |  |