# App Interface Template Test

**Schema location:** [/app-interface/template-test-1.yml](/schemas/app-interface/template-test-1.yml)

**Description:** Schema for defining tests for templates in app-interface. 
This includes details about the variables, expected outputs, 
and conditions for validating template rendering.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/template-test-1.yml |  |
| name | string | yes |  | A unique name for the template test. |
| variables | object | no |  | Variables to be used in the template test. |
| current | string | no |  | The current content of the file to be templated. |
| expectedTargetPath | string | no |  | The expected result of the target path after rendering the template. |
| expectedOutput | string | yes |  | The expected output of the template after rendering. |
| expectedToRender | boolean | no |  | Expected evaluation result of `$.condition` in `/app-interface/template-1.yml`. |