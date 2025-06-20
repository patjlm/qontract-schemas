# /app-sre/tekton-task-template-1.yml

**Schema location:** [/app-sre/tekton-task-template-1.yml](/schemas/app-sre/tekton-task-template-1.yml)

**Description:** Properties of tekton task templates deployed in tekton pipelines providers
namespaces


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/tekton-task-template-1.yml |  |
| name | string | yes |  |  |
| type | string | yes | onePerSaasFile, onePerNamespace |  |
| path | string | yes |  |  |
| variables | object | no |  |  |