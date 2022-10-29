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

- install text vim-editor `sudo apt install vim` or nano-editor `sudo apt install nano`

##Install Python

- check python version `python3 --version`

- install python3 `sudo apt-get install python3`

- check pip3 version `pip3 --version`

- install pip version `sudo apt install python3-pip`

- check pip3 list `pip3 list`

- install  virtualenv package by pip `sudo pip3 install virtualenv`

## Run postgresql container

- create postgresql container map internal port 5432 to external port 5431: `sudo docker run --name pgsql-dev -e POSTGRES_PASSWORD=pass123 -p 5431:5432 postgres`

- This command will start an interactive terminal inside the container. Next, you can start the PostgreSQL by running the following command on the same terminal. `docker exec -it pgsql-dev bash`

- start the postgres-container `sudo docker start 8121bd993540`

- you can access postgres docker-container with  address `172.0.0.1` port `5431`

## Install Postgres & setup password On virtual machine

- check your user role `whoami`

- install postgres `-y` (yes option as default) `sudo apt install postgresql-15.0 postgresql-contrib-15.0 -y`

- remove postgres `sudo apt-get remove --purge postgres*`

- access postgres on your machine and get help `psql --help` ,check version `psql --version`

- check the list of all user on your machine `sudo cat /etc/passwd`

- change the name of user `su - postgres`

- login to the database `postgres` exit your role and go back to root role `exit`

- go to default database `psql -U -postgres -d postgres`

##Postgres Config

- to to postgres installation floder `cd /etc/postgresql`

- go to main `cd /etc/postgresql/14/main`

		conf.d	     pg_ctl.conf  pg_ident.conf    start.conf
		environment  pg_hba.conf  postgresql.conf

- edit `postgresql.conf`: `vi postgresql.conf`

		#------------------------------------------------------------------------------
		# CONNECTIONS AND AUTHENTICATION
		#------------------------------------------------------------------------------
		# - Connection Settings -
		#listen_addresses = 'localhost'         # what IP address(es) to listen on;
		                                        # comma-separated list of addresses;
		                                        # defaults to 'localhost'; use '*' for all

edit the `listen_addresses` to access remotely

		#------------------------------------------------------------------------------
		# CONNECTIONS AND AUTHENTICATION
		#------------------------------------------------------------------------------
		# - Connection Settings -
		listen_addresses = '*' # your ip addresses , * allow access from any where
		#listen_addresses = 'localhost'         # what IP address(es) to listen on;
		                                        # comma-separated list of addresses;
		                                        # defaults to 'localhost'; use '*' for all

- edit `pg_hba.conf`

		# Database administrative login by Unix domain socket
		local   all             postgres                                peer
		# TYPE  DATABASE        USER            ADDRESS                 METHOD
		# "local" is for Unix domain socket connections only
		local   all             all                                     peer
		# IPv4 local connections:
		host    all             all             127.0.0.1/32            scram-sha-256
		# IPv6 local connections:
		host    all             all             ::1/128                 scram-sha-256

to 

		# Database administrative login by Unix domain socket
		local   all             postgres                                md5
		# TYPE  DATABASE        USER            ADDRESS                 METHOD
		# "local" is for Unix domain socket connections only
		local   all             all                                     md5
		# IPv4 local connections:
		host    all             all             0.0.0.0/0            	md5
		# IPv6 local connections:
		host    all             all             ::/0                 	md5
 
- restart to save change `systemctl restart postgresql`

## Create new user and setup python environment

## Environment Variables

## Alembic migrations on production database 12:42:24

## Gunicorn

## Creating a Systemd service

NGINX

Setting up Domain name

SSL/HTTPS

##NGINX enable

##Firewall

##Pushing code changes to Production