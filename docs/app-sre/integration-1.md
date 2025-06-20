# /app-sre/integration-1.yml

**Schema location:** [/app-sre/integration-1.yml](/schemas/app-sre/integration-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/integration-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| upstream | string | no |  |  |
| schemas | array | yes |  |  |
| pr_check | [pr_check](#object-pr-check) | no |  |  |
| managed | array of [managed](#array-managed) | no |  |  |

### <a name="object-pr-check"></a>pr_check
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cmd | string | yes |  |  |
| state | boolean | no |  |  |
| sqs | boolean | no |  |  |
| disabled | boolean | no |  |  |
| always_run | boolean | no |  |  |
| no_validate_schemas | boolean | no |  |  |
| run_for_valid_saas_file_changes | boolean | no |  |  |
| early_exit | boolean | no |  |  |
| check_only_affected_shards | boolean | no |  | defaults to false |
| run_order | integer | no |  |  |
| imageRef | string | no |  | image ref to be used |

### <a name="array-managed"></a>managed
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace |  | yes | [namespace-1.yml](/docs/openshift/namespace-1.md), [lean-namespace-1.yml](/docs/openshift/lean-namespace-1.md) |  |
| spec |  | yes |  |  |
| sharding |  | no |  |  |