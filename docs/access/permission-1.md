# /access/permission-1.yml

**Schema location:** [/access/permission-1.yml](/schemas/access/permission-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/permission-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| service | string | yes |  |  |
| org | string | no |  |  |
| team | string | no |  |  |
| cluster | string | no |  |  |
| namespace | string | no |  |  |
| instance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | no |  |  |
| quayOrg | $ref: [quay-org-1.yml](/docs/dependencies/quay-org-1.md) | no |  |  |
| role | string | no |  |  |
| group | string | no |  |  |
| access | string | no | owner, maintainer, developer, reporter, guest |  |
| token | vaultSecret | no |  |  |
| workspace | $ref: [slack-workspace-1.yml](/docs/dependencies/slack-workspace-1.md) | no |  |  |
| handle | string | no |  |  |
| pagerduty | array of $ref to [pagerduty-target-1.yml](/docs/dependencies/pagerduty-target-1.md) | no |  |  |
| ownersFromRepos | array | no |  |  |
| channels | array | no |  |  |
| schedule | $ref: [schedule-1.yml](/docs/app-sre/schedule-1.md) | no |  |  |
| skip | boolean | no |  |  |
| actions | array of $ref to [automated-action-1.yml](/docs/app-sre/automated-action-1.md) | no |  |  |