# /app-sre/integration-sharding-1.yml

**Schema location:** [/app-sre/integration-sharding-1.yml](/schemas/app-sre/integration-sharding-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/integration-sharding-1.yml |  |
| strategy | string | yes | per-aws-account, per-cloudflare-dns-zone, per-openshift-cluster, per-ocm-organization, static |  |
| shards | integer | no |  |  |
| shardSpecOverrides | array of [shardSpecOverrides](#array-shardSpecOverrides) | no |  |  |

### <a name="object-subSharding"></a>subSharding
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| strategy | string | no | static |  |
| shards | integer | no |  |  |

### <a name="array-shardSpecOverrides"></a>shardSpecOverride
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| shard |  | no | [cluster-1.yml](/docs/openshift/cluster-1.md), [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md), [account-1.yml](/docs/aws/account-1.md), [dns-zone-1.yml](/docs/cloudflare/dns-zone-1.md) |  |
| imageRef | string | no |  | Image ref used by the shard. |
| resources |  | no |  |  |
| disabled | boolean | no |  |  |
| subSharding | [subSharding](#object-subSharding) | no |  | Sub-sharding strategy used by a shard. |