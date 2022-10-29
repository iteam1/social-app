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

- jump out the container termial `exit`

## Update packages

- update packages `sudo apt update`

- update and upgrade `sudo apt update && upgrade -y`

- install text editor vim `sudo apt install vim`

##Install Python

- check python version `python3 --version`

- install python3 `sudo apt-get install python3`

- check pip3 version `pip3 --version`

- install pip version `sudo apt install python3-pip`

- check pip3 list `pip3 list`

- install  virtualenv package by pip `sudo pip3 install virtualenv`

##Install Postgres & setup password

- check your user role `whoami`

- install postgres `-y` (yes option as default) `sudo apt install postgresql postgresql-contrib -y`

- access postgres on your machine and get help `psql --help` ,check version `psql --version`

- check the list of all user on your machine `sudo cat /etc/passwd`

- change the name of user `su - postgres`

- login to the database `postgres` exit your role and go back to root role `exit`

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