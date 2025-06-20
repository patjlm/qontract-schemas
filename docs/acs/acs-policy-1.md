# Policy

**Schema location:** [/acs/acs-policy-1.yml](/schemas/acs/acs-policy-1.yml)

**Description:** Schema for defining security policies in Red Hat Advanced Cluster Security (ACS). 
Policies are used to enforce security standards and best practices in Kubernetes 
clusters. This schema includes details about policy severity, categories, scope, 
integrations, and conditions.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /acs/acs-policy-1.yml |  |
| labels | labels | no |  |  |
| description | string | no |  | A brief description of the policy, explaining its purpose and functionality. |
| name | string | yes |  | The name of the policy. This should be unique and descriptive. |
| integrations | [integrations](#object-integrations) | no |  | Configuration for integrations associated with the policy, such as <br>notifiers for external systems. |
| severity | string | yes | low, medium, high, critical | The severity level of the policy. This indicates the importance of the <br>policy and the potential impact of violations. |
| categories | array | yes |  | A list of categories that the policy belongs to. Categories help organize <br>policies based on their purpose or focus area. |
| scope | [scope](#object-scope) | yes |  | The scope of the policy, defining the level (cluster or namespace) and <br>the specific clusters or namespaces it applies to. |
| conditions | array | yes |  | A list of conditions that define the criteria for policy violations. <br>Each condition specifies a rule that must be met for the policy to trigger. |

### <a name="object-jira"></a>jira
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| escalationPolicy | $ref: [escalation-policy-1.yml](/docs/app-sre/escalation-policy-1.md) | yes |  | Reference to the escalation policy used for Jira integration. |

### <a name="object-notifiers"></a>notifiers
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| jira | [jira](#object-jira) | no |  | Configuration for integrating the policy with Jira for issue tracking. |

### <a name="object-integrations"></a>integrations
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| notifiers | [notifiers](#object-notifiers) | no |  | Configuration for notifier integrations associated with the policy. |

### <a name="object-scope"></a>scope
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| level | string | no | cluster, namespace | The level at which the policy is applied. This can be either `cluster` <br>or `namespace`. |
| clusters | array of $ref to [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  | A list of clusters that the policy applies to when the level is `cluster`. |
| namespaces | array of $ref to [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  | A list of namespaces that the policy applies to when the level is `namespace`. |