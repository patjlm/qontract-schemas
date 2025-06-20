# /aws/elasticsearch-defaults-1.yml

**Schema location:** [/aws/elasticsearch-defaults-1.yml](/schemas/aws/elasticsearch-defaults-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/elasticsearch-defaults-1.yml |  |
| elasticsearch_version | string | no |  |  |
| ebs_options | [ebs_options](#object-ebs-options) | no |  |  |
| encrypt_at_rest | [encrypt_at_rest](#object-encrypt-at-rest) | no |  |  |
| node_to_node_encryption | [node_to_node_encryption](#object-node-to-node-encryption) | no |  |  |
| domain_endpoint_options | [domain_endpoint_options](#object-domain-endpoint-options) | no |  |  |
| cluster_config | [cluster_config](#object-cluster-config) | no |  |  |
| snapshot_options | [snapshot_options](#object-snapshot-options) | no |  |  |
| vpc_options | [vpc_options](#object-vpc-options) | no |  |  |
| advanced_options | [advanced_options](#object-advanced-options) | no |  |  |
| advanced_security_options | [advanced_security_options](#object-advanced-security-options) | no |  |  |
| auth | [auth](#object-auth) | no |  |  |

### <a name="object-ebs-options"></a>ebs_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| ebs_enabled | boolean | yes |  |  |
| iops | integer | no |  |  |
| volume_size | integer | no |  |  |
| volume_type | string | no | standard, gp2, io1 |  |

### <a name="object-encrypt-at-rest"></a>encrypt_at_rest
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | yes |  |  |

### <a name="object-node-to-node-encryption"></a>node_to_node_encryption
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | yes |  |  |

### <a name="object-domain-endpoint-options"></a>domain_endpoint_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enforce_https | boolean | no |  |  |
| tls_security_policy | string | no | Policy-Min-TLS-1-0-2019-07, Policy-Min-TLS-1-2-2019-07 |  |

### <a name="object-zone-awareness-config"></a>zone_awareness_config
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| availability_zone_count | integer | no | 2, 3 |  |

### <a name="object-cold-storage-options"></a>cold_storage_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | no |  |  |

### <a name="object-cluster-config"></a>cluster_config
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| instance_type | string | no |  |  |
| instance_count | integer | no |  |  |
| dedicated_master_enabled | boolean | no |  |  |
| dedicated_master_type | string | no |  |  |
| dedicated_master_count | integer | no |  |  |
| zone_awareness_enabled | boolean | no |  |  |
| zone_awareness_config | [zone_awareness_config](#object-zone-awareness-config) | no |  |  |
| warm_enabled | boolean | no |  |  |
| warm_type | string | no |  |  |
| warm_count | integer | no |  |  |
| cold_storage_options | [cold_storage_options](#object-cold-storage-options) | no |  |  |

### <a name="object-snapshot-options"></a>snapshot_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| automated_snapshot_start_hour | integer | yes |  |  |

### <a name="object-vpc-options"></a>vpc_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| security_group_ids | array | no |  |  |
| subnet_ids | array | yes |  |  |

### <a name="object-advanced-options"></a>advanced_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| rest.action.multi.allow_explicit_index | string | no |  |  |
| indices.query.bool.max_clause_count | string | no |  |  |

### <a name="object-master-user-secret"></a>master_user_secret
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | string | yes |  |  |
| version | integer | yes |  |  |

### <a name="object-master-user-options"></a>master_user_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| master_user_secret | [master_user_secret](#object-master-user-secret) | yes |  | Secret containing the user/password authentication data. It must only<br>contain the "master_user_name" and "master_user_password" keys |

### <a name="object-advanced-security-options"></a>advanced_security_options
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | yes |  |  |
| internal_user_database_enabled | boolean | no |  |  |
| master_user_options | [master_user_options](#object-master-user-options) | no |  |  |

### <a name="object-admin-user-credentials"></a>admin_user_credentials
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| path | string | yes |  |  |
| version | integer | yes |  |  |

### <a name="object-auth"></a>auth
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| admin_user_arn | string | no |  | The ARN for the admin user.<br>This option is mutually exclusive with admin_user_credentials. |
| admin_user_credentials | [admin_user_credentials](#object-admin-user-credentials) | no |  | Secret containing the user/password authentication data. It must only<br>contain the "master_user_name" and "master_user_password" keys.<br>The admin user password must be at least 8 chars long, contain at least one<br>uppercase letter, one lowercase letter, one number, and one special character.<br>This option is mutually exclusive with admin_user_arn. |