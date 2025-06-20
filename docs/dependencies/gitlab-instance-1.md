# /dependencies/gitlab-instance-1.yml

**Schema location:** [/dependencies/gitlab-instance-1.yml](/schemas/dependencies/gitlab-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/gitlab-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| backupOrgs | array | no |  |  |
| managedGroups | array | yes |  |  |
| projectRequests | array of [projectRequests](#array-projectRequests) | no |  |  |
| description | string | yes |  |  |
| url | string | yes |  |  |
| token | vaultSecret | no |  |  |
| sslVerify | boolean | no |  |  |

### <a name="array-projectRequests"></a>projectRequest
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| group | string | yes | service |  |
| projects | array | yes |  |  |