# /aws/terraform-resource-lifecycle-1.yml

**Schema location:** [/aws/terraform-resource-lifecycle-1.yml](/schemas/aws/terraform-resource-lifecycle-1.yml)

**Description:** meta-arguments available for all resource blocks regardless of type

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /aws/terraform-resource-lifecycle-1.yml |  |
| create_before_destroy | boolean | no |  | create replacement object before the prior object is destroyed |
| prevent_destroy | boolean | no |  | reject with an error any plan that would destroy the object |
| ignore_changes | array | no |  | attributes to ignore when planning updates to the object |