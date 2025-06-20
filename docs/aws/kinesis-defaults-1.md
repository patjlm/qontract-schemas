# /aws/kinesis-defaults-1.yml

**Schema location:** [/aws/kinesis-defaults-1.yml](/schemas/aws/kinesis-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/kinesis-defaults-1.yml |  |
| name | string | yes |  |  |
| shard_count | integer | yes |  |  |
| retention_period | integer | no |  |  |
| encryption_type | string | no | NONE, KMS |  |
| kms_key_id | string | no |  |  |
| release_url | string | no |  |  |
| runtime | string | no |  |  |
| timeout | integer | no |  |  |
| handler | string | no |  |  |
| memory_size | integer | no |  |  |
| index_prefix | string | no |  |  |
| parallelization_factor | integer | no |  |  |
| batch_size | integer | no |  |  |
| starting_position | string | no | LATEST, TRIM_HORIZON, AT_TIMESTAMP |  |
| starting_position_timestamp | string | no |  |  |