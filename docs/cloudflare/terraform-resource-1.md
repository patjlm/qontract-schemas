# /cloudflare/terraform-resource-1.yml

**Schema location:** [/cloudflare/terraform-resource-1.yml](/schemas/cloudflare/terraform-resource-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | no | /cloudflare/terraform-resource-1.yml |  |
| provider | string | yes |  |  |
| identifier | longIdentifier | no |  |  |
| name | string | no |  |  |
| content_from_github | [content_from_github](#object-content-from-github) | no |  |  |
| vars | array of [vars](#array-vars) | no |  |  |
| zone | string | no |  |  |
| plan |  | no | enterprise, free |  |
| type |  | no | full, partial |  |
| settings | object | no |  |  |
| argo | [argo](#object-argo) | no |  |  |
| tiered_cache | [tiered_cache](#object-tiered-cache) | no |  |  |
| cache_reserve | [cache_reserve](#object-cache-reserve) | no |  |  |
| records | array | no |  |  |
| workers | array of [workers](#array-workers) | no |  |  |
| certificates | array of [certificates](#array-certificates) | no |  |  |
| custom_ssl_certificates | array of [custom_ssl_certificates](#array-custom-ssl-certificates) | no |  |  |
| destination_conf | string | no |  |  |
| enabled | boolean | no |  |  |
| logpull_options | string | no |  |  |
| ownership_challenge | string | no |  |  |
| dataset | string | no |  |  |
| frequency | string | no |  |  |
| filter | string | no |  |  |
| kind | string | no |  |  |

### <a name="object-content-from-github"></a>content_from_github
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| repo | string | yes |  |  |
| path | string | yes |  |  |
| ref | string | yes |  |  |

### <a name="array-vars"></a>var
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| name | string | yes |  |  |
| text | string | yes |  |  |

### <a name="object-argo"></a>argo
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| tiered_caching | boolean | no |  |  |
| smart_routing | boolean | no |  |  |

### <a name="object-tiered-cache"></a>tiered_cache
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| cache_type | string | yes | generic, smart |  |

### <a name="object-cache-reserve"></a>cache_reserve
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| enabled | boolean | no |  |  |

### <a name="array-workers"></a>worker
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| identifier | string | yes |  |  |
| pattern | string | yes |  |  |
| script_name | string | yes |  |  |

### <a name="array-certificates"></a>certificate
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| identifier | string | no |  |  |
| type | string | no | advanced |  |
| hosts | array | no |  |  |
| validation_method | string | no | txt |  |
| validity_days | integer | no | 90 |  |
| certificate_authority | string | no | lets_encrypt |  |
| cloudflare_branding | boolean | no |  |  |
| wait_for_active_status | boolean | no |  |  |

### <a name="object-certificate-secret"></a>certificate_secret
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| certificate | vaultSecret | yes |  |  |
| key | vaultSecret | yes |  |  |

### <a name="array-custom-ssl-certificates"></a>custom_ssl_certificate
| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| identifier | string | no |  |  |
| type | string | no | legacy_custom, sni_custom |  |
| bundle_method | string | no | ubiquitous, optimal, force |  |
| geo_restrictions | string | no | us, eu, highest_security |  |
| certificate_secret | [certificate_secret](#object-certificate-secret) | no |  |  |