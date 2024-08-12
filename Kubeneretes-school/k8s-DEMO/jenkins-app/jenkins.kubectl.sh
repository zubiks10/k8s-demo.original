kubectl create -f jenkins-deployment-service.yaml
kubectl create -f jenkins-deployment.yaml
kubectl create -f jenkins-ingress.yaml
kubectl create -f jenkins-nodeport.yaml
kubectl create  -f jenkins-pv-pvc.yaml
kubectl create -f jenkins-pvc.yaml
kubectl create -f jenkins-service.yaml
kubectl create -f jenkinsDeploy.yaml