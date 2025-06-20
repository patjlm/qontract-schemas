# App Interface Credentials Request

**Schema location:** [/app-interface/credentials-request-1.yml](/schemas/app-interface/credentials-request-1.yml)

**Description:** Schema for defining a credentials request in app-interface. 
This includes details about the user requesting the credentials 
and the credentials being requested.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/credentials-request-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the credentials request object. |
| description | string | yes |  | A brief description of the credentials request. |
| user | $ref: [user-1.yml](/docs/access/user-1.md) | yes |  | Reference to the user who is requesting the credentials. |
| credentials | string | yes |  | The credentials being requested. |