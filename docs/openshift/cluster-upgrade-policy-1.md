# /openshift/cluster-upgrade-policy-1.yml

**Schema location:** [/openshift/cluster-upgrade-policy-1.yml](/schemas/openshift/cluster-upgrade-policy-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/cluster-upgrade-policy-1.yml |  |
| schedule_type | string | no | automatic |  |
| schedule | string | yes |  |  |
| workloads | array | yes |  |  |
| versionGateApprovals | array | no |  |  |
| conditions |  | yes |  |  |