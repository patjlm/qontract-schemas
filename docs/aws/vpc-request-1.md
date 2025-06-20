# /aws/vpc-request-1.yml

**Schema location:** [/aws/vpc-request-1.yml](/schemas/aws/vpc-request-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/vpc-request-1.yml |  |
| labels | labels | no |  |  |
| identifier | longIdentifier | yes |  |  |
| region | string | yes |  |  |
| description | string | no |  |  |
| delete | boolean | no |  |  |
| cidr_block | crossref | yes |  | Reference to a network reservation file |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  |  |
| subnets | [subnets](#object-subnets) | no |  |  |

### <a name="object-subnets"></a>subnets
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| private | array | no |  | Private subnets CIDR blocks. |
| public | array | no |  | Public subnets CIDR blocks. |
| availability_zones | array | no |  | A list of availability zones names in the region. |