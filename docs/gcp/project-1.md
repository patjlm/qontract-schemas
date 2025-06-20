# /gcp/project-1.yml

**Schema location:** [/gcp/project-1.yml](/schemas/gcp/project-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /gcp/project-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| managedTeams | array | no |  |  |
| description | string | yes |  |  |
| automationToken | vaultSecret | no |  |  |
| gcrPushCredentials | vaultSecret | no |  |  |
| artifactPushCredentials | vaultSecret | no |  |  |