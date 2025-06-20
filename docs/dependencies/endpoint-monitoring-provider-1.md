# /dependencies/endpoint-monitoring-provider-1.yml

**Schema location:** [/dependencies/endpoint-monitoring-provider-1.yml](/schemas/dependencies/endpoint-monitoring-provider-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/endpoint-monitoring-provider-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| provider | string | yes | blackbox-exporter, signalfx | The provider defines which monitoring implementation will be used for endpoints |
| timeout | string | no |  | Timeout for the monitoring check, e.g. 10s |
| checkInterval | string | no |  | Interval between endpoint checks, e.g. 10s |
| metricLabels | prometheusLabels | no |  | Labels to be added to the resulting Prometheus metrics |
| blackboxExporter | [blackboxExporter](#object-blackboxExporter) | no |  | blackbox-exporter specific configuration options |
| signalFx | [signalFx](#object-signalFx) | no |  | signalfx exporter specific configuration options |

### <a name="object-blackboxExporter"></a>blackboxExporter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| module | string | yes |  | the blackbox exporter module to use for the endpoint check, e.g. http_2xx |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  | the namespace where the prometheus Probe CR will be created |
| exporterUrl | string | yes |  | the blackbox-exporter URL to use, must be a full scrape URL |

### <a name="object-signalFx"></a>signalFx
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  | the namespace where the prometheus Probe CR will be created |
| exporterUrl | string | yes |  | the signalfx-prometheus-exporter URL to use, must be a full scrape URL |
| targetFilterLabel | string | yes |  | the signalfx label that holds the target value to be filtered on |