# /app-sre/saas-file-2.yml

**Schema location:** [/app-sre/saas-file-2.yml](/schemas/app-sre/saas-file-2.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/saas-file-2.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| displayName | string | yes |  |  |
| description | string | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| pipelinesProvider | $ref: [pipelines-provider-1.yml](/docs/app-sre/pipelines-provider-1.md) | yes |  |  |
| skipSuccessfulDeployNotifications | boolean | no |  |  |
| slack | [slack](#object-slack) | no |  |  |
| managedResourceTypes | array | yes |  |  |
| managedResourceNames | array | no |  |  |
| authentication |  | no |  |  |
| parameters | object | no |  |  |
| allowedSecretParameterPaths | array | no |  |  |
| secretParameters | array | no |  | saas file level parameters from vault secrets |
| validateTargetsInApp | boolean | no |  | indicates a desire to validate that all targets belong to the same app as the saas file itself |
| validatePlannedData | boolean | no |  | enable skipping planned data validation, mostly for automated bootstrap pusrposes |
| resourceTemplates | array of [resourceTemplates](#array-resourceTemplates) | yes |  |  |
| takeover | boolean | no |  |  |
| deprecated | boolean | no |  | prevent updates to a saas file |
| compare | boolean | no |  |  |
| timeout | dhmsDuration | no |  | Maximum time the deployment job is allowed to last. In Tekton it defaults to<br>60 minutes. We don't allow smaller times as Tekton implementation currently deletes<br>PipelineRun pods, hence destroying logs. |
| publishJobLogs | boolean | no |  |  |
| clusterAdmin | boolean | no |  |  |
| imagePatterns | array | yes |  |  |
| use_channel_in_image_tag | boolean | no |  |  |
| deployResources |  | no |  | CPU and memory resources used by the openshift-saas-deploy step of the openshift-saas-deploy tasks created by the openshit-tekton-resources integration |

### <a name="object-notifications"></a>notifications
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| start | boolean | no |  |  |

### <a name="object-slack"></a>slack
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| output | string | no | events, publish |  |
| workspace | $ref: [slack-workspace-1.yml](/docs/dependencies/slack-workspace-1.md) | yes |  |  |
| channel | string | yes |  |  |
| notifications | [notifications](#object-notifications) | no |  |  |

### <a name="array-resourceTemplates"></a>resourceTemplate
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| url | string | yes |  |  |
| path | string | yes |  |  |
| provider | string | no | openshift-template, directory, helm |  |
| hash_length | integer | no |  |  |
| parameters | object | no |  |  |
| secretParameters | array | no |  | resource template level parameters from vault secrets |
| targets | array | yes |  |  |