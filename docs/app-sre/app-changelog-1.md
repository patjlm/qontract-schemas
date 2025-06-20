# Application Changelog

**Schema location:** [/app-sre/app-changelog-1.yml](/schemas/app-sre/app-changelog-1.yml)

**Description:** Schema for defining changelogs for applications defined in app-interface. 
This includes details about the application, the dates of changes, 
and descriptions of the changes made.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/app-changelog-1.yml |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | yes |  | Reference to the application associated with the changelog. |
| changelog | array of [changelog](#array-changelog) | yes |  | A list of changelog entries for the application. Each entry includes <br>the date of the change and a list of changes made. |

### <a name="array-changes"></a>change
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| tags | array | no |  | A list of tags categorizing the change (e.g., `bugfix`, <br>`feature`, `improvement`). |
| description | string | yes |  | A detailed description of the change made. |

### <a name="array-changelog"></a>changelog
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| date | date | yes |  | The date when the changes were made, in ISO 8601 format. |
| changes | array of [changes](#array-changes) | yes |  | A list of changes made on the specified date. Each change includes <br>tags and a description. |