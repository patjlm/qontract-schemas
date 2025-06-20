# /app-sre/slo-document-1.yml

**Schema location:** [/app-sre/slo-document-1.yml](/schemas/app-sre/slo-document-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/slo-document-1.yml |  |
| labels | labels | yes |  |  |
| name | identifier | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| namespaces | array of [namespaces](#array-namespaces) | yes |  |  |
| slos | array of [slos](#array-slos) | yes |  |  |

### <a name="object-prometheusAccess"></a>prometheusAccess
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| url | string | yes |  |  |
| username | vaultSecret | no |  |  |
| password | vaultSecret | no |  |  |

### <a name="array-namespaces"></a>namespace
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| SLONamespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  | This field is used to determine in which namespace PrometheusRule<br>object that contain the alerts generated from the expressions of<br>this SLO document is going to be created. Those alerts are being<br>used in the slo-to-status-board flow:<br>https://gitlab.cee.redhat.com/service/app-interface/-/blob/master/docs/status-board/statusboard-alertmanager-receiver.md<br><br>If omitted, the rules will be generated in the namespace<br>observabilityNamespace of the cluster to which the `namespace` of<br>this SLO document belongs to. |
| prometheusAccess | [prometheusAccess](#object-prometheusAccess) | no |  |  |

### <a name="object-SLOParameters"></a>SLOParameters
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| window | string | yes |  |  |

### <a name="array-slos"></a>slo
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| SLIType | string | yes | latency, availability, correctness, quality, freshness, coverage, correcteness, throughput, durability | SLI type. See https://sre.google/workbook/implementing-slos/ for details |
| SLISpecification | string | yes |  | SLI specification, e.g 'The proportion of valid requests served successfully' |
| SLODetails | string | yes |  | Thorough description of this SLO. Do not use a Google doc for this. It must contain<br>  * SLI description - What do we want to measure<br>  * SLI rationale -  Why do we want to measure it<br>  * Implementation details - How do we want to measure it<br>  * SLO rationale - Why we have chosen the targets<br>  * Alerting: How we are doing it on top of our SLIs/SLOs |
| SLOTargetUnit | string | yes | percent_0_1, percent_0_100 | Unit in which the 'expr' and 'SLOTarget' will be expressed:<br>  * Use 'percentage_0_1' if the your PromQL query is going to return values for 0 to 1<br>  * Use 'percentage_0_100' if the your PromQL query is going to return values for 0 to 100 |
| SLOParameters | [SLOParameters](#object-SLOParameters) | yes |  |  |
| expr |  | yes |  | Prometheus expression to calculate the SLO. It should be expressed<br>in the units of the 'SLOTargetUnit'. It will be processed with jinja,<br>with the SLOParameters as input. |
| SLOTarget | number | yes |  | SLO target. It should be expressed by means of the 'SLOTargetUnit' field |
| prometheusRules | string | yes |  | Location of the prometheus rules associated to this SLO definition<br>(currently only a path in app-interface) |
| prometheusRulesTests | string | no |  | Location of the prometheus rules tests for the prometheus rules |
| dashboard | string | yes |  | Related grafana dashboard |