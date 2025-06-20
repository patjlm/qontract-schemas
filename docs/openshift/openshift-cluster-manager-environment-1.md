# /openshift/openshift-cluster-manager-environment-1.yml

**Schema location:** [/openshift/openshift-cluster-manager-environment-1.yml](/schemas/openshift/openshift-cluster-manager-environment-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/openshift-cluster-manager-environment-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| url | string | yes |  |  |
| accessTokenClientId | string | yes |  |  |
| accessTokenUrl | string | yes |  |  |
| accessTokenClientSecret | vaultSecret | yes |  |  |
| telemeter | $ref: [prometheus-instance-1.yml](/docs/dependencies/prometheus-instance-1.md) | no |  |  |