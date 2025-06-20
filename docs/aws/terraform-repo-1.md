# /aws/terraform-repo-1.yml

**Schema location:** [/aws/terraform-repo-1.yml](/schemas/aws/terraform-repo-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /aws/terraform-repo-1.yml |  |
| account | $ref: [account-1.yml](/docs/aws/account-1.md) | yes |  |  |
| app | $ref: [app-1.yml](/docs/app-sre/app-1.md) | no |  |  |
| name | string | yes |  |  |
| repository | string | yes |  | GitLab repository URL |
| ref | string | yes |  | commit SHA, not a branch like main or master |
| projectPath | string | yes |  | path in the repo where the terraform files are located |
| delete | boolean | no |  | set to true to delete the repo |
| requireFips | boolean | no |  | whether this repo should be validated to ensure it is using FIPS endpoints for AWS |
| tfVersion | string | yes | 1.4.5, 1.4.7, 1.5.7, 1.6.6, 1.7.5, 1.8.5 | Which version of terraform binary to use |
| forceRerunTimestamp | string | no |  | force a rerun of tf-repo using ISO8601 format which can be grabbed with https://www.utctime.net/ |
| variables | object | no |  | Vault paths defining where Terraform inputs are read from and where Terraform outputs are written to |