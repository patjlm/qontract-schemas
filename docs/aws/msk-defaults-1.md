# /aws/msk-defaults-1.yml

**Schema location:** [/aws/msk-defaults-1.yml](/schemas/aws/msk-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/msk-defaults-1.yml |  |
| kafka_version | string | yes |  |  |
| number_of_broker_nodes | integer | yes |  |  |
| broker_node_group_info | [broker_node_group_info](#object-broker-node-group-info) | yes |  |  |
| server_properties | string | no |  |  |
| open_monitoring | [open_monitoring](#object-open-monitoring) | no |  |  |
| logging_info | [logging_info](#object-logging-info) | no |  |  |
| client_authentication | [client_authentication](#object-client-authentication) | no |  |  |

### <a name="object-broker-node-group-info"></a>broker_node_group_info
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| client_subnets | array | yes |  |  |
| instance_type | string | yes |  |  |
| ebs_volume_size | integer | yes |  |  |
| security_groups | array | yes |  |  |
| az_distribution | string | no | DEFAULT |  |

### <a name="object-jmx-exporter"></a>jmx_exporter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled_in_broker | boolean | yes |  |  |

### <a name="object-node-exporter"></a>node_exporter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled_in_broker | boolean | yes |  |  |

### <a name="object-prometheus"></a>prometheus
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| jmx_exporter | [jmx_exporter](#object-jmx-exporter) | no |  |  |
| node_exporter | [node_exporter](#object-node-exporter) | no |  |  |

### <a name="object-open-monitoring"></a>open_monitoring
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| prometheus | [prometheus](#object-prometheus) | yes |  |  |

### <a name="object-cloudwatch-logs"></a>cloudwatch_logs
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | yes |  |  |
| retention_in_days | integer | yes |  |  |

### <a name="object-broker-logs"></a>broker_logs
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cloudwatch_logs | [cloudwatch_logs](#object-cloudwatch-logs) | no |  |  |

### <a name="object-logging-info"></a>logging_info
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| broker_logs | [broker_logs](#object-broker-logs) | yes |  |  |

### <a name="object-sasl"></a>sasl
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| iam | boolean | no |  |  |
| scram | boolean | no |  |  |

### <a name="object-client-authentication"></a>client_authentication
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| sasl | [sasl](#object-sasl) | no |  |  |