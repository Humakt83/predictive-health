docker stop my-mongo
docker container rm my-mongo

docker run --name my-mongo -d -p 27017-27019:27017-27019 mongo:4.0-xenial
