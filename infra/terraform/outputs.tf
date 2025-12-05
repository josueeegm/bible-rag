output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "keyvault_uri" {
  value = azurerm_key_vault.kv.vault_uri
}

output "log_analytics_workspace_id" {
  value = azurerm_log_analytics_workspace.law.id
}

output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}
