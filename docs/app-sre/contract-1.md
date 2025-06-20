# Contract

**Schema location:** [/app-sre/contract-1.yml](/schemas/app-sre/contract-1.yml)

**Description:** Schema for defining contracts.
Contracts are agreements between the platform operator and platform tenants.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/contract-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the contract. This should be a unique identifier that <br>clearly represents the purpose or scope of the contract. |
| description | string | yes |  | A detailed description of the contract, explaining its purpose, <br>scope, and any relevant details. |
| source | string | yes |  | The location of the contract. This should be a valid URI pointing <br>to the source of the contract, such as a document or repository. |