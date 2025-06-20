# /app-sre/sre-checkpoint-1.yml

**Schema location:** [/app-sre/sre-checkpoint-1.yml](/schemas/app-sre/sre-checkpoint-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/sre-checkpoint-1.yml |  |
| labels | labels | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  |  |
| sre | $ref: [user-1.yml](/docs/access/user-1.md) | yes |  |  |
| date | string | yes |  | YYYY-mm-dd (year, month, day) |
| issue | string | yes |  |  |
| contractVersion | $ref: [contract-version-1.yml](/docs/app-sre/contract-version-1.md) | yes |  | Contract version |