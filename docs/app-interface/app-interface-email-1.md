# app-interface-email

**Schema location:** [/app-interface/app-interface-email-1.yml](/schemas/app-interface/app-interface-email-1.yml)

**Description:** Specification for a single automated email message. 
Recipients can be static or dynamic based on service, cluster, namespace, aws account, role, or user relations.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/app-interface-email-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | Internal name for an email instantiation. |
| subject | nonEmptyString | yes |  | Subject line of email message |
| to | [to](#object-to) | yes |  | Recipients of email message |
| body | nonEmptyString | yes |  | Body of email message |

### <a name="object-to"></a>to
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| aliases | array | no |  | Recipient group aliases. Group names and membership logic defined in qontract-reconcile email-sender integration. |
| services | array of $ref to [app-1.yml](/docs/app-sre/app-1.md) | no |  | Dynamic recipient group depending on service <> role <> user relations. |
| clusters | array of $ref to [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  | Dynamic recipient group depending on cluster <> role <> user relations. |
| namespaces | array of $ref to [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  | Dynamic recipient group depending on namespace <> role <> user relations. |
| aws_accounts | array of $ref to [account-1.yml](/docs/aws/account-1.md) | no |  | Dynamic recipient group depending on aws account <> role <> user relations. |
| roles | array of $ref to [role-1.yml](/docs/access/role-1.md) | no |  | Dynamic recipient group depending on role <> user relations. |
| users | array of $ref to [user-1.yml](/docs/access/user-1.md) | no |  | Explicit list of recipients by user schema references. |