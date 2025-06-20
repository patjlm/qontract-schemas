# App Interface Resource Template Test

**Schema location:** [/app-interface/resource-template-test-1.yml](/schemas/app-interface/resource-template-test-1.yml)

**Description:** Schema for defining resource template tests in app-interface. 
This includes details about the resource template to be tested, 
the expected result, and other metadata.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/resource-template-test-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | A unique name for the resource template test. |
| description | string | yes |  | A description of the resource template test. |
| resourcePath | string | yes |  | The path to the resource template to be tested. |
| expectedResult | string | yes |  | The expected result of the templating process to compare against. |