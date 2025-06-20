# /dependencies/dependency-1.yml

**Schema location:** [/dependencies/dependency-1.yml](/schemas/dependencies/dependency-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/dependency-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| statefulness | string | yes | Durable, Cache, Stateless |  |
| opsModel | string | yes | Hosted, External, Internal |  |
| statusPage | string | no |  |  |
| SLA | serviceLevel | yes |  |  |
| dependencyFailureImpact | string | yes | No Impact, Partial Outage, Major Outage, Complete Outage |  |
| monitoring | [monitoring](#object-monitoring) | yes |  |  |

### <a name="object-monitoring"></a>monitoring
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| url | string | no |  |  |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| provider | string | no | resource, resource-template |  |
| path | string | no |  |  |