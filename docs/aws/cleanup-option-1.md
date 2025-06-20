# /aws/cleanup-option-1.yml

**Schema location:** [/aws/cleanup-option-1.yml](/schemas/aws/cleanup-option-1.yml)

**Description:** Define cleanup options of AWS objects.

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /aws/cleanup-options-1.yml |  |
| provider | string | yes | ami, cloudwatch | Type of cleanup to implement. |
| regex | string | no |  | Regex expression to filter items by. |
| age | dhmsDuration | no |  | AMI age from which we can consider deletion. |
| retention_in_days | integer | no |  | Cloudwatch log retention |
| region | string | no |  | AWS region. |
| delete_empty_log_group | boolean | no |  | Enable deletion when log group is empty. |