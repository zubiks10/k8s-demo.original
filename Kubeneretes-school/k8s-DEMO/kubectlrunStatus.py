import subprocess

def run_kubectl_command(command):
    try:
        result = subprocess.run(['kubectl'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
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

def get_persistent_volumes_status():
    print("Persistent Volumes (PVs) Status:")
    print(run_kubectl_command("get pv"))

def get_persistent_volume_claims_status():
    print("Persistent Volume Claims (PVCs) Status:")
    print(run_kubectl_command("get pvc --all-namespaces"))

def get_services_status():
    print("Services Status:")
    print(run_kubectl_command("get services --all-namespaces"))

def get_replica_sets_status():
    print("Replica Sets Status:")
    print(run_kubectl_command("get rs --all-namespaces"))

def get_ingress_classes_status():
    print("Ingress Classes Status:")
    print(run_kubectl_command("get ingressclasses --all-namespaces"))

def get_ingresses_status():
    print("Ingresses Status:")
    print(run_kubectl_command("get ingresses --all-namespaces"))

def get_config_maps_status():
    print("Config Maps Status:")
    print(run_kubectl_command("get cm --all-namespaces"))

def get_secrets_status():
    print("Secrets Status:")
    print(run_kubectl_command("get secrets --all-namespaces"))

def get_storage_classes_status():
    print("Storage Classes Status:")
    print(run_kubectl_command("get sc"))

def get_namespaces_status():
    print("Namespaces Status:")
    print(run_kubectl_command("get ns"))

def get_cluster_roles_status():
    print("Cluster Roles Status:")
    print(run_kubectl_command("get clusterroles"))

def get_cluster_role_bindings_status():
    print("Cluster Role Bindings Status:")
    print(run_kubectl_command("get clusterrolebindings"))

def get_roles_status():
    print("Roles Status:")
    print(run_kubectl_command("get roles --all-namespaces"))

def get_service_accounts_status():
    print("Service Accounts Status:")
    print(run_kubectl_command("get serviceaccounts --all-namespaces"))

def get_stateful_sets_status():
    print("Stateful Sets Status:")
    print(run_kubectl_command("get statefulsets --all-namespaces"))

def get_daemon_sets_status():
    print("Daemon Sets Status:")
    print(run_kubectl_command("get daemonsets --all-namespaces"))

def get_jobs_status():
    print("Jobs Status:")
    print(run_kubectl_command("get jobs --all-namespaces"))

def get_replication_controllers_status():
    print("Replication Controllers Status:")
    print(run_kubectl_command("get rc --all-namespaces"))

def get_network_policies():
    print("Network Policies:")
    print(run_kubectl_command("get networkpolicies --all-namespaces"))

def main():
    get_cluster_info()
    get_nodes_status()
    get_pods_status()
    get_deployments_status()
    get_persistent_volumes_status()
    get_persistent_volume_claims_status()
    get_services_status()
    get_replica_sets_status()
    get_ingress_classes_status()
    get_ingresses_status()
    get_config_maps_status()
    get_secrets_status()
    get_storage_classes_status()
    get_namespaces_status()
    get_cluster_roles_status()
    get_cluster_role_bindings_status()
    get_roles_status()
    get_service_accounts_status()
    get_stateful_sets_status()
    get_daemon_sets_status()
    get_jobs_status()
    get_replication_controllers_status()
    get_network_policies()

if __name__ == "__main__":
    main()
