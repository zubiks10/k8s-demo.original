#!/bin/bash

# Function to check the status of a Kubernetes service
check_service_status() {
    service_name="$1"
    namespace="$2"

    # Check if namespace is provided, if not, use default
    if [ -z "$namespace" ]; then
        namespace="default"
    fi

    # Run kubectl command to get service status
    service_status=$(kubectl get svc "$service_name" -n "$namespace" --no-headers=true 2>/dev/null)

    # Check if the service status is empty (indicating service not found)
    if [ -z "$service_status" ]; then
        echo "Service '$service_name' not found in namespace '$namespace'"
    else
        # Extract service status from the kubectl output
        service_status=$(echo "$service_status" | awk '{print $4}')

        # Print service status
        echo "Service '$service_name' in namespace '$namespace' is: $service_status"
    fi
}

# Example usage:
check_service_status "my-service" "my-namespace"
check_service_status "another-service" "another-namespace"
