# /dynatrace/dynatrace-token-provider-token-spec-1.yml

**Schema location:** [/dynatrace/dynatrace-token-provider-token-spec-1.yml](/schemas/dynatrace/dynatrace-token-provider-token-spec-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dynatrace/dynatrace-token-provider-token-spec-1.yml |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| ocm_org_ids | array | yes |  |  |
| secrets | array of [secrets](#array-secrets) | yes |  |  |

### <a name="array-tokens"></a>token
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | Name used in the Dynatrace API as prefix for token.<br>Note, that due to Dynatrace API the token name length is limited. |
| keyNameInSecret | string | no |  | Key for this token inside the openshift secret object. If not set, uses "name" |
| scopes | array | yes |  |  |

### <a name="array-secrets"></a>secret
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| namespace | string | yes |  |  |
| tokens | array of [tokens](#array-tokens) | yes |  |  |