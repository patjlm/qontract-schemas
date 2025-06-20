# /access/external-user-1.yml

**Schema location:** [/access/external-user-1.yml](/schemas/access/external-user-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/external-user-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| github_username | identifier | no |  |  |
| quay_username | identifier | no |  |  |
| sponsors | array of $ref to [user-1.yml](/docs/access/user-1.md) | yes |  |  |
| roles | array of $ref to [role-1.yml](/docs/access/role-1.md) | no |  |  |