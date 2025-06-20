# /vault-config/replication-paths-1.yml

**Schema location:** [/vault-config/replication-paths-1.yml](/schemas/vault-config/replication-paths-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /vault-config/replication-paths-1.yml |  |
| provider | string | yes |  |  |
| jenkinsInstance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | no |  |  |
| policy | $ref: [policy-1.yml](/docs/vault-config/policy-1.md) | no |  |  |