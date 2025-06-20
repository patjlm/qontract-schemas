# /openshift/namespace-1.yml

**Schema location:** [/openshift/namespace-1.yml](/schemas/openshift/namespace-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/namespace-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| delete | boolean | no |  |  |
| description | string | yes |  |  |
| enableDynatraceLogging | boolean | no |  |  |
| grafanaUrl | string | no |  |  |
| cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| environment | $ref: [environment-1.yml](/docs/app-sre/environment-1.md) | yes |  |  |
| limitRanges | $ref: [limitrange-1.yml](/docs/openshift/limitrange-1.md) | no |  |  |
| quota | $ref: [quota-1.yml](/docs/openshift/quota-1.md) | no |  |  |
| networkPoliciesAllow | array of $ref to [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| clusterAdmin | boolean | no |  |  |
| managedRoles | boolean | no |  |  |
| managedResourceTypes | array | no |  |  |
| managedResourceTypeOverrides | array of [managedResourceTypeOverrides](#array-managedResourceTypeOverrides) | no |  |  |
| managedResourceNames | array | no |  |  |
| sharedResources | array of $ref to [shared-resources-1.yml](/docs/openshift/shared-resources-1.md) | no |  |  |
| skupperSite | [skupperSite](#object-skupperSite) | no |  |  |
| openshiftResources | array | no |  |  |
| managedExternalResources | boolean | no |  | are external resources managed for this namespace |
| externalResources | array | no |  | external resources to provision for this namespace |
| openshiftServiceAccountTokens | array of [openshiftServiceAccountTokens](#array-openshiftServiceAccountTokens) | no |  |  |
| glitchtipProjects | array of $ref to [glitchtip-project-1.yml](/docs/dependencies/glitchtip-project-1.md) | no |  |  |
| kafkaCluster | $ref: [cluster-1.yml](/docs/kafka/cluster-1.md) | no |  |  |

### <a name="array-managedResourceTypeOverrides"></a>managedResourceTypeOverride
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| resource | string | no |  |  |
| override | string | no |  |  |

### <a name="object-skupperSite"></a>skupperSite
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| network | $ref: [skupper-network-1.yml](/docs/dependencies/skupper-network-1.md) | yes |  |  |
| delete | boolean | no |  |  |
| siteControllerTemplates | array | no |  |  |

### <a name="array-openshiftServiceAccountTokens"></a>openshiftServiceAccountToken
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | no |  |  |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| serviceAccountName | string | yes |  |  |