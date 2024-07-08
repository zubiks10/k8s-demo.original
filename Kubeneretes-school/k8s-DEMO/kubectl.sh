#!/bin/bash
set -x
# Start Minikube in the background
minikube start &

# Wait for Minikube cluster to be ready
wait $(minikube status | grep -q "Running")

# Echo message indicating completion
echo "Minikube cluster is ready."

# Apply YAML configurations for MongoDB
kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo.yaml

# Apply YAML configuration for web app
kubectl apply -f webapp.yaml

# Get pods in all namespaces
kubectl get pods -A

# Apply YAML configurations for Jenkins
kubectl apply -f jenkins-service.yaml
kubectl apply -f jenkins-nodeport.yaml
kubectl apply -f jenkins-deployment.yaml

# Apply YAML configuration for multiple pods
kubectl apply -f multiple-pod.yaml

# Get pods in all namespaces using Minikube's Kubernetes
minikube kubectl -- get pods -A

# Get ingress-classes & ingress 
kubectl apply -f ingress-class.yaml
kubectl apply -f ingress.yaml
kubectl apply -f virtualmachine-crd.yaml
kubectl apply -f CRD.yaml

# Echo message indicating completion
echo "complete"

# Get nodes with wide output
kubectl get nodes -o wide

# Echo message indicating completion
echo "complete"

# Get services with wide output
kubectl get svc -o wide

# Echo message indicating completion
echo "complete"

# List all services exposed on Minikube
minikube service list

# Open Minikube dashboard in the background
minikube dashboard &

# Enable Metrics Server addon for Minikube
minikube addons enable metrics-server

# Start Minikube with RBAC enabled using extra configuration
# minikube start --extra-config=apiserver.authorization-mode=RBAC

# Echo completion message with date
echo "complete"; date

# Commands below are commented out
# kubectl get secret regcred --output=yaml
# kubectl exec --stdin --tty <pod_name> -- /bin/bash
