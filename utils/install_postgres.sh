#!usr/bin/bash

# refresh your server's local package index
sudo apt update

# install the Postgres package along with a -contrib package that adds some additional utilities and functionality
sudo apt install postgresql postgresql-contrib

sudo systemctl start postgresql.service

# ensure that the service is started
sudo systemctl is-active postgresql

sudo systemctl is-enabled postgresql

sudo systemctl status postgresql

sudo pg_isready