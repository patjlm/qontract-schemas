# App Interface Settings

**Schema location:** [/app-interface/app-interface-settings-1.yml](/schemas/app-interface/app-interface-settings-1.yml)

**Description:** Specifications for configuring an app-interface instance. 
Configuration includes repository configuration, credentials, integrations, and other operational parameters.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/app-interface-settings-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the app-interface settings object. |
| description | string | yes |  | A brief description of the app-interface settings object. |
| repoUrl | string | yes |  | URL of the app-interface Git repository. |
| vault | boolean | yes |  | If true, a Vault instance provides secrets for automation.<br>If false, a config file provides secrets for automation. |
| kubeBinary | string | yes | kubectl, oc | The Kubernetes CLI binary to use (e.g., kubectl or oc). |
| mergeRequestGateway | string | no | gitlab, sqs | Determines the interface and destination for merge requests created with automation. |
| saasDeployJobTemplate | string | yes | openshift-saas-deploy, saas-deploy | Used with visual-qontract to generate pipeline names. |
| hashLength | integer | yes | 7 | The length of the hash used in openshift-saas-deploy pipeline |
| smtp | [smtp](#object-smtp) | no |  | SMTP configuration for sending emails. |
| imap | [imap](#object-imap) | no |  | IMAP configuration for receiving emails. |
| githubRepoInvites | [githubRepoInvites](#object-githubRepoInvites) | no |  | Configuration for the github-repo-invites integration. |
| ldap | [ldap](#object-ldap) | no |  | LDAP configuration for authentication and directory services. |
| dependencies | array of [dependencies](#array-dependencies) | no |  | List of dependencies required by the app-interface instance. |
| credentials | array of [credentials](#array-credentials) | no |  | List of GraphQL client credential instantiations. |
| sqlQuery | [sqlQuery](#object-sqlQuery) | no |  | Configuration for SQL queries. |
| pushGatewayCluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  | Reference to the cluster used for the push gateway. |
| alertingServices | array | no |  | List of services authorized to send alerts. |
| endpointMonitoringBlackboxExporterModules | array | no |  | List of supported blackbox exporter modules for endpoint monitoring. |
| jiraWatcher | [jiraWatcher](#object-jiraWatcher) | no |  | Configuration for the Jira watcher integration. |
| cloudflareEmailDomainAllowList | array | no |  | List of email domains allowed for Cloudflare access. |
| cloudflareDNSZoneMaxRecords | integer | no |  | Maximum number of DNS records allowed per zone in Cloudflare. |
| state | object | no |  | Configuration for app-interface state settings. |
| ldapGroups | [ldapGroups](#object-ldapGroups) | no |  | Configuration for LDAP groups. |
| deadMansSnitchSettings | [deadMansSnitchSettings](#object-deadMansSnitchSettings) | no |  | Configuration for Dead Man's Snitch integration. |
| costReport | [costReport](#object-costReport) | no |  | Configuration for cost reporting. |
| jiralert | [jiralert](#object-jiralert) | no |  | Configuration for Jira alerting. |
| rhcsProvider | [rhcsProvider](#object-rhcsProvider) | no |  | Configuration for RHCSv2 certificate generation and storing |
| customMessages | array of [customMessages](#array-customMessages) | no |  | Custom messages used in integrations. |
| terraformResourcesProviderExclusions | array of [terraformResourcesProviderExclusions](#array-terraformResourcesProviderExclusions) | no |  | Exclusions for Terraform resources by provider. |
| terraformResourcesProviderExclusionsByProvisioner | array of [terraformResourcesProviderExclusionsByProvisioner](#array-terraformResourcesProviderExclusionsByProvisioner) | no |  | Deprecated object for Terraform resource exclusions by provisioner. |

### <a name="object-smtp"></a>smtp
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| mailAddress | string | yes |  | The email address used for sending emails. |
| timeout | integer | no |  | Timeout value for SMTP connections. |
| credentials | vaultSecret | yes |  | Vault secret containing SMTP credentials. |

### <a name="object-imap"></a>imap
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| timeout | integer | no |  | Timeout value for IMAP connections. |
| credentials | vaultSecret | yes |  | Vault secret containing IMAP credentials. |

### <a name="object-githubRepoInvites"></a>githubRepoInvites
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| credentials | vaultSecret | yes |  | Vault secret containing credentials for the machine user (app-sre-bot) that interacts with the GitHub API. |

### <a name="object-ldap"></a>ldap
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| serverUrl | string | no |  | URL of the LDAP server. |
| baseDn | string | no |  | Base DN for LDAP queries. |

### <a name="array-dependencies"></a>dependency
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | yes | openshift, aws, github, gitlab, quay, ci-int, ci-ext, kafka | The type of dependency (e.g., OpenShift, AWS, GitHub). |
| services | array of $ref to [dependency-1.yml](/docs/dependencies/dependency-1.md) | yes |  | List of service references associated with the dependency. |

### <a name="array-credentials"></a>credential
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | The name of the credential. |
| secret | vaultSecret | yes |  | Vault secret containing the credential. |

### <a name="object-sqlQuery"></a>sqlQuery
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| imageRepository | string | yes |  | The repository for the SQL query image. |
| pullSecret |  | yes |  | Vault secret for pulling the SQL query image. |

### <a name="object-jiraWatcher"></a>jiraWatcher
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| readTimeout | integer | yes |  | Read timeout for Jira watcher. |
| connectTimeout | integer | yes |  | Connection timeout for Jira watcher. |

### <a name="object-ldapGroups"></a>ldapGroups
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| contactList | string | yes |  | Contact list for LDAP groups. |
| credentials | vaultSecret | yes |  | Vault secret containing credentials for LDAP groups. |

### <a name="object-deadMansSnitchSettings"></a>deadMansSnitchSettings
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| alertMailAddresses | array | no |  | Email addresses used for Dead Man's Snitch alerts. |
| notesLink | string | no |  | Link to the SOP for handling Dead Man's Snitch alerts. |
| snitchesPath | string | no |  | Vault location for snitch URL secrets. |
| tokenCreds | vaultSecret | no |  | Vault secret containing credentials for Dead Man's Snitch API. |
| tags | array | no |  | Tags for filtering snitch data. |
| interval | string | no |  | Time interval between snitch check-ins. |
| alertType | string | no |  | Type of alert configured for the snitch. |

### <a name="object-costReport"></a>costReport
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| credentials | vaultSecret | yes |  | Vault secret containing credentials for cost reporting. |

### <a name="object-jiralert"></a>jiralert
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| defaultIssueType | string | yes |  | Default issue type for Jira alerts. |
| defaultPriority | string | yes |  | Default priority for Jira alerts. |
| defaultReopenState | string | yes |  | Default reopen state for Jira alerts. |

### <a name="object-rhcsProvider"></a>rhcsProvider
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| issuerUrl | string | yes |  | RHCS issuer web form endpoint |
| vaultBasePath | string | yes |  | Path in KV Vault mount where certificate secrets will be stored |
| caCertUrl | string | yes |  | URL to obtain ceritifcate authority trust cert from |

### <a name="array-customMessages"></a>customMessage
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| id | string | yes |  | Unique ID of the custom message. |
| content | string | yes |  | Content of the custom message. |

### <a name="array-terraformResourcesProviderExclusions"></a>terraformResourcesProviderExclusion
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | yes |  | The provider for the exclusion. |
| excludeAllProvisioners | boolean | no |  | Whether to exclude all provisioners. |
| excludeProvisioners | array of $ref to [account-1.yml](/docs/aws/account-1.md) | no |  | List of provisioners to exclude. |

### <a name="array-terraformResourcesProviderExclusionsByProvisioner"></a>terraformResourcesProviderExclusionsByProvisioner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provisioner | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| excludedProviders | array | yes |  |  |