# /aws/elasticache-defaults-1.yml

**Schema location:** [/aws/elasticache-defaults-1.yml](/schemas/aws/elasticache-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/elasticache-defaults-1.yml |  |
| apply_immediately | boolean | no |  | Specifies whether any modifications are applied immediately, or during the next maintenance window. Default: false |
| at_rest_encryption_enabled | boolean | no |  | Specifies whether to enable encryption at rest. |
| auto_minor_version_upgrade | boolean | no |  | Specifies whether minor engine upgrades are applied automatically to the cache cluster during the maintenance window. Default: true |
| automatic_failover_enabled | boolean | no |  | Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails. Default: true |
| availability_zones | array | no |  | List of Availability Zones in which cache nodes are created. terraform attribute: preferred_cache_cluster_azs |
| cluster_mode | [cluster_mode](#object-cluster-mode) | no |  | Enables data partitioning across distinct nodes in a Redis (cluster mode enabled) replication group. |
| engine | string | yes | redis, valkey | The name of the cache engine to be used for the cache clusters in this replication group. |
| engine_version | string | yes |  | The version number of the cache engine to be used for the cache clusters in this replication group. |
| log_delivery_configuration | array | no |  |  |
| maintenance_window | string | no |  | The weekly time range (in UTC) during which system maintenance can occur. Format: ddd:hh24:mi-ddd:hh24:mi |
| multi_az_enabled | boolean | no |  | Specifies whether to enable Multi-AZ Support for the replication group |
| node_type | string | yes |  | Instance class for the cache cluster. See https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html |
| notification_topic_arn | string | no |  | ARN of an SNS topic to send ElastiCache notifications to. |
| number_cache_clusters | integer | no |  | The number of cache clusters (primary and replicas) in this replication group. Terraform attribute: num_cache_clusters |
| parameter_group_name | string | no |  | The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used. |
| port | integer | no |  | The port number on which each of the cache nodes accepts connections. Default: 6379 |
| replication_group_id | string | no |  | The replication group identifier. |
| replication_group_description | string | no |  | The replication group description. Default: 'elasticache cluster' |
| security_group_ids | array | yes |  | List of security group IDs to associate with this replication group. |
| snapshot_retention_limit | integer | no |  | The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them. For zero (0), backups are turned off. |
| snapshot_window | string | no |  | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group. Minimum a 60 minute period. Format: hh24:mi-hh24:mi |
| subnet_group_name | string | no |  | The name of the cache subnet group to be used for the replication group. |
| transit_encryption_enabled | boolean | no |  | Specifies whether to enable encryption in transit. |
| transit_encryption_mode | string | no | preferred, required | Specifies whether to use encryption in transit for the replication group. |
| service_updates_enabled | boolean | no |  | Enable or disable automatic service updates for the ElastiCache cluster. Default: true |
| service_updates_severities | array | no |  | A list of the service update severity levels that can be applied for the replication group. Default: ['critical', 'important'] |
| service_updates_cooldown_days | integer | no |  | The number of days that ElastiCache will wait before applying a service update to the replication group. Default: 14 days for production, 7 days for staging, and 5 days for others. |

### <a name="object-cluster-mode"></a>cluster_mode
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| num_node_groups | integer | yes |  | The number of node groups (shards) for this Redis replication group. Terraform attribute: num_node_groups |
| replicas_per_node_group | integer | no |  | An optional parameter that specifies the number of replica nodes in each node group (shard). Terraform attribute: replicas_per_node_group |