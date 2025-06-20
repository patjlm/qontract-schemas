# /dependencies/glitchtip-instance-1.yml

**Schema location:** [/dependencies/glitchtip-instance-1.yml](/schemas/dependencies/glitchtip-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/glitchtip-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | identifierLowercase64 | yes |  |  |
| description | string | yes |  |  |
| consoleUrl | string | yes |  |  |
| automationUserEmail | vaultSecret | yes |  |  |
| automationToken | vaultSecret | yes |  |  |
| readTimeout | integer | no |  |  |
| maxRetries | integer | no |  |  |
| mailDomain | string | no |  |  |
| glitchtipJiraBridgeAlertUrl | string | no |  |  |
| glitchtipJiraBridgeToken | vaultSecret | no |  |  |