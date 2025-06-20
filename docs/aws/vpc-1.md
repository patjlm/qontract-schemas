# /aws/vpc-1.yml

**Schema location:** [/aws/vpc-1.yml](/schemas/aws/vpc-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/vpc-1.yml |  |
| labels | labels | yes |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| vpc_id | string | yes |  |  |
| cidr_block | string | yes |  |  |
| region | string | yes |  |  |
| subnets | array of [subnets](#array-subnets) | no |  |  |

### <a name="array-subnets"></a>subnet
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| id | string | yes |  |  |
| privacy | string | no |  |  |