# /access/user-1.yml

**Schema location:** [/access/user-1.yml](/schemas/access/user-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/user-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| org_username | identifier | yes |  |  |
| github_username | identifier | yes |  |  |
| quay_username | identifier | no |  |  |
| slack_username | string | no |  |  |
| pagerduty_username | string | no |  |  |
| aws_username | string | no |  |  |
| cloudflare_user | string | no |  |  |
| roles | array of $ref to [role-1.yml](/docs/access/role-1.md) | no |  |  |
| public_gpg_key | string | no |  |  |
| tag_on_merge_requests | boolean | no |  |  |
| tag_on_cluster_updates | boolean | no |  |  |