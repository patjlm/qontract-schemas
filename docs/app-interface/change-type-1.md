# App Interface Change Type

**Schema location:** [/app-interface/change-type-1.yml](/schemas/app-interface/change-type-1.yml)

**Description:** Schema for defining change types in app-interface. 
Change types influence how merge requests are processed and provide 
context for changes, including priority, restrictions, and inheritance.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/change-type-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the change type. |
| description | string | yes |  | A brief description of the change type. |
| priority | string | yes | critical, urgent, high, progressive-delivery, medium, low | The priority of the change type, which influences the order <br>in which merge requests are processed. |
| contextType | string | yes |  | The type of context associated with the change type. |
| contextSchema | string | no |  | The schema defining the context for the change type. |
| disabled | boolean | no |  | Indicates whether the change type is disabled. <br>A disabled change type does not have any effect but will still <br>log into the pull request check logs. |
| restrictive | boolean | no |  | Indicates whether the change type is restrictive. <br>Entities protected with a restrictive change type can only be <br>changed by the team assigned to the change type. |
| inherit | array of $ref to [change-type-1.yml](/docs/app-interface/change-type-1.md) | no |  | A list of additional change types whose changes are inherited <br>by this change type. |
| changes | array of [changes](#array-changes) | no |  | A list of changes associated with the change type. Each change <br>specifies a provider, schema, and additional context. |
| implicitOwnership | array | no |  | A list of implicit ownership rules for the change type. <br>These rules define ownership based on JSONPath selectors. |

### <a name="object-context"></a>context
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| selector | string | no |  | The selector used to identify the context for the change. |
| where | string | no | backrefs | Specifies where the context applies. Supported values <br>include `backrefs`. |
| when | string | no | added, removed | Specifies when the context applies. Supported values <br>include `added` and `removed`. |

### <a name="array-changes"></a>change
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | no | jsonPath, change-type | The provider for the change. Supported providers include <br>`jsonPath` and `change-type`. |
| changeSchema | string | no |  | The schema defining the structure of the change. |
| jsonPathSelectors | array | no |  | A list of JSONPath selectors used to identify the changes. |
| changeTypes | array of $ref to [change-type-1.yml](/docs/app-interface/change-type-1.md) | no |  | A list of additional change types associated with this change. |
| context | [context](#object-context) | no |  | Context for the change, including selectors and conditions. |