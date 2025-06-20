# /aws/quota-limits-1.yml

**Schema location:** [/aws/quota-limits-1.yml](/schemas/aws/quota-limits-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/quota-limits-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| quotas | array of [quotas](#array-quotas) | yes |  |  |

### <a name="array-quotas"></a>quota
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| serviceCode | string | yes |  | Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the ListServices operation. |
| quotaCode | string | yes |  | Specifies the quota identifier. To find the quota code for a specific quota, use the ListServiceQuotas operation, and look for the QuotaCode response in the output for the quota you want. |
| value | number | yes |  | Specifies the new, increased value for the quota. |