kubectl apply -f deployment.yaml --namespace ingress-basic

az aks get-credentials --resource-group USEDADVCRDRSG14 --name USEDADVCRDAKS01

kubectl apply -f deployment.yaml --namespace ingress-basic

kubectl apply -f ingress.yaml --namespace ingress-basic

kubectl apply -f ingress.yaml --namespace ingress-basic

kubectl --namespace ingress-basic get services

kubectl autoscale deployment {deploymentName} --cpu-percent=30 --min=1 --max=5

kubectl delete namespace ingress-basic


