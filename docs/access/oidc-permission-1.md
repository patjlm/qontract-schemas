# /access/oidc-permission-1.yml

**Schema location:** [/access/oidc-permission-1.yml](/schemas/access/oidc-permission-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/oidc-permission-1.yml |  |
| labels | labels | no |  |  |
| name | string | yes |  |  |
| service | string | yes |  |  |
| description | string | yes |  |  |
| vault_policies | array of $ref to  | no |  |  |
| instance | $ref: [instance-1.yml](/docs/vault-config/instance-1.md) | no |  |  |
| clusters | array of $ref to [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  |  |
| namespaces | array of $ref to [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| permission_set |  | no | admin, analyst, vuln-admin, vuln-report-creator |  |