# /openshift/external-resource-1.yml

**Schema location:** [/openshift/external-resource-1.yml](/schemas/openshift/external-resource-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /openshift/external-resource-1.yml |  |
| provider | string | yes | aws, cloudflare, gcp-project, cna-experimental | terraform provider type to use |
| provisioner | crossref | yes |  | the provisioning entity |
| resources | array | yes |  | resources to provision |