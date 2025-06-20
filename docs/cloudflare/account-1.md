# /cloudflare/account-1.yml

**Schema location:** [/cloudflare/account-1.yml](/schemas/cloudflare/account-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /cloudflare/account-1.yml |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| providerVersion | string | yes |  |  |
| accountOwners | array of [accountOwners](#array-accountOwners) | yes |  |  |
| apiCredentials | vaultSecret | yes |  |  |
| enforceTwofactor | boolean | no |  |  |
| type | string | no | standard, enterprise |  |
| terraformStateAccount | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  | AWS Account to use for state in S3 |
| deletionApprovals | array | no |  |  |

### <a name="array-accountOwners"></a>accountOwner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |