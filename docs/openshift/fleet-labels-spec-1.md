# /openshift/fleet-labels-spec-1.yml

**Schema location:** [/openshift/fleet-labels-spec-1.yml](/schemas/openshift/fleet-labels-spec-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/fleet-labels-spec-1.yml |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| managedSubscriptionLabelPrefix | string | yes |  |  |
| ocmEnv | $ref: [openshift-cluster-manager-environment-1.yml](/docs/openshift/openshift-cluster-manager-environment-1.md) | yes |  |  |
| dryRunLabelSynchronization | boolean | no |  | Disable the synchronization of labels from the subscription to the cluster.<br>This is useful if you want to let fleet labeler render the inventory first and<br>investigate/change any desired labels manually before the synchronization starts. |
| labelDefaults | array of [labelDefaults](#array-labelDefaults) | yes |  | List of default labels to apply to clusters by external configuration labels |
| clusters | array of [clusters](#array-clusters) | yes |  | List of clusters to define dynatrace token provider labels for |

### <a name="object-subscriptionLabelTemplate"></a>subscriptionLabelTemplate
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | resourceref | yes |  |  |
| type | string | no | jinja2, extracurlyjinja2 |  |
| variables | object | no |  |  |

### <a name="array-labelDefaults"></a>labelDefault
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| matchSubscriptionLabels | object | yes |  |  |
| subscriptionLabelTemplate | [subscriptionLabelTemplate](#object-subscriptionLabelTemplate) | yes |  |  |

### <a name="array-clusters"></a>cluster
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | cluster name |
| serverUrl | string | yes |  | cluster server url |
| clusterId | string | yes |  | cluster ID |
| subscriptionId | string | yes |  | subscription ID |
| subscriptionLabels | object | yes |  |  |