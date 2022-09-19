
#login to acr
az acr login --name idw234092380480

#tag images
docker tag hr_data-hrdata idw234092380480.azurecr.io/hrdata/hrdata

#push docker images
docker push idw234092380480.azurecr.io/hrdata/hrdata