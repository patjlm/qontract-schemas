# /kafka/cluster-1.yml

**Schema location:** [/kafka/cluster-1.yml](/schemas/kafka/cluster-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /kafka/cluster-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| ocm | $ref: [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | yes |  |  |
| spec | [spec](#object-spec) | yes |  |  |

### <a name="object-spec"></a>spec
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | yes | aws |  |
| region | string | yes |  |  |
| multi_az | boolean | yes |  |  |