import subprocess
import time

def run_command(command, wait=False, capture_output=False):
    """Run a shell command."""
    result = subprocess.run(command, shell=True, check=True, capture_output=capture_output, text=True)
    if wait:
        time.sleep(5)  # Pause to wait for processes to be ready
    return result

def kubectl_apply_with_retry(file, retries=5, delay=5):
    """Try to apply a YAML configuration file with retries."""
    for i in range(retries):
        try:
            run_command(f"kubectl apply --validate=false -f {file}")
            break  # If successful, exit the loop
        except subprocess.CalledProcessError as e:
            if i < retries - 1:
                print(f"Retrying to apply {file} ({i+1}/{retries}) after {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed to apply {file} after {retries} attempts.")
                raise e

def main():
    # Start Minikube in the background
    subprocess.Popen("minikube start", shell=True)

    # Wait for Minikube cluster to be ready
    while True:
        status = subprocess.run("minikube status | grep -q 'Running'", shell=True)
        if status.returncode == 0:
            break
        time.sleep(5)

    # Echo message indicating completion
    print("Minikube cluster is ready.")

    # Apply YAML configurations for MongoDB
    kubectl_apply_with_retry("mongo-config.yaml")
    kubectl_apply_with_retry("mongo-secret.yaml")
    kubectl_apply_with_retry("mongo.yaml")

    # Apply YAML configuration for web app
    kubectl_apply_with_retry("webapp.yaml")

    # Get pods in all namespaces
    run_command("kubectl get pods -A")

    # Apply YAML configurations for Jenkins
    kubectl_apply_with_retry("jenkins-service.yaml")
    kubectl_apply_with_retry("jenkins-nodeport.yaml")
    kubectl_apply_with_retry("jenkins-deployment.yaml")

    # Apply YAML configuration for multiple pods
    kubectl_apply_with_retry("multiple-pod.yaml")

    # Get pods in all namespaces using Minikube's Kubernetes
    run_command("minikube kubectl -- get pods -A")

    # Get ingress-classes & ingress
    kubectl_apply_with_retry("ingress-class.yaml")
    kubectl_apply_with_retry("ingress.yaml")
    kubectl_apply_with_retry("virtualmachine-crd.yaml")
    kubectl_apply_with_retry("CRD.yaml")

    # Echo message indicating completion
    print("complete")

    # Get nodes with wide output
    run_command("kubectl get nodes -o wide")

    # Echo message indicating completion
    print("complete")

    # Get services with wide output
    run_command("kubectl get svc -o wide")

    # Echo message indicating completion
    print("complete")

    # List all services exposed on Minikube
    run_command("minikube service list")

    # Open Minikube dashboard in the background
    subprocess.Popen("minikube dashboard", shell=True)

    # Enable Metrics Server addon for Minikube
    run_command("minikube addons enable metrics-server")

    # Echo completion message with date
    run_command("echo complete; date", capture_output=True)

if __name__ == "__main__":
    main()
