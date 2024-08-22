from kubernetes import client, config

def create_pod(api_instance, pod_manifest):
    try:
        api_instance.create_namespaced_pod(
            namespace="default",
            body=pod_manifest
        )
        print(f"Pod '{pod_manifest['metadata']['name']}' created successfully.")
    except client.exceptions.ApiException as e:
        print(f"Exception when creating pod: {e}")

def main():
    # Load the Kubernetes configuration
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
                    }
                ]
            }
        }
    ]

    # Create a Kubernetes API client
    api_instance = client.CoreV1Api()

    # Create each pod
    for pod in pods:
        create_pod(api_instance, pod)

if __name__ == "__main__":
    main()
