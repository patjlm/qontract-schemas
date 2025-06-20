# /aws/rds-defaults-1.yml

**Schema location:** [/aws/rds-defaults-1.yml](/schemas/aws/rds-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/rds-defaults-1.yml |  |
| engine | string | yes | postgres, mysql |  |
| engine_version | string | yes |  |  |
| name | string | no |  |  |
| username | string | no |  |  |
| port | integer | no |  |  |
| instance_class | string | yes |  |  |
| allocated_storage | integer | no |  |  |
| max_allocated_storage | integer | no |  |  |
| storage_encrypted | boolean | no |  |  |
| auto_minor_version_upgrade | boolean | yes | False |  |
| skip_final_snapshot | boolean | no |  |  |
| backup_retention_period | integer | no |  |  |
| storage_type | string | no | gp3, io1, io2 |  |
| multi_az | boolean | no |  |  |
| db_subnet_group_name | string | no |  |  |
| vpc_security_group_ids | array | no |  |  |
| enabled_cloudwatch_logs_exports | array | no |  |  |
| backup_window | string | no |  |  |
| copy_tags_to_snapshot | boolean | no |  |  |
| monitoring_interval | integer | no |  |  |
| performance_insights_enabled | boolean | no |  |  |
| maintenance_window | string | no |  |  |
| kms_key_id | string | no |  |  |
| deletion_protection | boolean | no |  |  |
| option_group_name | string | no |  |  |
| license_model | string | no |  |  |
| allow_major_version_upgrade | boolean | no |  |  |
| iops | integer | no |  |  |
| storage_throughput | integer | no |  |  |
| publicly_accessible | boolean | no |  |  |
| ca_cert_identifier | string | no | rds-ca-2019, rds-ca-rsa2048-g1, rds-ca-rsa4096-g1, rds-ca-ecc384-g1 |  |
| timeouts | [timeouts](#object-timeouts) | no |  |  |

### <a name="object-timeouts"></a>timeouts
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| create | string | no |  |  |
| update | string | no |  |  |
| delete | string | no |  |  |