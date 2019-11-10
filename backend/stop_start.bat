docker stop mycontainer
docker container rm mycontainer
docker build -t myimage .
docker run -d --link my-mongo:mongodb --name mycontainer -p 5000:80 myimage 