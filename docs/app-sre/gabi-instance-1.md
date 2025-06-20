# /app-sre/gabi-instance-1.yml

**Schema location:** [/app-sre/gabi-instance-1.yml](/schemas/app-sre/gabi-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/gabi-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | extendedIdentifier | yes |  |  |
| description | string | yes |  |  |
| readReplicasWaiverPledge | string | no |  |  |
| signoffManagers | array of $ref to [user-1.yml](/docs/access/user-1.md) | yes |  |  |
| users | array of $ref to [user-1.yml](/docs/access/user-1.md) | yes |  |  |
| instances | array of [instances](#array-instances) | yes |  |  |
| expirationDate | string | yes |  |  |

### <a name="array-instances"></a>instance
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| account |  | yes |  |  |
| identifier | longIdentifier | yes |  |  |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |