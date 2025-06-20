# /openshift/cluster-addon-1.yml

**Schema location:** [/openshift/cluster-addon-1.yml](/schemas/openshift/cluster-addon-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/cluster-addon-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| parameters | array of [parameters](#array-parameters) | no |  |  |

### <a name="array-parameters"></a>parameter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| id | string | yes |  |  |
| value | string | yes |  |  |