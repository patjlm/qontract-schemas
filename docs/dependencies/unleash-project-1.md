# /dependencies/unleash-project-1.yml

**Schema location:** [/dependencies/unleash-project-1.yml](/schemas/dependencies/unleash-project-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/unleash-project-1.yml |  |
| labels | labels | no |  |  |
| name | string | yes |  | The name of the project. For open-source Unleash it must be "default"! |
| server | $ref: [unleash-instance-1.yml](/docs/app-sre/unleash-instance-1.md) | yes |  |  |