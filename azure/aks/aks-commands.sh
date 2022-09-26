#AKS GET CREDS
az aks get-credentials --resource-group rg-aks-southcentralus-001 --name aks-shared-southcentralus-001
#GET TOKEN FROM ACR
TOKEN=$(az acr login --name acrsharedsouthcentralus001.azurecr.io --expose-token --output tsv --query accessToken)
#LOGIN TO ACR
docker login acrsharedsouthcentralus001.azurecr.io --username 00000000-0000-0000-0000-000000000000 --password $TOKEN
#TAG THE CONTAINER IN DOCKER TO PUSH TO TO ACR
docker tag idw_api_psrb:0.1.0 acrsharedsouthcentralus001.azurecr.io/idw_api_psrb:0.1.0
#PUSH THE CONTAINER TO ACR
docker push acrsharedsouthcentralus001.azurecr.io/idw_api_psrb:0.1.0
#APPLY DEPLOYMENT FILE
kubectl apply -f deployment.yaml --namespace idw
#APPLY INGRESS FILE
kubectl apply -f ingress.yaml --namespace idw
#GET THE SERVICES RUNNING IN THE NAMESPACE
kubectl --namespace idw get services
#AUTOSCALE THE DEPLOYMENT
kubectl autoscale deployment {deploymentName} --cpu-percent=30 --min=1 --max=5


