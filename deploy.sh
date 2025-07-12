#!/bin/bash

# Determine the environment based on the Git branch
if [[ "$(git rev-parse --abbrev-ref HEAD)" == "prod" ]]; then


    # Pull the latest changes from the current branch in the Git repository
    git pull origin "$(git rev-parse --abbrev-ref HEAD)"

    # Build the Docker image
    docker build -t backend:prod .

    # Bring down existing containers
    docker-compose down

    # Start containers with the specified environment variables
    docker-compose up -d


else

    # Pull the latest changes from the current branch in the Git repository
    git pull origin "$(git rev-parse --abbrev-ref HEAD)"

    # Build the Docker image
    docker build -t backend:test .

    # Bring down existing containers
    docker-compose down

    # Start containers with the specified environment variables
    docker-compose up -d

fi

