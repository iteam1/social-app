# social-app
FastAPI framework

### Guides

*Note: Run the command on your terminal*

- create virtual enviroment `virtualenv env`
- activate virtual enviroment `source env/bin/activate`
- deactivate virtual enviroment `deactivate`
- export packages in virtual enviroment `pip3 freeze > requirements.txt`
- install packages as requirements: `pip3 install -r requirements.txt`
- install FastAPI full (all flag) `pip3 install fastapi[all]`
- run app (app instance from main) `uvicorn app.main:app`
- view api-doc `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`
- reload web app automaticly if changing happen `uvicon app.main:app --reload`
- switch over to the postgres account on your server `sudo -i -u postgres`
- then you can access the postgres prompt by running `psql`
- to exit postgresql prompt `\q`
- to go back the linux command prompt `exit`

		
- access pdadmin4 local-server `http://127.0.0.1/pgadmin4`

### Course contents

<details><summary>Click to expand</summary>
<p>

- [Intro](https://github.com/iteam1/social-app/tree/v1)

- [Project Overview](https://github.com/iteam1/social-app/tree/v1)

- [Mac Python Installation](https://github.com/iteam1/social-app/tree/v1)

- [Mac VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Windows Python Installation](https://github.com/iteam1/social-app/tree/v1)

- [Windows VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Python virtual Env Basics](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on windows](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on Mac](https://github.com/iteam1/social-app/tree/v1)

- [Install dependencies w/ pip](https://github.com/iteam1/social-app/tree/v1)

- [Starting FastAPI](https://github.com/iteam1/social-app/tree/v1)

- [Path Operations](https://github.com/iteam1/social-app/tree/v2)

- [Intro Postman](https://github.com/iteam1/social-app/tree/v2)

- [HTTP Requests](https://github.com/iteam1/social-app/tree/v2)

- [Schema Validation with Pydantic](https://github.com/iteam1/social-app/tree/v3)

- [CRUD Operations](https://github.com/iteam1/social-app/tree/v4)

- [Storing in Array](https://github.com/iteam1/social-app/tree/v4)

- [Creating](https://github.com/iteam1/social-app/tree/v4)

- [Postman Collections & saving requests](https://github.com/iteam1/social-app/tree/v4)

- [Retrieve One](https://github.com/iteam1/social-app/tree/v4)

- [Path order Matters](https://github.com/iteam1/social-app/tree/v4)

- [Changing response Status Codes](https://github.com/iteam1/social-app/tree/v5)

- [Deleting](https://github.com/iteam1/social-app/tree/v5)

- [Updating](https://github.com/iteam1/social-app/tree/v5)

- [Automatic Documentation](https://github.com/iteam1/social-app/tree/v5)

- [Python packages](https://github.com/iteam1/social-app/tree/v6)

- [Database Intro](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Windows Install](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Mac Install](https://github.com/iteam1/social-app/tree/v6)

- [Database Schema & Tables](https://github.com/iteam1/social-app/tree/v6)

- [Managing Postgres with PgAdmin GUI](https://github.com/iteam1/social-app/tree/v6)

- [Your first SQL Query](https://github.com/iteam1/social-app/tree/v6)

- Filter results with "where"

- SQL Operators

- IN

- Pattern matching with LIKE

- Ordering Results

- LIMIT & OFFSET

- Modifying Data

- Setup App Database

- Connecting to database w/ Python

- Database CRUD

- ORM intro

- SQLALCHEMY setup

- Adding CreatedAt Column

- Get All

- Create

- Get by ID

- Delete

- Update

- Pydantic vs ORM Models

- Pydantic Models Deep Dive

- Response Model

- Creating Users Table

- User Registration Path Operation

- Hashing Passwords

- Refractor Hashing Logic

- Get User by ID

- FastAPI Routers

- Router Prefix

- Router Tags

- JWT Token Basics

- Login Process  

- Creating Token

- OAuth2 PasswordRequestForm

- Verify user is Logged In

- Fixing Bugs

- Protecting Routes

- Test Expired Token

- Fetching User in Protected Routes

- Postman advanced Features

- SQL Relationship Basics

- Postgres Foreign Keys

- SQLAlchemy Foreign Keys

- Update Schema to include User

- Assigning Owner id when creating new

- Delete and Update only your own

- Only Retrieving Logged in User's

- Sqlalchemy Relationships

- Query Parameters

- Cleanup our main.py file

- Env Variables

- Vote/Like Theory

- Votes Table

- Votes Sqlalchemy

- Votes Route

- SQL Joins

- Joins in SqlAlchemy

- Get One with Joins

- What is a database migration tool

- Alembic Setup

- Disable SqlAlchemy create Engine

- What is CORS?

- Git PreReqs

- Git Install

- Github

- Heroku intro

- Create Heroku App

- Heroku procfile

- Adding a Postgres database

- Env Variables in Heroku

- Alembic migrations on Heroku Postgres instance

- Pushing changed to production

- Create an Ubuntu VM

- Update packages

- Install Python

- Install Postgres & setup password

- Postgres Config

- Create new user and setup python evironment

- Env Variables

- Alembic migrations on production database

- Gunicorn

- Creating a Systemd service

- NGINX

- Setting up Domain name

- SSL/HTTPS

- NGINX enable

- Firewall

- Pushing code changes to Production

- Dockerfile

- Docker Compose

- Postgres Container

- Bind Mounts

- Dockerhub

- Production vs Development

- Testing Intro

- Writing your first test

- The -s & -v flags

- Testing more functions

- Parametrize

- Testing Classes

- Fixtures

- Combining Fixtures + Parametrize

- Testing Exceptions

- FastAPI TestClient

- Pytest flags

- Test create user

- Setup testing database

- Create & destroy database after each test

- More Fixtures to handle database interaction

- Trailing slashes in path

- Fixture scope

- Test user fixture

- Test/validate token

- Conftest.py

- Testing

- CI/CD intro

- Github Actions

- Creating Jobs

- setup python/dependencies/pytest

- Env variables

- Github Secrets

- Testing database

- Building Docker images

- Deploy to heroku

- Failing tests in pipeline

- Deploy to Ubuntu

</p>
</details>

### references

[Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA)

[fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)

[FastAPI official document](https://fastapi.tiangolo.com/tutorial/)

[HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

[download Postman](https://www.postman.com/downloads/)

[pydantic](https://pydantic-docs.helpmanual.io/)

[HTTP Status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[ubuntu-install-postgresql-and-pgadmin](https://codingpub.dev/ubuntu-install-postgresql-and-pgadmin/)

[Ubuntu: Install PostgreSQL and pgAdmin](https://www.pgadmin.org/download/pgadmin-4-apt/)