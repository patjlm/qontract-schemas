# /dependencies/quay-org-1.yml

**Schema location:** [/dependencies/quay-org-1.yml](/schemas/dependencies/quay-org-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/quay-org-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| instance | $ref: [quay-instance-1.yml](/docs/dependencies/quay-instance-1.md) | no |  |  |
| mirror | $ref: [quay-org-1.yml](/docs/dependencies/quay-org-1.md) | no |  |  |
| mirrorFilters | array of [mirrorFilters](#array-mirrorFilters) | no |  |  |
| managedTeams | array | yes |  |  |
| description | string | yes |  |  |
| managedRepos | boolean | yes |  |  |
| serverUrl | string | no |  |  |
| automationToken | vaultSecret | no |  |  |
| pushCredentials | vaultSecret | no |  |  |

### <a name="array-mirrorFilters"></a>mirrorFilter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | Name of the repository to filter. |
| tags | array | no |  | This limits which tags to mirror to the ones in the list.<br>They will take preference over the ones excluded.<br>Regular expressions are supported. |
| tagsExclude | array | no |  | Tags to exclude. Regular expression are supported. |