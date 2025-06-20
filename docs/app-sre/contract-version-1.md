# Contract Version

**Schema location:** [/app-sre/contract-version-1.yml](/schemas/app-sre/contract-version-1.yml)

**Description:** Schema for defining a contract-1.yml schema version. 
Each version represents a specific iteration of a contract, including its name, 
description, associated contract, and source location.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/contract-version-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the contract version. This should uniquely identify the <br>version and indicate its purpose or scope. |
| description | string | yes |  | A detailed description of the contract version, explaining its purpose, <br>scope, and any relevant details. |
| contract | $ref: [contract-1.yml](/docs/app-sre/contract-1.md) | no |  | Reference to the contract that this version is associated with. This <br>links the version to its parent contract. |
| source | string | yes |  | The location of the contract version. This should be a valid URI pointing <br>to the source of the version, such as a document or repository. |