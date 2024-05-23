provider "aws" {
  region = "us-west-2"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "my-cluster"
  cluster_version = "1.21"
  subnets         = ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]
  vpc_id          = "vpc-0123456789abcdef0"

  node_groups = {
    eks_nodes = {
      desired_capacity = 2
      max_capacity     = 2
      min_capacity     = 2

      instance_type = "t3.medium"

      key_name = "my-key"
    }
  }
}

resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "nginx-deployment"
    namespace = "default"
  }

  spec {
    replicas = 6

    selector {
      match_labels = {
        app = "nginx"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx"
        }
      }

      spec {
        container {
          name  = "nginx"
          image = "nginx:1.21"

          ports {
            container_port = 80
          }
        }
      }
    }
  }
}
