1. docker build -t flasknginx:v1 .
2. cd kubernetsServices
3. kubectl apply -f deployment.yml

Activity 1
- kubectl apply -f simpleService.yml
   -  kubectl apply -f kuber.yml 
   -  kubectl get services   -  
   -  kubectl port-forward svc/flasknginx-service 8085:8085
   -   Open Browser And Check
   -  kubectl delete service flasknginx-service

Activity 2
- kubectl apply -f nodePortService.yml
   - kubectl cluster-info
   - kubectl get node -o wide
   - ----FOR IBM---
   - ibmcloud ks worker ls --cluster clustername If ur using IBM cloud
   - http://FirstPublicAddressAbove:30036/

   - kubectl delete service flasknginx-nodePortService

Activity 3
- kubectl apply -f loadbalancer.yml
   -   kubectl get service 
   -   BROWSER : url:port