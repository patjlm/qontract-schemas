# Automated Actions Instance

**Schema location:** [/app-sre/automated-actions-instance-1.yml](/schemas/app-sre/automated-actions-instance-1.yml)

**Description:** Schema for defining instances of automated actions. 
Each instance represents a deployment of automated actions with 
associated metadata, such as name, description, and deployment details.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/automated-actions-instance-1.yml |  |
| labels | labels | no |  |  |
| name | extendedIdentifier | yes |  | The unique name of the automated actions instance. This name is used <br>to identify the instance across the system. |
| description | string | no |  | A brief description of the automated actions instance, explaining its <br>purpose and functionality. |
| deployment | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  | Reference to the OpenShift namespace where the automated actions <br>instance is deployed. This will be replaced by proper URL and token <br>references in the future. |