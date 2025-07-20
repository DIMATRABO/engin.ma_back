#!/bin/bash
git pull 

# Build the Docker image
docker build --no-cache -t backend:latest .

# Bring down existing containers
docker compose down

# Start containers with the specified environment variables
docker compose up -d

docker image prune