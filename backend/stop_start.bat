docker stop mycontainer
docker container rm mycontainer
docker build -t myimage .
docker run -d --name mycontainer -p 5000:80 myimage 