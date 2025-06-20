# /app-sre/network-1.yml

**Schema location:** [/app-sre/network-1.yml](/schemas/app-sre/network-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/network-1.yml |  |
| labels | labels | no |  |  |
| name | extendedIdentifier | yes |  |  |
| description | string | yes |  |  |
| inUseBy | [inUseBy](#object-inUseBy) | no |  | A reference to some entity that is able to, and has claimed this network. If this network is unclaimed, this will have a null value. |
| networkAddress | string | yes |  | The network address in CIDR format |
| parentNetwork | $ref: [network-1.yml](/docs/app-sre/network-1.md) | no |  | A reference to this network's parent network. If this is a 'root' network, it will have no parent. |
| region | string | no |  | Region where this network resides |

### <a name="object-inUseBy"></a>inUseBy
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| vpc | $ref: [vpc-request-1.yml](/docs/aws/vpc-request-1.md) | no |  |  |