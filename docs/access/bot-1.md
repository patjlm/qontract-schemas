# Bot

**Schema location:** [/access/bot-1.yml](/schemas/access/bot-1.yml)

**Description:** Schema for defining bot access in app-interface. 
This includes details about the bot's usernames, service accounts, 
and associated roles.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /access/bot-1.yml |  |
| labels | labels | yes |  |  |
| name | string | yes |  | The name of the bot. |
| description | string | no |  | A brief description of the bot. |
| org_username | gitlabUsername | no |  | The GitLab username associated with the bot. |
| github_username | botIdentifier | no |  | The GitHub username associated with the bot. |
| openshift_serviceaccount | string | no |  | The OpenShift service account associated with the bot, <br>in the format `<namespace>/<serviceaccount>`. |
| quay_username | identifier | no |  | The Quay username associated with the bot. |
| owner | $ref: [user-1.yml](/docs/access/user-1.md) | no |  | Reference to the owner of the bot. |
| roles | array of $ref to [role-1.yml](/docs/access/role-1.md) | no |  | A list of roles assigned to the bot. |