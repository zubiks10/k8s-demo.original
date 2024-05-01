
import subprocess

def run_kubectl_command(command):
    try:
        result = subprocess.run(['kubectl', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)  # Print error output for more details
        return None

def get_cluster_info():
    print("Cluster Info:")
    print(run_kubectl_command("cluster-info"))

def get_nodes_status():
    print("Nodes Status:")
    print(run_kubectl_command("get nodes"))

def get_pods_status():
    print("Pods Status:")
    print(run_kubectl_command("get pods --all-namespaces"))

def get_deployments_status():
    print("Deployments Status:")
    print(run_kubectl_command("get deployments --all-namespaces"))

def main():
    get_cluster_info()
    get_nodes_status()
    get_pods_status()
    get_deployments_status()

if __name__ == "__main__":
    main()
