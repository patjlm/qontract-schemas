# /app-sre/app-1.yml

**Schema location:** [/app-sre/app-1.yml](/schemas/app-sre/app-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/app-1.yml |  |
| labels | labels | yes |  |  |
| name | extendedIdentifier | yes |  |  |
| product | $ref: [product-1.yml](/docs/app-sre/product-1.md) | no |  |  |
| description | string | yes |  |  |
| onboardingStatus | string | yes | Proposed, InProgress, TransitionPeriod, OnBoarded, OffBoarding, BestEffort |  |
| grafanaUrls | array of [grafanaUrls](#array-grafanaUrls) | yes |  | List of links to Grafana Dashboard/Folders associated with the service. Please provide<br>a title together with the link. |
| sopsUrl | string | yes |  | Link to the git repo path that contains the top-level for the service<br>SOPs. |
| architectureDocument | string | yes |  | The Architecture Document should be written with SREs as the target audience. Anyone<br>reading the Architecture Document should understand how the service works, even<br>without any prior background. This document will be the primary reference during<br>incidents. To ensure the Architecture Document is always accessible to SREs and its<br>changes properly reviewed and tracked, it must be written in markdown and stored in<br>a place where SREs can control its changes. |
| parentApp | $ref: [app-1.yml](/docs/app-sre/app-1.md) | no |  |  |
| serviceOwners | array of [serviceOwners](#array-serviceOwners) | yes |  | Teams or individuals who is/are responsible for the running instance of the software. |
| serviceNotifications | array of [serviceNotifications](#array-serviceNotifications) | no |  | Teams or individuals who is/are should get notifications related to the service. |
| serviceDocs | array | no |  | List of service docs |
| dependencies | array of $ref to [dependency-1.yml](/docs/dependencies/dependency-1.md) | no |  |  |
| artifactRegistryMirrors | array of [artifactRegistryMirrors](#array-artifactRegistryMirrors) | no |  |  |
| gcrRepos | array of [gcrRepos](#array-gcrRepos) | no |  |  |
| quayRepos | array of [quayRepos](#array-quayRepos) | no |  |  |
| endPoints | array of [endPoints](#array-endPoints) | no |  |  |
| escalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | yes |  |  |
| codeComponents | array of [codeComponents](#array-codeComponents) | no |  |  |
| glitchtipProjects | array of $ref to [glitchtip-project-1.yml](/docs/dependencies/glitchtip-project-1.md) | no |  |  |

### <a name="array-grafanaUrls"></a>grafanaUrl
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| title | string | yes |  |  |
| url | string | yes |  |  |

### <a name="array-serviceOwners"></a>serviceOwner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |

### <a name="array-serviceNotifications"></a>serviceNotification
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |

### <a name="array-items"></a>item
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| imageURL | string | yes |  |  |
| mirror | $ref: [container-image-mirror-1.yml](/docs/dependencies/container-image-mirror-1.md) | yes |  |  |

### <a name="array-artifactRegistryMirrors"></a>artifactRegistryMirror
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| project | $ref: [project-1.yml](/docs/gcp/project-1.md) | yes |  |  |
| items | array of [items](#array-items) | yes |  |  |

### <a name="array-items"></a>item
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| description | string | yes |  |  |
| public | boolean | yes |  |  |
| mirror | $ref: [container-image-mirror-1.yml](/docs/dependencies/container-image-mirror-1.md) | no |  |  |

### <a name="array-gcrRepos"></a>gcrRepo
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| project | $ref: [project-1.yml](/docs/gcp/project-1.md) | yes |  |  |
| items | array of [items](#array-items) | yes |  |  |

### <a name="array-teams"></a>team
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| permissions | array of $ref to [permission-1.yml](/docs/access/permission-1.md) | yes |  |  |
| role | string | yes | read |  |

### <a name="object-verificationMethod"></a>verificationMethod
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| jiraBoard | $ref: [jira-board-1.yml](/docs/dependencies/jira-board-1.md) | no |  |  |

### <a name="array-notifications"></a>notification
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| event | string | yes | vulnerability_found |  |
| severity | string | no | Defcon 1, Critical, High, Medium, Low, Negligible, Unknown |  |
| method | string | yes | email |  |
| escalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | yes |  |  |
| verificationMethod | [verificationMethod](#object-verificationMethod) | no |  |  |

### <a name="array-items"></a>item
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| description | string | yes |  |  |
| public | boolean | yes |  |  |
| mirror | $ref: [container-image-mirror-1.yml](/docs/dependencies/container-image-mirror-1.md) | no |  |  |

### <a name="array-quayRepos"></a>quayRepo
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| org | $ref: [quay-org-1.yml](/docs/dependencies/quay-org-1.md) | yes |  |  |
| teams | array of [teams](#array-teams) | no |  |  |
| notifications | array of [notifications](#array-notifications) | no |  |  |
| items | array of [items](#array-items) | yes |  |  |

### <a name="array-monitoring"></a>monitoring
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | $ref: [endpoint-monitoring-provider-1.yml](/docs/dependencies/endpoint-monitoring-provider-1.md) | yes |  | Reference to a monitoring provider to use for this endpoint |

### <a name="array-endPoints"></a>endPoint
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| description | string | yes |  |  |
| url | string | yes |  |  |
| monitoring | array of [monitoring](#array-monitoring) | no |  |  |

### <a name="object-sourceProject"></a>sourceProject
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | no |  |  |
| group | string | no |  |  |
| branch | string | no |  |  |

### <a name="object-destinationProject"></a>destinationProject
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | no |  |  |
| group | string | no |  |  |
| branch | string | no |  |  |

### <a name="object-gitlabSync"></a>gitlabSync
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| sourceProject | [sourceProject](#object-sourceProject) | yes |  |  |
| destinationProject | [destinationProject](#object-destinationProject) | yes |  |  |

### <a name="object-gitlabRepoOwners"></a>gitlabRepoOwners
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | no |  |  |
| persistentLgtm | boolean | no |  |  |

### <a name="array-labels-allowed"></a>labels_allowed
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| role | $ref: [role-1.yml](/docs/access/role-1.md) | yes |  |  |

### <a name="object-gitlabHousekeeping"></a>gitlabHousekeeping
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | yes |  |  |
| rebase | boolean | yes |  |  |
| days_interval | integer | no |  |  |
| limit | integer | no |  |  |
| enable_closing | boolean | no |  |  |
| pipeline_timeout | integer | no |  |  |
| labels_allowed | array of [labels_allowed](#array-labels-allowed) | no |  |  |
| must_pass | array | no |  |  |

### <a name="array-codeComponents"></a>codeComponent
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| description | string | no |  |  |
| resource | string | yes | upstream, bundle, other, gitops, infrastructure |  |
| showInReviewQueue | boolean | no |  | Include MRs from this repo in the AppSRE Review Queue |
| url | string | yes |  |  |
| gitlabSync | [gitlabSync](#object-gitlabSync) | no |  |  |
| gitlabRepoOwners | [gitlabRepoOwners](#object-gitlabRepoOwners) | no |  |  |
| gitlabHousekeeping | [gitlabHousekeeping](#object-gitlabHousekeeping) | no |  |  |
| jira | $ref: [jira-server-1.yml](/docs/dependencies/jira-server-1.md) | no |  |  |
| mirror | string | no |  | GitLab repo to mirror from |
| imageBuildUrl | string | no |  | URL for the component's image build job (jenkins job, rhtap pipeline page, etc.) |
| managePermissions | boolean | no |  | should permissions be managed on the repository |
| blockedVersions | array | no |  |  |
| hotfixVersions | array | no |  |  |