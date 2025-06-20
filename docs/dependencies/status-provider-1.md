# /dependencies/status-provider-1.yml

**Schema location:** [/dependencies/status-provider-1.yml](/schemas/dependencies/status-provider-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/status-provider-1.yml |  |
| provider | string | yes |  |  |
| prometheusAlerts | [prometheusAlerts](#object-prometheusAlerts) | no |  |  |
| manual | [manual](#object-manual) | no |  |  |
| maintenance | $ref: [maintenance-1.yml](/docs/app-sre/maintenance-1.md) | no |  |  |

### <a name="object-matchExpression"></a>matchExpression
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| alert | string | no |  |  |
| labels | labels | no |  |  |

### <a name="array-matchers"></a>matcher
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| matchExpression | [matchExpression](#object-matchExpression) | yes |  |  |
| componentStatus | statusPageStatus | yes |  |  |

### <a name="object-prometheusAlerts"></a>prometheusAlerts
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| matchers | array of [matchers](#array-matchers) | yes |  |  |

### <a name="object-manual"></a>manual
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| componentStatus | string | yes |  |  |
| from | string | no |  |  |
| until | string | no |  |  |