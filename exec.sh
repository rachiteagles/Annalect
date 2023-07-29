# build docker image
docker build -t pokemon_image .

# run docker container and give it a name "pokemon"
docker run --name pokemon pokemon_image

# copy the result.txt from inside the container to the current directory on the host
docker cp pokemon:/home/jovyan/work/result.txt .

# remove the container named "pokemon"
docker rm -f pokemon