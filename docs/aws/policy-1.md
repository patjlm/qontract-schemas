# /aws/policy-1.yml

**Schema location:** [/aws/policy-1.yml](/schemas/aws/policy-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/policy-1.yml |  |
| labels | labels | yes |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| name | awsPolicyName | yes |  |  |
| description | string | yes |  |  |
| mandatory | boolean | no |  | is policy mandatory in the account |
| policy | object | yes |  |  |