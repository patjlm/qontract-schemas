# Environment

**Schema location:** [/app-sre/environment-1.yml](/schemas/app-sre/environment-1.yml)

**Description:** Schema for defining environments in an app-interface instance. 
Environments represent logical groupings of resources and configurations for applications, 
including their name, description, product association, parameters, and dependencies.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/environment-1.yml |  |
| labels | labels | yes |  |  |
| name | extendedIdentifier | yes |  | The unique name of the environment. |
| description | string | yes |  | A detailed description of the environment, explaining its purpose <br>and scope. |
| product | $ref: [product-1.yml](/docs/app-sre/product-1.md) | yes |  | Reference to the product associated with the environment. |
| parameters | object | no |  | A set of key-value pairs representing environment-level parameters. <br>These parameters are used to configure the environment. |
| secretParameters | array | no |  | A list of environment-level parameters sourced from vault secrets. |
| dependsOn | $ref: [environment-1.yml](/docs/app-sre/environment-1.md) | no |  | Reference to another environment that this environment depends on. <br>This is used to define dependencies between environments. |