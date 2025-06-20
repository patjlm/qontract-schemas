# /openshift/cluster-1.yml

**Schema location:** [/openshift/cluster-1.yml](/schemas/openshift/cluster-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /openshift/cluster-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| consoleUrl | string | yes |  |  |
| kibanaUrl | string | no |  |  |
| prometheusUrl | string | yes |  |  |
| alertmanagerUrl | string | no |  |  |
| serverUrl | string | yes |  |  |
| elbFQDN | string | yes |  |  |
| auth | array of [auth](#array-auth) | yes |  |  |
| observabilityNamespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| grafanaUrl | string | no |  |  |
| ocm | $ref: [openshift-cluster-manager-1.yml](/docs/openshift/openshift-cluster-manager-1.md) | no |  |  |
| dynatraceEnvironment | $ref: [dynatrace-environment-1.yml](/docs/dependencies/dynatrace-environment-1.md) | no |  |  |
| managedGroups | array | no |  |  |
| managedClusterRoles | boolean | no |  |  |
| enableDeadMansSnitch | boolean | no |  | Flag to automate snitch creation/deletion by deadmanssnitch integration |
| enableCostReport | boolean | no |  | Flag to enable openshift cost report |
| spec | [spec](#object-spec) | no |  |  |
| externalConfiguration | [externalConfiguration](#object-externalConfiguration) | no |  |  |
| upgradePolicy |  | no |  |  |
| additionalRouters | array of [additionalRouters](#array-additionalRouters) | no |  |  |
| network | [network](#object-network) | no |  |  |
| machinePools | array of [machinePools](#array-machinePools) | no |  |  |
| peering | [peering](#object-peering) | no |  |  |
| addons | array of $ref to [cluster-addon-1.yml](/docs/openshift/cluster-addon-1.md) | no |  |  |
| insecureSkipTLSVerify | boolean | no |  |  |
| jumpHost | $ref: [jump-host-1.yml](/docs/openshift/jump-host-1.md) | no |  |  |
| automationToken | vaultSecret | no |  |  |
| clusterAdmin | boolean | no |  | should enable cluster admin for this cluster |
| clusterAdminAutomationToken | vaultSecret | no |  |  |
| description | string | yes |  |  |
| internal | boolean | yes |  | the cluster is attached to the transit gateway to the VPN, only private cluster can be internal |
| disable | [disable](#object-disable) | no |  |  |
| awsInfrastructureAccess | array of [awsInfrastructureAccess](#array-awsInfrastructureAccess) | no |  |  |
| awsInfrastructureManagementAccounts | array of [awsInfrastructureManagementAccounts](#array-awsInfrastructureManagementAccounts) | no |  |  |
| prometheus | [prometheus](#object-prometheus) | no |  |  |
| ocmSubscriptionLabels | [ocmSubscriptionLabels](#object-ocmSubscriptionLabels) | no |  |  |

### <a name="array-auth"></a>auth
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| service | string | no | github-org, github-org-team, oidc, rhidp |  |
| org | string | no |  |  |
| team | string | no |  |  |

### <a name="object-spec"></a>spec
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| product | string | yes |  |  |
| id | string | no |  |  |
| external_id | string | no |  |  |
| provider | string | yes | aws |  |
| region | string | yes |  |  |
| channel | string | no | stable, fast, candidate |  |
| version | string | yes |  |  |
| initial_version | string | yes |  |  |
| multi_az | boolean | yes |  |  |
| private | boolean | yes |  | kube API (load balancer) and router is private, access require peering |
| storage | integer | no | 1, 100, 600, 1100, 1600, 2100, 2600, 3100, 3600, 4100, 7100 |  |
| load_balancers | integer | no | 0, 4, 8, 12, 16, 20 |  |
| provision_shard_id | string | no |  |  |
| disable_user_workload_monitoring | boolean | no |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  |  |
| subnet_ids | array | no |  | Hosted Clusters only: list of subnet_ids to use with the cluster creation. |
| availability_zones | array | no |  | Hosted Clusters only: list of availability_zones to use with the cluster creation. |
| hypershift | boolean | no |  |  |
| oidc_endpoint_url | string | no |  |  |

### <a name="object-externalConfiguration"></a>externalConfiguration
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| labels | labels | yes |  |  |

### <a name="array-additionalRouters"></a>additionalRouter
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| private | boolean | yes |  |  |
| route_selectors | labels | no |  |  |

### <a name="object-network"></a>network
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| type | string | no | OpenShiftSDN, OVNKubernetes |  |
| vpc | string | no |  |  |
| service | string | no |  |  |
| pod | string | no |  |  |

### <a name="array-taints"></a>taint
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| key | string | yes |  |  |
| value | string | yes |  |  |
| effect | string | yes | NoSchedule, NoExecute, PreferNoSchedule |  |

### <a name="object-autoscale"></a>autoscale
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| min_replicas | integer | yes |  |  |
| max_replicas | integer | yes |  |  |

### <a name="array-machinePools"></a>machinePool
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| id | string | yes |  |  |
| instance_type | string | yes |  |  |
| labels | labels | no |  |  |
| subnet | string | no |  |  |
| taints | array of [taints](#array-taints) | no |  |  |
| replicas | integer | no |  |  |
| autoscale | [autoscale](#object-autoscale) | no |  |  |

### <a name="array-connections"></a>connection
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | string | no | account-vpc, account-vpc-mesh, account-tgw, cluster-vpc-requester, cluster-vpc-accepter |  |
| name | string | no |  |  |
| description | string | no |  |  |
| vpc | $ref: [vpc-1.yml](/docs/aws/vpc-1.md) | no |  |  |
| cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  |  |
| awsInfrastructureManagementAccount | $ref: [account-1.yml](/docs/aws/account-1.md) | no |  |  |
| tags | object | no |  |  |
| manageRoutes | boolean | no |  |  |
| manageAccountRoutes | boolean | no |  |  |
| manageSecurityGroups | boolean | no |  |  |
| manageRoute53Associations | boolean | no |  |  |
| allowPrivateHcpApiAccess | boolean | no |  | if set to true, enable traffic from attached TGW to reach the API and oauth server<br>of a private HCP by adapting the VPC endpoint security group |
| cidrBlock | string | no |  |  |
| cidrBlocks | array | no |  |  |
| delete | boolean | no |  |  |
| assumeRole | string | no |  |  |

### <a name="object-peering"></a>peering
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| connections | array of [connections](#array-connections) | yes |  |  |

### <a name="object-disable"></a>disable
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| integrations | array | no |  |  |

### <a name="array-awsInfrastructureAccess"></a>awsInfrastructureAccess
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| awsGroup | $ref: [group-1.yml](/docs/aws/group-1.md) | yes |  |  |
| accessLevel | string | yes | read-only, network-mgmt |  |

### <a name="array-awsInfrastructureManagementAccounts"></a>awsInfrastructureManagementAccount
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| accessLevel | string | yes | read-only, network-mgmt |  |
| default | boolean | no |  |  |

### <a name="object-prometheus"></a>prometheus
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| url | string | yes |  |  |
| auth | vaultSecret | yes |  |  |

### <a name="object-v2"></a>v2
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| tenant | string | yes |  | dynatrace tenant id to issue tokens for |
| token-spec | string | yes |  | name of the DTP token-spec to use for this cluster |

### <a name="object-dtp"></a>dtp
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| v2 | [v2](#object-v2) | no |  |  |

### <a name="object-sre-capabilities"></a>sre-capabilities
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| dtp | [dtp](#object-dtp) | no |  | request dynatrace-token-provider to issue a token for the cluster |

### <a name="object-ocmSubscriptionLabels"></a>ocmSubscriptionLabels
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| sre-capabilities | [sre-capabilities](#object-sre-capabilities) | no |  |  |