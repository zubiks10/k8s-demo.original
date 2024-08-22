from kubernetes import client, config

def create_pod(api_instance, pod_manifest):
    """Create a Kubernetes Pod based on the provided manifest."""
    try:
        api_instance.create_namespaced_pod(
            namespace="default",  # Specify the namespace
            body=pod_manifest     # Pod manifest
        )
        print(f"Pod '{pod_manifest['metadata']['name']}' created successfully.")
    except client.exceptions.ApiException as e:
        print(f"Exception when creating pod '{pod_manifest['metadata']['name']}': {e}")

def main():
    """Main function to create Pods."""
    # Load the Kubernetes configuration from default location
    config.load_kube_config()

    # Define Pod specifications
    pods = [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "nginx-1"},
            "spec": {
                "containers": [
                    {
                        "name": "container-1",
                        "image": "nginx",
                        "imagePullPolicy": "Always",
                        "resources": {
                            "limits": {
                                "cpu": "1.0m",
                                "memory": "256Mi"
                            }
                        }
                    }
                ]
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "terraform-pod"},
            "spec": {
                "containers": [
                    {
                        "name": "terraform-container",
                        "image": "hashicorp/terraform:latest",
                        "imagePullPolicy": "Always",
                        "resources": {
                            "limits": {
                                "cpu": "1.0m",
                                "memory": "256Mi"
                            }
                        },
                        "command": ["/bin/sleep", "infinity"]
                    }
                ]
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "centos-pod"},
            "spec": {
                "containers": [
                    {
                        "name": "centos-container",
                        "image": "centos:latest",
                        "imagePullPolicy": "Always",
                        "resources": {
                            "limits": {
                                "cpu": "1.0m",
                                "memory": "256Mi"
                            }
                        },
                        "command": ["/bin/sleep", "infinity"]
                   
