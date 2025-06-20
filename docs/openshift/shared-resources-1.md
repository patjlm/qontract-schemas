# /openshift/shared-resources-1.yml

**Schema location:** [/openshift/shared-resources-1.yml](/schemas/openshift/shared-resources-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/shared-resources-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| openshiftResources | array | yes |  |  |
| openshiftServiceAccountTokens | array of [openshiftServiceAccountTokens](#array-openshiftServiceAccountTokens) | no |  |  |
| glitchtipProjects | array of $ref to [glitchtip-project-1.yml](/docs/dependencies/glitchtip-project-1.md) | no |  |  |

### <a name="array-openshiftServiceAccountTokens"></a>openshiftServiceAccountToken
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | no |  |  |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| serviceAccountName | string | yes |  |  |