provider "azurearm" {
features{}
}

resource "azurearm_resource_group" "rg" {
    name = "ai-rg"
    location = "East US"
}

resource "azurearm_kubernetes_cluster" "aks" {
    name = "ai-aks"
    location = azurearm_resource_group.rg.location
    resource_group_name= azurearm_resource_group.rg.name
    dns_prefix = "aiaks"


default_node_pool {
    name = "default"
    node_count = 2
    vm_size = "Standard_B2s"
}

identity{
    type = "SystemAssigned"
}

}