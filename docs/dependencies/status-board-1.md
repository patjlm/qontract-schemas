# /dependencies/status-board-1.yml

**Schema location:** [/dependencies/status-board-1.yml](/schemas/dependencies/status-board-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/status-board-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| ocm | $ref: [openshift-cluster-manager-environment-1.yml](/docs/openshift/openshift-cluster-manager-environment-1.md) | yes |  |  |
| globalAppSelectors | [globalAppSelectors](#object-globalAppSelectors) | no |  |  |
| products | array of [products](#array-products) | yes |  |  |

### <a name="object-globalAppSelectors"></a>globalAppSelectors
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| exclude | array | no |  |  |

### <a name="object-appSelectors"></a>appSelectors
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| exclude | array | no |  |  |

### <a name="array-products"></a>product
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| productEnvironment | $ref: [environment-1.yml](/docs/app-sre/environment-1.md) | yes |  |  |
| appSelectors | [appSelectors](#object-appSelectors) | no |  |  |