# /cloudflare/dns-zone-1.yml

**Schema location:** [/cloudflare/dns-zone-1.yml](/schemas/cloudflare/dns-zone-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /cloudflare/dns-zone-1.yml |  |
| labels | labels | no |  |  |
| identifier | longIdentifier | no |  |  |
| zone | string | yes |  |  |
| plan | string | no | free, enterprise |  |
| type |  | no | full, partial |  |
| account | $ref: [account-1.yml](/docs/cloudflare/account-1.md) | no |  |  |
| records | array | no |  |  |
| max_records | integer | no |  |  |
| delete | boolean | no |  |  |