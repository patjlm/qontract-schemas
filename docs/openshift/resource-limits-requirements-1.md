# /openshift/resource-limits-requirements-1.yml

**Schema location:** [/openshift/resource-limits-requirements-1.yml](/schemas/openshift/resource-limits-requirements-1.yml)

**Description:** CPU and memory resources requirements to be set in pods limits configuration


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/resource-limits-requirements-1.yml |  |
| cpu | k8sResourceRequirementQuantity | no |  |  |
| memory | k8sResourceRequirementQuantity | yes |  |  |