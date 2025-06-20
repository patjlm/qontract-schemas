# /dependencies/jenkins-instance-1.yml

**Schema location:** [/dependencies/jenkins-instance-1.yml](/schemas/dependencies/jenkins-instance-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /dependencies/jenkins-instance-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | yes |  |  |
| serverUrl | string | no |  |  |
| token | vaultSecret | no |  |  |
| previousUrls | array | no |  |  |
| plugins | array | no |  |  |
| deleteMethod | string | no | manual |  |
| managedProjects | array | no |  |  |
| buildsCleanupRules | array of [buildsCleanupRules](#array-buildsCleanupRules) | no |  |  |
| workerFleets | array of [workerFleets](#array-workerFleets) | no |  |  |

### <a name="array-buildsCleanupRules"></a>buildsCleanupRule
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| keep_hours | integer | yes |  |  |

### <a name="object-sshConnector"></a>sshConnector
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| credentialsId | string | yes |  | Jenkins credential name of ssh private key to be used for logging in to the remote host. |
| jvmOptions | string | no |  | JAVA Options to set in the agents |
| launchTimeoutSeconds | integer | no |  |  |
| maxNumRetries | integer | no |  |  |
| port | integer | no |  |  |
| retryWaitTime | integer | no |  |  |
| sshHostKeyVerificationStrategy | string | no | nonVerifyingKeyVerificationStrategy |  |

### <a name="array-workerFleets"></a>workerFleet
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| account |  | yes |  |  |
| identifier | longIdentifier | yes |  | ASG used for this Jenkins cloud, need to match an ASG identifier. |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  |  |
| sshConnector | [sshConnector](#object-sshConnector) | yes |  |  |
| fsRoot | string | no |  |  |
| labelString | string | yes |  |  |
| numExecutors | integer | no |  |  |
| idleMinutes | integer | no |  |  |
| minSpareSize | integer | no |  |  |
| maxTotalUses | integer | no |  |  |
| noDelayProvision | boolean | no |  |  |
| alwaysReconnect | boolean | no |  |  |