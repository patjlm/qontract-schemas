# /aws/account-1.yml

**Schema location:** [/aws/account-1.yml](/schemas/aws/account-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/account-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| consoleUrl | string | yes |  |  |
| uid | string | yes |  |  |
| resourcesDefaultRegion | string | yes |  |  |
| supportedDeploymentRegions | array | no |  |  |
| providerVersion | string | yes |  |  |
| terraformUsername | string | no |  |  |
| accountOwners | array of [accountOwners](#array-accountOwners) | yes |  |  |
| securityContact | [securityContact](#object-securityContact) | no |  |  |
| automationToken | vaultSecret | yes |  |  |
| automationRole | [automationRole](#object-automationRole) | no |  | Role per integration or use-case to assume in the account |
| garbageCollection | boolean | no |  |  |
| enableDeletion | boolean | no |  |  |
| deletionApprovals | array | no |  |  |
| disable | [disable](#object-disable) | no |  |  |
| deleteKeys | array | no |  |  |
| resetPasswords | array of [resetPasswords](#array-resetPasswords) | no |  |  |
| premiumSupport | boolean | yes |  |  |
| partition | string | no | aws, aws-us-gov | the partition used in ARNs in the account (arn:aws:...) |
| sharing | array | no |  |  |
| cleanup | array | no |  |  |
| terraformState | $ref: [terraform-state-1.yml](/docs/dependencies/terraform-state-1.md) | no |  | key information for a terraform's state location and integration |
| rosa | $ref: [rosa-ocm-1.yml](/docs/dependencies/rosa-ocm-1.md) | no |  | Rosa related attributes in the aws account. |
| billingAccount | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  | AWS account to be used as the Billing account for ROSA HCP cluster provisioning |
| sso | boolean | no |  | Enable single sign on for the account. Default is enabled. |
| organization |  | no |  |  |
| alias | string | no |  | The alias for the account. This is the name that appears in the AWS SSO page. If not set, the account name will be used. |
| quotaLimits | array of $ref to [quota-limits-1.yml](/docs/aws/quota-limits-1.md) | no |  |  |
| organizationAccountTags | labels | no |  | For payer accounts only! Apply these tags to all accounts in the organization. This is useful for tagging all accounts in the organization with the same tags. |
| externalResources | [externalResources](#object-externalResources) | no |  | External resources settings for the account. |

### <a name="array-accountOwners"></a>accountOwner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |

### <a name="object-securityContact"></a>securityContact
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | The name of the security contact. |
| title | string | no |  | The title of the security contact. Default use the name. |
| email | string | yes |  |  |
| phoneNumber | phoneNumber | yes |  |  |

### <a name="object-automationRole"></a>automationRole
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| awsAccountManager | string | no |  | The AWS account manager IAM role name in the payer account |

### <a name="object-disable"></a>disable
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| integrations | array | no |  | integrations to disable for the aws account |

### <a name="array-resetPasswords"></a>resetPassword
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| user | $ref: [user-1.yml](/docs/access/user-1.md) | yes |  |  |
| requestId | string | yes |  |  |

### <a name="object-externalResources"></a>externalResources
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| channel | string | no |  | The channel to use for external resource modules. |