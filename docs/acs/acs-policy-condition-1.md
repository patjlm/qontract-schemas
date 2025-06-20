# Policy Condition

**Schema location:** [/acs/acs-policy-condition-1.yml](/schemas/acs/acs-policy-condition-1.yml)

**Description:** Schema for defining conditions in Red Hat Advanced Cluster Security (ACS) policies. 
Conditions specify the criteria that must be met for a policy to trigger. 
This schema includes details about fields, comparisons, and thresholds 
used to evaluate policy violations.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /acs/acs-policy-condition-1.yml |  |
| policyField | string | yes |  | The field in the policy that is being evaluated. Examples include <br>`cvss`, `severity`, `cve`, `image_tag`, and `image_age`. |
| comparison | string | no | gt, gte, eq, lt, lte | The comparison operator used to evaluate the policy condition. <br>Supported operators include `gt` (greater than), `gte` (greater than or equal to), <br>`eq` (equal to), `lt` (less than), and `lte` (less than or equal to). |
| score | integer | no |  | The numerical score used for comparison when the `policyField` is `cvss`. |
| level | string | no | low, moderate, important, critical | The severity level used for comparison when the `policyField` is `severity`. <br>Supported levels include `low`, `moderate`, `important`, and `critical`. |
| fixable | boolean | no |  | Indicates whether the condition applies only to fixable issues. <br>This is used when the `policyField` is `cve`. |
| tags | array | no |  | A list of image tags used for evaluation when the `policyField` is `image_tag`. |
| negate | boolean | no |  | Indicates whether the condition should negate the specified tags. <br>This is used when the `policyField` is `image_tag`. |
| days | integer | no |  | The number of days used for evaluation when the `policyField` is `image_age`. |