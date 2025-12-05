variable "subscription_id" {
  description = "Azure subscription id"
  type        = string
}

variable "resource_group_name" {
  description = "Resource Group to create"
  type        = string
  default     = "gio-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "aks_name" {
  description = "AKS Cluster name"
  type        = string
  default     = "gio-aks"
}

variable "acr_name" {
  description = "ACR name (must be globally unique & lowercase)"
  type        = string
  default     = "giobibleacr2032"
}

variable "keyvault_name" {
  description = "Key Vault name"
  type        = string
  default     = "giobiblekv2032"
}

variable "log_analytics_name" {
  description = "Log Analytics workspace name"
  type        = string
  default     = "giobiblelaw2032"
}

variable "storage_account_name" {
  description = "Storage account name (lowercase, 3-24 chars)"
  type        = string
  default     = "giobiblestorageyessir"
}

variable "tenant_id" {}
variable "client_id" {}
variable "client_secret" {}

variable "sp_object_id" {
  type = string
}