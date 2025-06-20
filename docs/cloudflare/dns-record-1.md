# /cloudflare/dns-record-1.yml

**Schema location:** [/cloudflare/dns-record-1.yml](/schemas/cloudflare/dns-record-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /cloudflare/dns-record-1.yml |  |
| identifier | longIdentifier | no |  |  |
| name | string | yes |  |  |
| type | string | yes | A, AAAA, CAA, CNAME, TXT, NS, MX, DS, DNSKEY |  |
| ttl | integer | yes |  |  |
| value | string | no |  |  |
| data | [data](#object-data) | no |  |  |
| proxied | boolean | no |  |  |
| priority | DNSRecordPriority | no |  |  |

### <a name="object-data"></a>data
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| algorithm | dsDNSRecordAlgro | no |  |  |
| key_tag | dsDNSRecordKeyTag | no |  |  |
| flags | dsDNSRecordKeyTag | no |  |  |
| protocol | integer | no |  |  |
| public_key | string | no |  |  |
| digest_type | integer | no |  |  |
| digest | string | no |  |  |
| tag | string | no |  |  |
| value | string | no |  |  |