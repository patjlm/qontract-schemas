# App Interface SQL Query

**Schema location:** [/app-interface/app-interface-sql-query-1.yml](/schemas/app-interface/app-interface-sql-query-1.yml)

**Description:** Schema for defining SQL queries for automated execution.
Includes details about the query, its schedule, output, and overrides.


| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-interface/app-interface-sql-query-1.yml |  |
| labels | labels | yes |  |  |
| name | k8sValidContainerName | yes |  | The name of the SQL query object, following Kubernetes container naming conventions. |
| namespace | $ref: [namespace-1.yml](/docs/openshift/namespace-1.md) | yes |  | Reference to the namespace where the SQL query will be executed. |
| identifier | longIdentifier | yes |  | The identifier for the RDS instance as defined in a namespace instantiation. |
| requestor | $ref: [user-1.yml](/docs/access/user-1.md) | no |  | Reference to the user who requested the SQL query. |
| overrides | [overrides](#object-overrides) | no |  | Overrides for database connection parameters. |
| output | string | yes | stdout, filesystem, encrypted | The output method for the SQL query results. Options include:<br>- `stdout`: Print results to standard output.<br>- `filesystem`: Save results to the filesystem.<br>- `encrypted`: Save results in an encrypted format. |
| schedule | string | no |  | The schedule for executing the SQL query, defined in cron format. |
| delete | boolean | no |  | Indicates whether the SQL query should be deleted after execution. |
| query | query | no |  | The SQL query to be executed. |
| queries | array | no |  | A list of SQL queries to be executed. |

### <a name="object-overrides"></a>overrides
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| db_port | string | no |  | The port number for the database connection. |
| db_name | string | no |  | The name of the database to connect to. |
| db_user | string | no |  | The username for the database connection. |