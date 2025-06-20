# /app-sre/pipelines-provider-1.yml

**Schema location:** [/app-sre/pipelines-provider-1.yml](/schemas/app-sre/pipelines-provider-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/pipelines-provider-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| provider | string | yes | tekton |  |
| defaults | crossref | no |  | Pipeline provider defaults |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| retention |  | no |  | Describes the amount of builds that will be kept |
| taskTemplates | array | no |  |  |
| pipelineTemplates |  | no |  |  |
| deployResources |  | no |  |  |