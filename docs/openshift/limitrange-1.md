# /openshift/limitrange-1.yml

**Schema location:** [/openshift/limitrange-1.yml](/schemas/openshift/limitrange-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/limitrange-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| limits | array of [limits](#array-limits) | yes |  |  |

### <a name="object-default"></a>default
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cpu | string | no |  |  |
| memory | string | no |  |  |

### <a name="object-defaultRequest"></a>defaultRequest
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cpu | string | no |  |  |
| memory | string | no |  |  |

### <a name="object-max"></a>max
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cpu | string | no |  |  |
| memory | string | no |  |  |

### <a name="object-maxLimitRequestRatio"></a>maxLimitRequestRatio
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cpu | string | no |  |  |
| memory | string | no |  |  |

### <a name="object-min"></a>min
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cpu | string | no |  |  |
| memory | string | no |  |  |

### <a name="array-limits"></a>limit
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | no | Container, Pod |  |
| default | [default](#object-default) | no |  |  |
| defaultRequest | [defaultRequest](#object-defaultRequest) | no |  |  |
| max | [max](#object-max) | no |  |  |
| maxLimitRequestRatio | [maxLimitRequestRatio](#object-maxLimitRequestRatio) | no |  |  |
| min | [min](#object-min) | no |  |  |