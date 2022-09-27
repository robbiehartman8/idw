
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