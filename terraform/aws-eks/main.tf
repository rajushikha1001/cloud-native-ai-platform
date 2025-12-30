provider "aws" {
    region = "us-east-1"
}

module "eks" {
    source = "terraform-aws-modules/eks/aws"
    cluster_name = "ai-eks"
    cluster_version = "1.29"
    subnet_ids = []
    vpc_id = ""
}