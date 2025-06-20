# /access/role-1.yml

**Schema location:** [/access/role-1.yml](/schemas/access/role-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/role-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  |  |
| description | string | no |  |  |
| expirationDate | string | no |  |  |
| permissions | array of $ref to [permission-1.yml](/docs/access/permission-1.md) | yes |  |  |
| oidc_permissions | array of $ref to [oidc-permission-1.yml](/docs/access/oidc-permission-1.md) | no |  |  |
| tag_on_cluster_updates | boolean | no |  |  |
| access | array of [access](#array-access) | no |  |  |
| aws_groups | array of $ref to [group-1.yml](/docs/aws/group-1.md) | no |  |  |
| user_policies | array of $ref to [policy-1.yml](/docs/aws/policy-1.md) | no |  |  |
| glitchtip_teams | array of $ref to [glitchtip-team-1.yml](/docs/dependencies/glitchtip-team-1.md) | no |  |  |
| glitchtip_roles | array of [glitchtip_roles](#array-glitchtip-roles) | no |  |  |
| sendgrid_accounts | array of $ref to [sendgrid-account-1.yml](/docs/dependencies/sendgrid-account-1.md) | no |  |  |
| cloudflare_access | array of $ref to [account-role-1.yml](/docs/cloudflare/account-role-1.md) | no |  |  |
| self_service | array of [self_service](#array-self-service) | no |  |  |
| ldapGroup | [ldapGroup](#object-ldapGroup) | no |  |  |
| memberSources | array of [memberSources](#array-memberSources) | no |  |  |

### <a name="array-access"></a>access
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | no |  |  |
| role | string | no |  |  |
| cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  |  |
| group | string | no |  |  |
| clusterRole | string | no |  |  |

### <a name="array-glitchtip-roles"></a>glitchtip_role
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| organization | $ref: [glitchtip-organization-1.yml](/docs/dependencies/glitchtip-organization-1.md) | yes |  |  |
| role | string | yes | member, admin, manager, owner |  |

### <a name="array-self-service"></a>self_service
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| description | string | no |  |  |
| change_type | $ref: [change-type-1.yml](/docs/app-interface/change-type-1.md) | no |  |  |
| resources | array | no |  |  |
| datafiles | array of $ref to  | no |  |  |

### <a name="object-ldapGroup"></a>ldapGroup
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | ldapGroupName | yes |  | The name of the LDAP/Rover group |
| notes | string | no |  | Notes added to the LDAP/Rover group |
| membersAreOwners | boolean | no |  | Grant "owner" permission to all members of the LDAP/Rover group |

### <a name="array-memberSources"></a>memberSource
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| provider | $ref: [membership-provider-1.yml](/docs/access/membership-provider-1.md) | no |  |  |
| group | string | no |  |  |