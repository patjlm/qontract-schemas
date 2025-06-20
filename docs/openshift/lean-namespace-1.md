# /openshift/lean-namespace-1.yml

**Schema location:** [/openshift/lean-namespace-1.yml](/schemas/openshift/lean-namespace-1.yml)

**Description:** a lean definition of a namespace in a cluster with an automation token and some context in the form of an environment

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/lean-namespace-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| cluster | [cluster](#object-cluster) | yes |  |  |
| environment | [environment](#object-environment) | yes |  |  |

### <a name="object-cluster"></a>cluster
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| serverUrl | string | yes |  |  |
| automationToken | vaultSecret | yes |  |  |

### <a name="object-environment"></a>environment
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| parameters | object | no |  |  |