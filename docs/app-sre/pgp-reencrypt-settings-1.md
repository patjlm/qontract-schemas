# /app-sre/pgp-reencrypt-settings-1.yml

**Schema location:** [/app-sre/pgp-reencrypt-settings-1.yml](/schemas/app-sre/pgp-reencrypt-settings-1.yml)

**Description:** No description

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| $schema | string | yes | /app-sre/pgp-reencrypt-settings-1.yml |  |
| public_gpg_key | string | yes |  | This PGP Public key will be used to encrypt the users, instead of the users keys.<br>It is owned by APP-SRE. The field name is not a type as it is consistent with access/user-1.yml schema. |
| private_pgp_key_vault_path | string | yes |  | This is the vault path to the private key used for reencryption. |
| reencrypt_vault_path | string | yes |  | Base path to read/write pgp encrypted entries from/to. |
| aws_account_output_vault_path | string | yes |  | Path to write reencrypted AWS Account passwords to. |
| skip_aws_accounts | array of $ref to [account-1.yml](/docs/aws/account-1.md) | no |  | This is kind of a feature flipper. Access requests for AWS accounts listed here will be sent<br>using the SMTP mail send implementation in terraform-users integration. |