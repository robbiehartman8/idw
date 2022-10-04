################ PERSONAL ################
#login to acr
az acr login --name idw234092380480

#tag images
docker tag example_api-example_api idw234092380480.azurecr.io/apis/example
docker tag hr_data_api-hrdata idw234092380480.azurecr.io/apis/hrdata
docker tag worker_api-worker idw234092380480.azurecr.io/apis/worker

#push docker images
docker push idw234092380480.azurecr.io/apis/example
docker push idw234092380480.azurecr.io/apis/hrdata
docker push idw234092380480.azurecr.io/apis/worker
################ PERSONAL ################


################ EY ################
#login to acr
TOKEN=$(az acr login --name usedadvcrdacr05 --expose-token --output tsv --query accessToken)
docker login usedadvcrdacr05.azurecr.io --username 00000000-0000-0000-0000-000000000000 --password $TOKEN

#tag images
docker tag example_api-example_api usedadvcrdacr05.azurecr.io/apis/example
docker tag hr_data_api-hrdata usedadvcrdacr05.azurecr.io/apis/hrdata
docker tag worker_api-worker usedadvcrdacr05.azurecr.io/apis/worker

#push docker images
docker push usedadvcrdacr05.azurecr.io/apis/example
docker push usedadvcrdacr05.azurecr.io/apis/hrdata
docker push usedadvcrdacr05.azurecr.io/apis/worker
################ EY ################