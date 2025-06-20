# /openshift/prometheus-rule-1.yml

**Schema location:** [/openshift/prometheus-rule-1.yml](/schemas/openshift/prometheus-rule-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/prometheus-rule-1.yml |  |
| apiVersion | string | yes | monitoring.coreos.com/v1 |  |
| kind | string | yes | PrometheusRule |  |
| metadata | [metadata](#object-metadata) | yes |  |  |
| spec | [spec](#object-spec) | yes |  |  |

### <a name="object-labels"></a>labels
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| prometheus | string | yes | app-sre, quay-aggregation |  |
| role | string | yes | alert-rules, aggregation-rules |  |

### <a name="object-metadata"></a>metadata
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| labels | [labels](#object-labels) | yes |  |  |

### <a name="array-groups"></a>group
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| interval | string | no |  |  |
| rules | array | yes |  |  |

### <a name="object-spec"></a>spec
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| groups | array of [groups](#array-groups) | yes |  |  |