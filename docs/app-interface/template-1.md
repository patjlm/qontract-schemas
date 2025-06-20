# App Interface Template

**Schema location:** [/app-interface/template-1.yml](/schemas/app-interface/template-1.yml)

**Description:** Schema for defining templates in app-interface. 
This includes details about the template, its target path, 
conditions, tests, and rendering options.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/template-1.yml |  |
| name | string | yes |  | A unique name for the template. |
| autoApproved | boolean | no |  | Indicates whether the template is automatically approved. |
| targetPath | string | yes |  | The target path where the template will be applied. |
| condition | string | no |  | A condition that must be met for the template to be applied. |
| patch | [patch](#object-patch) | no |  | A patch to be applied to the template. |
| template | string | yes |  | The content of the template to be rendered. |
| templateTest | array of $ref to [template-test-1.yml](/docs/app-interface/template-test-1.md) | yes |  | A list of tests to validate the template. |
| templateRenderOptions | [templateRenderOptions](#object-templateRenderOptions) | no |  | Options for rendering the template. |

### <a name="object-patch"></a>patch
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | string | yes |  | JSON path to the target field in the template to patch. |
| identifier | string | no |  | Unique identifier field to use with path results.<br>Can be a string (field name) or a JSON path.<br>Examples: <br>  path_results = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]<br>  identifier = 'id'<br>  path_results = ['a', 'b']<br>  identifier = '$.id' |

### <a name="object-templateRenderOptions"></a>templateRenderOptions
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| trimBlocks | boolean | no |  | Indicates whether to trim blocks during rendering. |
| lstripBlocks | boolean | no |  | Indicates whether to strip leading whitespace from blocks. |
| keepTrailingNewline | boolean | no |  | Indicates whether to keep trailing newlines in the rendered template. |