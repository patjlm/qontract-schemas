# /openshift/openshift-resource-1.yml

**Schema location:** [/openshift/openshift-resource-1.yml](/schemas/openshift/openshift-resource-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/openshift-resource-1.yml |  |
| provider | string | yes |  |  |
| path | string | no |  |  |
| validate_json | boolean | no |  |  |
| validate_alertmanager_config | boolean | no |  |  |
| alertmanager_config_key | string | no |  |  |
| enable_query_support | boolean | no |  | indicates that this resource is using graphql query results |
| type | string | no |  |  |
| variables | object | no |  |  |
| name | string | no |  |  |
| version | integer | no |  |  |
| labels | labels | no |  |  |
| annotations | annotations | no |  |  |
| vault_tls_secret_path | string | no |  |  |
| vault_tls_secret_version | integer | no |  |  |
| tests | array | no |  |  |
| service_account_name | string | no |  |  |
| service_account_password | vaultSecret | no |  |  |
| secret_name | string | no |  |  |
| auto_renew_threshold_days | integer | no |  |  |