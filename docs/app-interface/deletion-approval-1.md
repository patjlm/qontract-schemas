# App Interface Deletion Approval

**Schema location:** [/app-interface/deletion-approval-1.yml](/schemas/app-interface/deletion-approval-1.yml)

**Description:** Schema for defining deletion approvals in app-interface. 
This includes details about the resource being deleted, 
the type of resource, and the expiration of the approval.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-interface/deletion-approval-1.yml |  |
| expiration | string | yes |  | The expiration date for the deletion approval. <br>After this date, the approval is no longer valid. |
| type | string | yes |  | The type of resource for which deletion is being approved. |
| name | string | yes |  | The name of the resource for which deletion is being approved. |