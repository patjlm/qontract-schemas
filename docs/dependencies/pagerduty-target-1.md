# /dependencies/pagerduty-target-1.yml

**Schema location:** [/dependencies/pagerduty-target-1.yml](/schemas/dependencies/pagerduty-target-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/pagerduty-target-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| instance | $ref: [pagerduty-instance-1.yml](/docs/dependencies/pagerduty-instance-1.md) | yes |  |  |
| scheduleID | string | no |  |  |
| escalationPolicyID | string | no |  |  |