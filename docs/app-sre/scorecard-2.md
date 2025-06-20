# /app-sre/scorecard-2.yml

**Schema location:** [/app-sre/scorecard-2.yml](/schemas/app-sre/scorecard-2.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/scorecard-2.yml |  |
| labels | labels | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| date | string | yes |  | YYYY-mm-dd (year, month, day) |
| acceptanceCriteria | array of [acceptanceCriteria](#array-acceptanceCriteria) | yes |  | acceptance criteria items |

### <a name="array-acceptanceCriteria"></a>acceptanceCriteria
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes | CONTINUITY-0001, CONTINUITY-0002, CONTINUITY-0003, INCIDENT-MGMT-0001, INCIDENT-MGMT-0002, INCIDENT-MGMT-0003, INCIDENT-MGMT-0004, INCIDENT-MGMT-0005, INCIDENT-MGMT-0006, INCIDENT-MGMT-0007, INCIDENT-MGMT-0008, OBSERVABILITY-0001, OBSERVABILITY-0002, OBSERVABILITY-0003, OBSERVABILITY-0004, OBSERVABILITY-0005, OBSERVABILITY-0006, RELEASING-0001, RELEASING-0002, RELEASING-0003, RELEASING-0004, RELEASING-0005, RELIABILITY-0001, RELIABILITY-0002, RELIABILITY-0003, RELIABILITY-0004, RELIABILITY-0005, RELIABILITY-0006, RELIABILITY-0007, RELIABILITY-0008, RELIABILITY-0009, RELIABILITY-0010, RELIABILITY-0011, SECURITY-0001, SECURITY-0002, SECURITY-0003, SECURITY-0004 | name of acceptance criteria item |
| status | string | yes | green, yellow, red |  |
| comment | string | no |  |  |