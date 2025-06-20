# /aws/sharing-option-1.yml

**Schema location:** [/aws/sharing-option-1.yml](/schemas/aws/sharing-option-1.yml)

**Description:** define sharing options between aws accounts

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /aws/sharing-options-1.yml |  |
| provider | string | yes | ami | type of sharing to implement |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| regex | string | no |  | regex expression to filter items by |
| region |  | no |  |  |