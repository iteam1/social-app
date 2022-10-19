#!usr/bin/bash

# refresh your server's local package index
sudo apt update

# install the Postgres package along with a -contrib package that adds some additional utilities and functionality
sudo apt install postgresql postgresql-contrib

# ensure that the service is started
sudo systemctl start postgresql.service

# By default, Postgres uses a concept called “roles” to handle authentication and authorization.
# These are, in some ways, similar to regular Unix-style users and groups.
# Upon installation, Postgres is set up to use ident authentication, 
# meaning that it associates Postgres roles with a matching Unix/Linux system account.
# If a role exists within Postgres, a Unix/Linux username with the same name is able to sign in as that role.
# The installation procedure created a user account called postgres that is associated with the default Postgres role.
# There are a few ways to utilize this account to access Postgres.
# One way is to switch over to the postgres account on your server by running the following command: