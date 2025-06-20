# /dependencies/dns-record-1.yml

**Schema location:** [/dependencies/dns-record-1.yml](/schemas/dependencies/dns-record-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/dns-record-1.yml |  |
| name | string | yes |  |  |
| type | string | yes | A, AAAA, CNAME, MX, NS, SPF, SRV, TXT |  |
| ttl | integer | no |  |  |
| alias | [alias](#object-alias) | no |  |  |
| weighted_routing_policy | [weighted_routing_policy](#object-weighted-routing-policy) | no |  |  |
| geolocation_routing_policy | object | no |  |  |
| set_identifier | string | no |  |  |
| records | array | no |  |  |
| failover_routing_policy | [failover_routing_policy](#object-failover-routing-policy) | no |  |  |
| _healthcheck | [_healthcheck](#object--healthcheck) | no |  |  |
| _target_cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  |  |
| _target_namespace_zone | [_target_namespace_zone](#object--target-namespace-zone) | no |  | a namespace and a route53 zone name provisioned within that namespace |
| _records_from_vault | array of [_records_from_vault](#array--records-from-vault) | no |  |  |

### <a name="object-alias"></a>alias
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| zone_id | string | yes |  |  |
| evaluate_target_health | boolean | yes |  |  |

### <a name="object-weighted-routing-policy"></a>weighted_routing_policy
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| weight | integer | no |  |  |

### <a name="object-failover-routing-policy"></a>failover_routing_policy
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | no | PRIMARY, SECONDARY |  |

### <a name="object--healthcheck"></a>_healthcheck
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| fqdn | string | no |  |  |
| port | integer | no |  |  |
| type | string | no | HTTP, HTTPS, HTTP_STR_MATCH, HTTPS_STR_MATCH, TCP |  |
| resource_path | string | no |  |  |
| failure_threshold | integer | no |  |  |
| request_interval | integer | no |  |  |
| search_string | string | no |  |  |

### <a name="object--target-namespace-zone"></a>_target_namespace_zone
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| name | k8sValidContainerName | yes |  |  |

### <a name="array--records-from-vault"></a>_records_from_vault
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | string | yes |  |  |
| field | string | yes |  |  |
| key | string | no |  |  |
| version | integer | no |  |  |