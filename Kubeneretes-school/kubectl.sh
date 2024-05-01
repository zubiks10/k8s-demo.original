set x-o

minikube start &
echo "complete"

kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo.yaml
kubectl apply -f webapp.yaml
kubectl get pods -A
kubectl apply jenkins-service.yaml
kubectl apply jenkins-nodeport.yaml
kubectl apply jenkins-deployment.yaml
kubectl apply multiple-pod.yaml

minikube kubectl -- get pods -A
echo "complete"
kubectl get nodes -o wide
echo "complete"
kubectl get svc -o wide
echo "complete"

#list all the services 

minikube service list


minikube dashboard &
minikube addons enable metrics-server
 
#kubectl get secret regcred --output=yaml
#Get a shell to the running container:
#kubectl exec --stdin --tty <pod_name> -- /bin/bash

for i in k8s-demo;do minikube dashboard &;done

echo complete;date