## Create Linux virtual machine 

### Create virtual machine by virtualbox

- download and install [VirtualBox](https://phoenixnap.com/kb/install-virtualbox-on-ubuntu)

- download [ubuntu release](https://releases.ubuntu.com/)


### Run by docker Ubuntu image

- list all container is running `docker rm -f $(docker ps -a -q)`

- pull ubuntu image: `docker pull ubuntu`

- run docker imgae interactive mode `sudo docker run -t [your image name]`

- start the container `sudo docker container start [container id]`

- stop the container `docker stop [container_id or name]`

- delete all container `docker rm -f [container_id or name]`

- open terminal inside container `docker exec -it [container id] /bin/sh`

## Update packages

- update packages `sudo apt update`

##Install Python

##Install Postgres & setup password

##Postgres Config

##Create new user and setup python environment

##Environment Variables

##Alembic migrations on production database 12:42:24

##Gunicorn

##Creating a Systemd service

##NGINX

##Setting up Domain name

##SSL/HTTPS

##NGINX enable

##Firewall

##Pushing code changes to Production