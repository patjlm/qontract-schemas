# /app-sre/integration-spec-1.yml

**Schema location:** [/app-sre/integration-spec-1.yml](/schemas/app-sre/integration-spec-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-sre/integration-spec-1.yml |  |
| cache | boolean | no |  | integration requires cache |
| command | string | no | qontract-reconcile, app-interface-metrics-exporter, app-interface-reporter, glitchtip-access-reporter, glitchtip-access-revalidation, saas-metrics-exporter | command to run |
| disableUnleash | boolean | no |  | disable integration interaction with unleash instance |
| environmentAware | boolean | no |  | integration is aware of the environment it is running in |
| extraArgs | string | no |  | additional arguments to pass to integration |
| extraEnv | array of [extraEnv](#array-extraEnv) | no |  |  |
| imageRef | string | no |  |  |
| internalCertificates | boolean | no |  | integration requires internal certificates to execute |
| logs | [logs](#object-logs) | no |  | ship logs to providers (cloudwatch is enabled by default) |
| resources |  | yes |  |  |
| fluentdResources |  | no |  |  |
| sleepDurationSecs | string | no |  | time to sleep in seconds between integration executions |
| state | boolean | no |  | integration is stateful |
| storage | string | no |  | size of cache storage |
| storageClassName | string | no | gp2, gp2-csi, gp3-csi | kubernetes storage class name for the cache |
| trigger | boolean | no |  | integration is an openshift-saas-deploy trigger |
| cron | string | no |  | cron expression for integration execution |
| dashdotdb | boolean | no |  | integration interacts with dashdotdb |
| concurrencyPolicy | string | no | Allow, Forbid, Replace | how to treat concurrent executions of the integration |
| restartPolicy | string | no | Always, OnFailure, Never | restarts of the integration |
| successfulJobHistoryLimit | integer | no |  | number of history records reserved for successful integration executions |
| failedJobHistoryLimit | integer | no |  | number of history records reserved for failed integration executions |
| enablePushgateway | boolean | no |  | push metrics at the end of the run to the configured Pushgateway |

### <a name="array-extraEnv"></a>extraEnv
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| secretName | string | no |  | secret name to get environment variable from |
| secretKey | string | no |  | secret key to get value from and to use as the environment variable name |
| name | string | no |  | environment variable name |
| value | string | no |  | environment variable value |

### <a name="object-logs"></a>logs
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| slack | boolean | no |  | ship logs to slack |
| googleChat | boolean | no |  | ship logs to google chat |