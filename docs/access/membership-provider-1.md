# /access/membership-provider-1.yml

**Schema location:** [/access/membership-provider-1.yml](/schemas/access/membership-provider-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /access/membership-provider-1.yml |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| hasAuditTrail | boolean | yes |  |  |
| source | [source](#object-source) | yes |  |  |

### <a name="object-source"></a>source
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | no | app-interface |  |
| url | string | no |  |  |
| username | vaultSecret | no |  |  |
| password | vaultSecret | no |  |  |