# App Interface Database Access

**Schema location:** [/app-interface/database-access-1.yml](/schemas/app-interface/database-access-1.yml)

**Description:** Schema for defining database access in app-interface. 
This includes details about the user, database, and access permissions.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /app-interface/database-access-1.yml |  |
| name | string | yes |  | The name of the database access object. |
| username | psqlIdentifier | yes |  | The username for the database access. |
| database | psqlIdentifier | yes |  | The name of the database to which access is being granted. |
| delete | boolean | no |  | Indicates whether the database access should be deleted. |
| access | array of [access](#array-access) | no |  | A list of access permissions for the database. |

### <a name="object-target"></a>target
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| dbschema | psqlIdentifier | no |  | The schema within the database to which the access applies. |

### <a name="array-access"></a>access
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| grants | array | yes |  | A list of grants specifying the permissions for the database. |
| target | [target](#object-target) | yes |  | The target schema within the database for the access permissions. |