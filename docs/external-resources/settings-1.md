# /external-resources/settings-1.yml

**Schema location:** [/external-resources/settings-1.yml](/schemas/external-resources/settings-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /external-resources/settings-1.yml |  |
| labels | labels | no |  |  |
| tf_state_bucket | string | no |  |  |
| tf_state_dynamodb_table | string | no |  |  |
| tf_state_region | string | no |  |  |
| state_dynamodb_account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| state_dynamodb_region | string | yes |  |  |
| state_dynamodb_table | string | yes |  |  |
| workers_cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | yes |  |  |
| workers_namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| vault_secrets_path | string | yes |  |  |
| outputs_secret_image | string | yes |  | Docker image to use for the outputs secret container |
| outputs_secret_version | string | yes |  | Version of the outputs secret container to use |
| module_default_resources |  | yes |  |  |