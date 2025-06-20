# /dependencies/dynatrace-environment-1.yml

**Schema location:** [/dependencies/dynatrace-environment-1.yml](/schemas/dependencies/dynatrace-environment-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/dynatrace-environment-1.yml |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| environmentID | string | yes |  | Dynatrace tenant ID. |
| environmentUrl | string | yes |  | The URL to a specific Dynatrace entity called environment, which is also known as tenant. |
| bootstrapToken | vaultSecret | yes |  | Dynatrace API token dedicated for generating new API tokens for Hypershift. |
| environment | string | no | integration, stage, production | Which of integration, stage or production are the data coming from. |
| dynatraceRegion | string | no |  | https://gitlab.cee.redhat.com/service/app-interface/-/blame/9f303046645ebbb48e87ccf5d89778521a2d8345/data/services/osd-operators/cicd/saas/saas-dynatrace-operator.yaml#L356-433 |
| awsRegion | array | no |  | A list of HCP AWS regions. |