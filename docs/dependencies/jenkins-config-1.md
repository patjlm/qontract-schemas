# /dependencies/jenkins-config-1.yml

**Schema location:** [/dependencies/jenkins-config-1.yml](/schemas/dependencies/jenkins-config-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/jenkins-config-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| instance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | yes |  |  |
| type | string | yes | defaults, global-defaults, views, secrets, base-templates, global-base-templates, job-templates, jobs |  |
| config_path | resourceref | no |  |  |
| config | array | no |  |  |