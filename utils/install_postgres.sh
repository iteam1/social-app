#!usr/bin/bash

# refresh your server's local package index
sudo apt update

# install the Postgres package along with a -contrib package that adds some additional utilities and functionality
sudo apt install postgresql postgresql-contrib

# ensure that the service is started
sudo systemctl start postgresql.service