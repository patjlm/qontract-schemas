# /dependencies/acs-instance-1.yml

**Schema location:** [/dependencies/acs-instance-1.yml](/schemas/dependencies/acs-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/acs-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| url | string | yes |  |  |
| credentials | vaultSecret | yes |  |  |
| authProvider | [authProvider](#object-authProvider) | yes |  |  |

### <a name="object-authProvider"></a>authProvider
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | no |  |  |
| id | string | no |  |  |
| kind |  | no | oidc |  |