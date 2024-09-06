## Simple python docker dev example for the official docker docs
https://docs.docker.com/language/python/containerize/


### containerize and run your Python application using Docker.

## resolving the ssl error(if)
`git cofig --global http.sslBackend schannel`

## cloning the github demo repo of fast-api
`git clone https://github.com/estebanx64/python-docker-example`
## initializing the docker setup
`docker init`

************ TO START THE DOCKER AND RUN ON LOCALHOST *******************************
## go to the current working directory
`cd "current_directory"`
## running the docker file 
`docker compose up --build`
## running docker file in detached mode
`docker compose up --build -d`
## stopping the application from terminal
`docker compose down`


## Deploying the files to docker hub.

https://docs.docker.com/language/python/configure-ci-cd/#step-three-run-the-workflow