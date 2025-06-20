# App Interface Template Collection

**Schema location:** [/app-interface/template-collection-1.yml](/schemas/app-interface/template-collection-1.yml)

**Description:** Schema for defining a collection of templates in app-interface. 
This includes details about the templates, variables, and 
configurations for generating multiple templates.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/template-collection-1.yml |  |
| name | string | yes |  | A unique name for the template collection. |
| additionalMrLabels | array | no |  | Additional merge request labels to be applied to the templates. |
| description | string | yes |  | A description of the template collection. |
| enableAutoApproval | boolean | no |  | Indicates whether auto-approval is enabled for the template collection. |
| forEach | [forEach](#object-forEach) | no |  | Configuration for iterating over a list of items to generate templates. |
| variables | [variables](#object-variables) | no |  | Variables to be used in the templates. |
| templates | array of $ref to [template-1.yml](/docs/app-interface/template-1.md) | yes |  | A list of templates to be included in the collection. |

### <a name="object-forEach"></a>forEach
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| items | array | no |  | A list of objects on which to run this template collection. |

### <a name="array-dynamic"></a>dynamic
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | The name of the dynamic variable. |
| query | string | yes |  | The GraphQL query used to fetch the dynamic variable. |

### <a name="object-variables"></a>variables
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| static | object | no |  | Static variables to be used in the templates. |
| dynamic | array of [dynamic](#array-dynamic) | no |  | Dynamic variables fetched from GraphQL queries. |