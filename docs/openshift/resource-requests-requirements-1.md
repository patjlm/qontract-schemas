# /openshift/resource-requests-requirements-1.yml

**Schema location:** [/openshift/resource-requests-requirements-1.yml](/schemas/openshift/resource-requests-requirements-1.yml)

**Description:** CPU and memory resources requirements to be set in pods requests
configuration


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/resource-requests-requirements-1.yml |  |
| cpu | k8sResourceRequirementQuantity | yes |  |  |
| memory | k8sResourceRequirementQuantity | yes |  |  |