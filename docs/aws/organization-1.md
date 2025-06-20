# /aws/organization-1.yml

**Schema location:** [/aws/organization-1.yml](/schemas/aws/organization-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /aws/organization-1.yml |  |
| payerAccount | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  | AWS parent account |
| ou | path | yes |  | AWS organizational unit. Use path to the OU, e.g. /Root/OrgUnit1/Foo/Bar |
| tags | labels | no |  | Tags for this account |