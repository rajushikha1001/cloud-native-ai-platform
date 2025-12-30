provider "google" {
    project = "test-project"
    region = "us-central1"
}

resource "google_container_cluster" "gke" {
name = "ai-gke"
location = "us-central1"
intial_node_count = 2
}