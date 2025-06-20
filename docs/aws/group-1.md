# /aws/group-1.yml

**Schema location:** [/aws/group-1.yml](/schemas/aws/group-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/group-1.yml |  |
| labels | labels | yes |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| policies | array | no |  |  |