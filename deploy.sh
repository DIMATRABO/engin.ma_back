#!/bin/bash
git pull 

# Build the Docker image
docker build --no-cache -t backend:latest .

# Bring down existing containers
docker compose down

# Start containers with the specified environment variables
docker compose up -d

# docker compose -f docker-compose.test.yml up -d --build

docker image prune