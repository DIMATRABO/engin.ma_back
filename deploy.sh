#!/bin/bash
git pull 

# Build the Docker image
docker build -t backend:prod .

# Bring down existing containers
docker-compose down

# Start containers with the specified environment variables
docker-compose up -d

docker rmi -f `docker images -qa `