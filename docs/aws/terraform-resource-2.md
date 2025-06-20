# /aws/terraform-resource-2.yml

**Schema location:** [/aws/terraform-resource-2.yml](/schemas/aws/terraform-resource-2.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /aws/terraform-resource-2.yml |  |
| provider | string | yes |  |  |
| annotations | annotations | no |  |  |
| lifecycle |  | no |  |  |
| identifier | string | no |  |  |
| name | string | no |  |  |
| variables | object | no |  |  |
| policies | array | no |  |  |
| policy | object | no |  |  |
| fifo_topic | boolean | no |  |  |
| user_policy | object | no |  |  |
| role_policy | object | no |  |  |
| assume_role | object | no |  |  |
| assume_condition | object | no |  |  |
| assume_action | string | no |  |  |
| database_access | array of $ref to [database-access-1.yml](/docs/app-interface/database-access-1.md) | no |  |  |
| inline_policy | object | no |  |  |
| output_resource_name | longIdentifier | no |  |  |
| output_format |  | no |  |  |
| defaults | string | no |  |  |
| parameter_group | resourceref | no |  |  |
| old_parameter_group | resourceref | no |  |  |
| blue_green_deployment | [blue_green_deployment](#object-blue-green-deployment) | no |  |  |
| region |  | no |  |  |
| overrides | object | no |  |  |
| es_identifier | string | no |  |  |
| availability_zone | string | no |  |  |
| enhanced_monitoring | boolean | no |  |  |
| grafana_datasource | boolean | no |  | is rds instance used as a grafana datasource |
| replica_source | string | no |  |  |
| output_resource_db_name | string | no |  |  |
| reset_password | string | no |  |  |
| ca_cert | vaultSecret | no |  |  |
| secret | vaultSecret | no |  |  |
| storage_class | string | no |  |  |
| specs | array | no |  |  |
| s3_events | array | no |  |  |
| replication_configurations | array | no |  |  |
| event_notifications | array | no |  |  |
| data_classification | [data_classification](#object-data-classification) | no |  |  |
| sqs_identifier | string | no |  |  |
| bucket_policy | object | no |  |  |
| kms_encryption | boolean | no |  |  |
| mirror | $ref: [container-image-mirror-1.yml](/docs/dependencies/container-image-mirror-1.md) | no |  |  |
| public | boolean | no |  |  |
| domain | object | no |  |  |
| aws_infrastructure_access | [aws_infrastructure_access](#object-aws-infrastructure-access) | no |  |  |
| vpc | $ref: [vpc-1.yml](/docs/aws/vpc-1.md) | no |  |  |
| certificate_arn | string | no |  |  |
| ssl_policy | string | no |  |  |
| idle_timeout | integer | no |  |  |
| enable_http2 | boolean | no |  | indicates whether HTTP/2 is enabled |
| ingress_cidr_blocks | array | no |  | ingress cidr blocks to allow for an alb |
| ip_address_type | string | no | ipv4, dualstack |  |
| access_logs | boolean | no |  |  |
| mutual_authentication | object | no |  |  |
| targets | array | no |  |  |
| rules | array | no |  |  |
| cloudinit_configs | array | no |  |  |
| publish_log_types | array | no |  |  |
| image | array of [image](#array-image) | no |  |  |
| secrets_prefix | string | no |  |  |
| api_proxy_uri | string | no |  |  |
| sms_role_ext_id | string | no |  |  |
| cognito_callback_bucket_name | string | no |  |  |
| vpc_arn | string | no |  |  |
| vpc_id | string | no |  |  |
| vpce_id | string | no |  |  |
| subnet_ids | array | no |  |  |
| domain_name | string | no |  |  |
| network_interface_ids | array | no |  |  |
| openshift_ingress_load_balancer_arn | string | no |  |  |
| insights_callback_urls | array | no |  |  |
| pre_signup_lambda_github_release_url | string | no |  |  |
| subscriptions | array of [subscriptions](#array-subscriptions) | no |  |  |
| records | array | no |  |  |
| extra_tags | object | no |  |  |
| users | array of [users](#array-users) | no |  |  |
| managed_by_erv2 | boolean | no |  | Manage the resource with erv2 |
| delete | boolean | no |  | Flag to delete the resource |
| module | [module](#object-module) | no |  |  |
| module_overrides |  | no |  |  |
| max_session_duration | integer | no |  | Maximum session duration (in seconds) that you want to set for the specified role.<br>If you do not specify a value for this setting, the default maximum of one hour is applied.<br>This setting can have a value from 3600 (1 hour) to 43200 (12 hours). |

### <a name="object-target"></a>target
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| parameter_group | resourceref | no |  |  |
| engine_version | string | no |  |  |
| instance_class | string | no |  |  |
| allocated_storage | integer | no |  | The amount of storage in gibibytes (GiB) to allocate for the green DB instance.<br>You can choose to increase or decrease the allocated storage on the green DB instance.<br>Range from 20GiB to 16TiB (20-16384). |
| storage_type | string | no | gp3, io1, io2 |  |
| iops | integer | no |  |  |
| storage_throughput | integer | no |  |  |

### <a name="object-blue-green-deployment"></a>blue_green_deployment
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | no |  |  |
| switchover | boolean | no |  |  |
| switchover_timeout | integer | no |  | The amount of time, in seconds, for the switchover to complete.<br>If the switchover takes longer than the specified duration,<br>then any changes are rolled back, and no changes are made to the environments.<br>The default timeout period is 300 seconds (5 minutes).<br>This is the max allowed downtime, use it to plan maintenance window. |
| delete | boolean | no |  |  |
| target | [target](#object-target) | no |  |  |

### <a name="object-data-classification"></a>data_classification
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| loss_impact | string | no | high, medium, low, none |  |

### <a name="object-aws-infrastructure-access"></a>aws_infrastructure_access
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cluster | $ref: [cluster-1.yml](/docs/openshift/cluster-1.md) | no |  |  |
| access_level | string | no |  |  |
| assume_role | string | no |  |  |

### <a name="object-upstream"></a>upstream
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| instance | $ref: [jenkins-instance-1.yml](/docs/dependencies/jenkins-instance-1.md) | no |  |  |

### <a name="array-image"></a>image
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| upstream | [upstream](#object-upstream) | no |  |  |

### <a name="array-subscriptions"></a>subscription
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| protocol | string | no | email, sms |  |
| endpoint | string | no |  |  |

### <a name="array-users"></a>user
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | identifierLowercase64 | yes |  |  |
| secret | vaultSecret | yes |  |  |

### <a name="object-module"></a>module
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| url | string | no |  |  |
| path | string | no |  |  |
| ref | string | no |  |  |