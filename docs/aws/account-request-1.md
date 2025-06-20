# /aws/account-request-1.yml

**Schema location:** [/aws/account-request-1.yml](/schemas/aws/account-request-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/account-request-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | Unique name for aws account, it will be added to account as an alias.<br>It must be a minimum length of 3 characters and maximum length of 63 characters,<br>contain only digits, lowercase letters, and hyphens (-), but cannot begin or end with a hyphen. |
| description | string | yes |  |  |
| accountOwner | [accountOwner](#object-accountOwner) | yes |  | Account owner |
| organization |  | yes |  |  |
| quotaLimits | array of $ref to [quota-limits-1.yml](/docs/aws/quota-limits-1.md) | no |  |  |
| resourcesDefaultRegion | string | yes |  |  |
| supportedDeploymentRegions | array | no |  |  |
| uid | string | no |  | Specifying an account UID will takeover an existing account instead of creating a new one.<br>Please make sure you specify the current account owner and the current organization. |
| additionalFeatures | object | no |  | Enable/disable additional features for this account. See account template for all available feature options. |
| accountFileTargetPath | string | no |  | Specifying the target path for the new account file. Default: `/aws/<account_name>/account.yml` |

### <a name="object-accountOwner"></a>accountOwner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |