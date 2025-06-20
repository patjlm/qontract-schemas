# /aws/asg-defaults-1.yml

**Schema location:** [/aws/asg-defaults-1.yml](/schemas/aws/asg-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/asg-defaults-1.yml |  |
| max_size | integer | yes |  |  |
| min_size | integer | yes |  |  |
| iam_role_name | string | no |  |  |
| instance_types | array | no |  |  |
| vpc_zone_identifier | array | no |  |  |
| capacity_rebalance | boolean | no |  |  |
| max_instance_lifetime | integer | no |  |  |
| protect_from_scale_in | boolean | no |  |  |
| enabled_metrics | array | no |  |  |
| instances_distribution | [instances_distribution](#object-instances-distribution) | no |  |  |
| instance_refresh_preferences | [instance_refresh_preferences](#object-instance-refresh-preferences) | no |  |  |
| vpc_security_group_ids | array | no |  |  |
| update_default_version | boolean | no |  |  |
| block_device_mappings | array of [block_device_mappings](#array-block-device-mappings) | no |  |  |
| instance_requirements | [instance_requirements](#object-instance-requirements) | no |  |  |

### <a name="object-instances-distribution"></a>instances_distribution
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| spot_allocation_strategy | string | no | lowest-price, price-capacity-optimized, capacity-optimized, capacity-optimized-prioritized |  |
| on_demand_base_capacity | integer | no |  |  |
| on_demand_percentage_above_base_capacity | integer | no |  |  |
| spot_instance_pools | integer | no |  |  |

### <a name="object-instance-refresh-preferences"></a>instance_refresh_preferences
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| instance_warmup | integer | no |  |  |
| min_healthy_percentage | integer | no |  |  |

### <a name="object-ebs"></a>ebs
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| volume_size | integer | no |  |  |
| volume_type | string | no | standard, gp2, gp3, io1, io2, sc1, st1 |  |
| encrypted | boolean | no |  |  |

### <a name="array-block-device-mappings"></a>block_device_mapping
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| device_name | string | no |  |  |
| ebs | [ebs](#object-ebs) | no |  |  |

### <a name="object-vcpu-count"></a>vcpu_count
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| min | integer | no |  |  |
| max | integer | no |  |  |

### <a name="object-instance-requirements"></a>instance_requirements
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| vcpu_count | [vcpu_count](#object-vcpu-count) | no |  |  |
| memory_mib |  | no |  |  |
| excluded_instance_types | array | no |  |  |