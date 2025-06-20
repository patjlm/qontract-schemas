# /dependencies/feature-toggle-1.yml

**Schema location:** [/dependencies/feature-toggle-1.yml](/schemas/dependencies/feature-toggle-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/feature-toggle-1.yml |  |
| labels | labels | no |  |  |
| name | string | yes |  | The name of the feature toggle |
| description | string | yes |  | A description of the feature toggle |
| delete | boolean | no |  | Whether to delete the feature toggle |
| provider | string | yes |  |  |
| unleash | [unleash](#object-unleash) | no |  | Configuration for an Unleash feature toggle |

### <a name="object-unleash"></a>unleash
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | no | experiment, kill_switch, release, operational, permission | The type of the feature toggle. Default is "release" |
| impressionData | boolean | no |  | Whether to collect impression data |
| projects | array of $ref to [unleash-project-1.yml](/docs/dependencies/unleash-project-1.md) | no |  | The projects that the feature toggle is associated with |
| environments | unleash-environments | no |  |  |