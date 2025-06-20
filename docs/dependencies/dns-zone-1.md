# /dependencies/dns-zone-1.yml

**Schema location:** [/dependencies/dns-zone-1.yml](/schemas/dependencies/dns-zone-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/dns-zone-1.yml |  |
| labels | labels | no |  |  |
| name | string | yes |  |  |
| domain_name | string | no |  |  |
| description | string | no |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  |  |
| vpc | $ref: [vpc-1.yml](/docs/aws/vpc-1.md) | no |  |  |
| allowed_vault_secret_paths | array | no |  | List of paths used to limit the secrets that can be accessed for creating DNS records, the primary use case being domain control validation (DCV) |
| records | array | yes |  |  |