# /dependencies/rosa-ocm-1.yml

**Schema location:** [/dependencies/rosa-ocm-1.yml](/schemas/dependencies/rosa-ocm-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /dependencies/rosa-ocm-1.yml |  |
| ocm_environments | array of [ocm_environments](#array-ocm-environments) | no |  |  |

### <a name="array-ocm-environments"></a>ocm_environment
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| ocm | $ref: [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | no |  |  |
| creator_role_arn | string | no |  |  |
| installer_role_arn | string | no |  |  |
| support_role_arn | string | no |  |  |
| controlplane_role_arn | string | no |  |  |
| worker_role_arn | string | no |  |  |