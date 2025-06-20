# /app-sre/product-1.yml

**Schema location:** [/app-sre/product-1.yml](/schemas/app-sre/product-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/product-1.yml |  |
| labels | labels | yes |  |  |
| name | extendedIdentifier | yes |  |  |
| description | string | yes |  |  |
| productOwners | array of [productOwners](#array-productOwners) | yes |  | Teams or individuals who is/are responsible for the running instance of the software. |

### <a name="array-productOwners"></a>productOwner
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| email | string | yes |  |  |