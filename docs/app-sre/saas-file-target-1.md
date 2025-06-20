# /app-sre/saas-file-target-1.yml

**Schema location:** [/app-sre/saas-file-target-1.yml](/schemas/app-sre/saas-file-target-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/saas-file-target-1.yml |  |
| name | string | no |  |  |
| provider | string | no | static, dynamic |  |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| namespaceSelector |  | no |  |  |
| ref | string | yes |  |  |
| promotion | [promotion](#object-promotion) | no |  |  |
| parameters | object | no |  |  |
| secretParameters | array | no |  | target level parameters from vault secrets |
| upstream | [upstream](#object-upstream) | no |  |  |
| images | array of [images](#array-images) | no |  | wait for all images to exist before triggering a deployment |
| slos | array of $ref to [slo-document-1.yml](/docs/app-sre/slo-document-1.md) | no |  | list of file path of slo documents to be evaluated before promoting changes |
| disable | boolean | no |  |  |
| delete | boolean | no |  |  |

### <a name="array-data"></a>data
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | no |  |  |

### <a name="array-promotion-data"></a>promotion_data
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| channel | string | no |  |  |
| data | array of [data](#array-data) | no |  |  |

### <a name="object-promotion"></a>promotion
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| auto | boolean | no |  |  |
| redeployOnPublisherConfigChange | boolean | no |  | Whether to redeploy if a config change happened in a publisher. This will set<br>target_config_hash in promotion_data. This is mainly intended for test jobs. |
| publish | array | no |  |  |
| subscribe | array | no |  |  |
| soakDays | integer | no |  | number of days to wait for promotion |
| schedule | string | no |  | Same as AUS schedule - crontab expression to optionally restrict deployment windows |
| promotion_data | array of [promotion_data](#array-promotion-data) | no |  |  |

### <a name="object-upstream"></a>upstream
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| instance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | yes |  |  |
| name | string | yes |  |  |

### <a name="array-images"></a>image
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| org | $ref: [quay-org-1.yml](/docs/dependencies/quay-org-1.md) | yes |  |  |
| name | string | yes |  | image repository name |