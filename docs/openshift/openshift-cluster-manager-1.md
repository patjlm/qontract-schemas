# /openshift/openshift-cluster-manager-1.yml

**Schema location:** [/openshift/openshift-cluster-manager-1.yml](/schemas/openshift/openshift-cluster-manager-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/openshift-cluster-manager-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| orgId | string | yes |  | The internal OCM organization ID that can be found via<br>ocm whoami | jq .organization.id |
| environment | $ref: [openshift-cluster-manager-environment-1.yml](/docs/openshift/openshift-cluster-manager-environment-1.md) | yes |  |  |
| accessTokenClientId | string | no |  |  |
| accessTokenUrl | string | no |  |  |
| accessTokenClientSecret | vaultSecret | no |  |  |
| allowedClusterExternalConfigLabels | array | no |  |  |
| addonManagedUpgrades | boolean | no |  |  |
| addonUpgradeTests | array of [addonUpgradeTests](#array-addonUpgradeTests) | no |  | trigger a job in jenkins following an addon upgrade |
| recommendedVersions | array of [recommendedVersions](#array-recommendedVersions) | no |  |  |
| recommendedVersionWeight | [recommendedVersionWeight](#object-recommendedVersionWeight) | no |  |  |
| blockedVersions | array | no |  | List of versions that will be rejected for upgrades. They can be regular expressions |
| upgradePolicyAllowedWorkloads | array | no |  | List of workloads that are allowed to be defined as cluster upgrade policy workload |
| upgradePolicyAllowedMutexes | array | no |  | List of mutexes that are allowed to be defined as cluster upgrade policy mutex |
| ausClusterHealthChecks | array of [ausClusterHealthChecks](#array-ausClusterHealthChecks) | no |  | List of cluster health check providers |
| sectors | array of [sectors](#array-sectors) | no |  | List of allowed deployment sectors and their dependencies |
| upgradePolicyDefaults | array | no |  | List of default upgrade policies to apply to clusters by external configuration labels |
| upgradePolicyClusters | array of [upgradePolicyClusters](#array-upgradePolicyClusters) | no |  | List of clusters to define upgrade policies for (no cluster management in such OCM orgs) |
| inheritVersionData | array of $ref to [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | no |  | list of OCM organizations from which we will retrieve cluster version informations (current versions stats, soak days, sectors, ..). |
| publishVersionData | array of $ref to [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | no |  | list of OCM organizations to which we will publish cluster version informations (current versions stats, soak days, sectors, ..) |
| disable | [disable](#object-disable) | no |  |  |

### <a name="array-addonUpgradeTests"></a>addonUpgradeTest
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| addon | $ref: [cluster-addon-1.yml](/docs/openshift/cluster-addon-1.md) | yes |  |  |
| instance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | yes |  |  |
| name | string | yes |  |  |

### <a name="array-recommendedVersions"></a>recommendedVersion
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| recommendedVersion | string | yes |  | Recommended version for provisioning new clusters |
| initialVersion | string | yes |  | Initial version string, as used by the OCM API |
| workload | string | yes |  | Workload the version is recommended for |
| channel | string | no |  | Channel version can be found, stable if not set |

### <a name="object-recommendedVersionWeight"></a>recommendedVersionWeight
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| majority | number | no |  | most used version currently running that workload |
| highest | number | no |  | highest version currently running that workload |

### <a name="array-ausClusterHealthChecks"></a>ausClusterHealthCheck
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | yes | telemeter |  |
| enforced | boolean | yes |  |  |

### <a name="array-dependencies"></a>dependency
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | sector name |
| ocm | $ref: [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | no |  |  |

### <a name="array-sectors"></a>sector
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | sector name |
| maxParallelUpgrades | string | no |  | The maximum number of upgrades that can happen at any given time within that sector.<br>This string must contain an bare integer or percentage of the number of clusters in the sector.<br>Default is "100%", so any number of parallel upgrades is allowed. |
| dependencies | array of [dependencies](#array-dependencies) | no |  | list of sectors this one is depending on |

### <a name="object-spec"></a>spec
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| id | string | no |  |  |

### <a name="array-upgradePolicyClusters"></a>upgradePolicyCluster
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  | cluster name |
| serverUrl | string | no |  | cluster server url |
| spec | [spec](#object-spec) | no |  |  |
| upgradePolicy |  | yes |  |  |

### <a name="object-disable"></a>disable
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| integrations | array | no |  | integrations to disable for the ocm organization |