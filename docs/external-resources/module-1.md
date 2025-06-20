# /external-resources/module-1.yml

**Schema location:** [/external-resources/module-1.yml](/schemas/external-resources/module-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /external-resources/module-1.yml |  |
| labels | labels | no |  |  |
| provision_provider | string | yes |  |  |
| provider | string | yes |  |  |
| module_type | string | yes |  |  |
| reconcile_drift_interval_minutes | integer | yes |  |  |
| reconcile_timeout_minutes | integer | yes |  |  |
| outputs_secret_sync | boolean | yes |  |  |
| outputs_secret_image | string | no |  | Docker image to use for the outputs secret container |
| outputs_secret_version | string | no |  | Version of the outputs secret container to use |
| resources |  | no |  |  |
| default_channel | string | yes |  |  |
| channels | array of [channels](#array-channels) | yes |  |  |

### <a name="array-channels"></a>channel
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| image | string | yes |  |  |
| version | string | yes |  |  |