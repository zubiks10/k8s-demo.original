#!/bin/bash

# Function to run kubectl command
run_kubectl_command() {
    local command=$1
    result=$(kubectl $command 2>&1)
    if [ $? -eq 0 ]; then
        echo "$result" | sed 's/[[:space:]]*$//'
    else
        echo "Error executing command: $result" >&2
        return 1
    fi
}

# Function to get cluster info
get_cluster_info() {
    echo "Cluster Info:"
    run_kubectl_command "cluster-info"
}

# Function to get nodes status
get_nodes_status() {
    echo "Nodes Status:"
    run_kubectl_command "get nodes"
}

# Function to get pods status
get_pods_status() {
    echo "Pods Status:"
    run_kubectl_command "get pods --all-namespaces"
}

# Function to get deployments status
get_deployments_status() {
    echo "Deployments Status:"
    run_kubectl_command "get deployments --all-namespaces"
}

# Function to get persistent volumes (PVs) status
get_persistent_volumes_status() {
    echo "Persistent Volumes (PVs) Status:"
    run_kubectl_command "get pv"
}

# Function to get persistent volume claims (PVCs) status
get_persistent_volume_claims_status() {
    echo "Persistent Volume Claims (PVCs) Status:"
    run_kubectl_command "get pvc --all-namespaces"
}

# Function to get services status
get_services_status() {
    echo "Services Status:"
    run_kubectl_command "get services --all-namespaces"
}

# Function to get replica sets status
get_replica_sets_status() {
    echo "Replica Sets Status:"
    run_kubectl_command "get rs --all-namespaces"
}

# Function to get ingress classes status
get_ingress_classes_status() {
    echo "Ingress Classes Status:"
    run_kubectl_command "get ingressclasses --all-namespaces"
}

# Function to get ingresses status
get_ingresses_status() {
    echo "Ingresses Status:"
    run_kubectl_command "get ingresses --all-namespaces"
}

# Function to get config maps status
get_config_maps_status() {
    echo "Config Maps Status:"
    run_kubectl_command "get cm --all-namespaces"
}

# Function to get secrets status
get_secrets_status() {
    echo "Secrets Status:"
    run_kubectl_command "get secrets --all-namespaces"
}

# Function to get storage classes status
get_storage_classes_status() {
    echo "Storage Classes Status:"
    run_kubectl_command "get sc"
}

# Function to get namespaces status
get_namespaces_status() {
    echo "Namespaces Status:"
    run_kubectl_command "get ns"
}

# Function to get cluster roles status
get_cluster_roles_status() {
    echo "Cluster Roles Status:"
    run_kubectl_command "get clusterroles"
}

# Function to get cluster role bindings status
get_cluster_role_bindings_status() {
    echo "Cluster Role Bindings Status:"
    run_kubectl_command "get clusterrolebindings"
}

# Function to get roles status
get_roles_status() {
    echo "Roles Status:"
    run_kubectl_command "get roles --all-namespaces"
}

# Function to get service accounts status
get_service_accounts_status() {
    echo "Service Accounts Status:"
    run_kubectl_command "get serviceaccounts --all-namespaces"
}

# Function to get stateful sets status
get_stateful_sets_status() {
    echo "Stateful Sets Status:"
    run_kubectl_command "get statefulsets --all-namespaces"
}

# Function to get daemon sets status
get_daemon_sets_status() {
    echo "Daemon Sets Status:"
    run_kubectl_command "get daemonsets --all-namespaces"
}

# Function to get jobs status
get_jobs_status() {
    echo "Jobs Status:"
    run_kubectl_command "get jobs --all-namespaces"
}

# Main function
main() {
    get_cluster_info
    get_nodes_status
    get_pods_status
    get_deployments_status
    get_persistent_volumes_status
    get_persistent_volume_claims_status
    get_services_status
    get_replica_sets_status
    get_ingress_classes_status
    get_ingresses_status
    get_config_maps_status
    get_secrets_status
    get_storage_classes_status
    get_namespaces_status
    get_cluster_roles_status
    get_cluster_role_bindings_status
    get_roles_status
    get_service_accounts_status
    get_stateful_sets_status
    get_daemon_sets_status
    get_jobs_status
}

# Execute main function
main
