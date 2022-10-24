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
- check linux enviroment variables `set`
- check specific linux variable `echo "$HOME"`
- set a enviroment variable `export POSTGRES_HOST=localhost`

### Course contents

<details><summary>Click to expand</summary>
<p>

**Section 1: Intro**

- [Intro](https://github.com/iteam1/social-app/tree/v1)

- [Project Overview](https://github.com/iteam1/social-app/tree/v1)

- [Mac Python Installation](https://github.com/iteam1/social-app/tree/v1)

**Section 2: Setup & installation**

- [Mac VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Windows Python Installation](https://github.com/iteam1/social-app/tree/v1)

- [Windows VS Code install and setup](https://github.com/iteam1/social-app/tree/v1)

- [Python virtual Env Basics](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on windows](https://github.com/iteam1/social-app/tree/v1)

- [Virtual Env on Mac](https://github.com/iteam1/social-app/tree/v1)

**Section 3: FastAPI**

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

**Section 4: Databases**

- [Database Intro](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Windows Install](https://github.com/iteam1/social-app/tree/v6)

- [Postgres Mac Install](https://github.com/iteam1/social-app/tree/v6)

- [Database Schema & Tables](https://github.com/iteam1/social-app/tree/v6)

- [Managing Postgres with PgAdmin GUI](https://github.com/iteam1/social-app/tree/v6)

- [Your first SQL Query](https://github.com/iteam1/social-app/tree/v6)

- [Filter results with "where"](https://github.com/iteam1/social-app/tree/v6)

- [SQL Operators](https://github.com/iteam1/social-app/tree/v6)

- [IN](https://github.com/iteam1/social-app/tree/v6)

- [Pattern matching with LIKE](https://github.com/iteam1/social-app/tree/v6)

- [Ordering Results](https://github.com/iteam1/social-app/tree/v6)

- [LIMIT & OFFSET](https://github.com/iteam1/social-app/tree/v6)

- [Modifying Data](https://github.com/iteam1/social-app/tree/v6)

**Section 5: Python + Raw SQL**

- [Setup App Database](https://github.com/iteam1/social-app/tree/v7)

- [Connecting to database w/ Python](https://github.com/iteam1/social-app/tree/v7)

- [Database CRUD](https://github.com/iteam1/social-app/tree/v7)

**Section 6: ORMs**

- [ORM intro](https://github.com/iteam1/social-app/tree/v8)

- [SQLALCHEMY setup](https://github.com/iteam1/social-app/tree/v8)

- [Adding CreatedAt Column](https://github.com/iteam1/social-app/tree/v8)

- [Get All](https://github.com/iteam1/social-app/tree/v8)

- [Create](https://github.com/iteam1/social-app/tree/v8)

- [Get by ID](https://github.com/iteam1/social-app/tree/v8)

- [Delete](https://github.com/iteam1/social-app/tree/v8)

- [Update](https://github.com/iteam1/social-app/tree/v8)

**Section 7: Pydantic Models**

- [Pydantic vs ORM Models](https://github.com/iteam1/social-app/tree/v9)

- [Pydantic Models Deep Dive](https://github.com/iteam1/social-app/tree/v9)

- [Response Model](https://github.com/iteam1/social-app/tree/v9)

**Section 8: Authentication & Users**

- [Creating Users Table](https://github.com/iteam1/social-app/tree/v9)

- [User Registration Path Operation](https://github.com/iteam1/social-app/tree/v9)

- [Hashing Passwords](https://github.com/iteam1/social-app/tree/v9)

- [Refractor Hashing Logic](https://github.com/iteam1/social-app/tree/v9)

- [Get User by ID](https://github.com/iteam1/social-app/tree/v9)

- [FastAPI Routers](https://github.com/iteam1/social-app/tree/v10)

- [Router Prefix](https://github.com/iteam1/social-app/tree/v11)

- [Router Tags](https://github.com/iteam1/social-app/tree/v11)

- [JWT Token Basics](https://github.com/iteam1/social-app/tree/v12)

- [Login Process](https://github.com/iteam1/social-app/tree/v12)

- [Creating Token](https://github.com/iteam1/social-app/tree/v12)

- [OAuth2 PasswordRequestForm](https://github.com/iteam1/social-app/tree/v13)

- [Verify user is Logged In](https://github.com/iteam1/social-app/tree/v13)

- [Fixing Bugs](https://github.com/iteam1/social-app/tree/v13)

- [Protecting Routes](https://github.com/iteam1/social-app/tree/v13)

- [Test Expired Token](https://github.com/iteam1/social-app/tree/v13)

- [Fetching User in Protected Routes](https://github.com/iteam1/social-app/tree/v13)

- [Postman advanced Features](https://github.com/iteam1/social-app/tree/v13)

**Section 9: Relationships**

- [SQL Relationship Basics](https://github.com/iteam1/social-app/tree/v14)

- [Postgres Foreign Keys](https://github.com/iteam1/social-app/tree/v14)

- [SQLAlchemy Foreign Keys](https://github.com/iteam1/social-app/tree/v14)

- [Update Schema to include User](https://github.com/iteam1/social-app/tree/v14)

- [Assigning Owner id when creating new](https://github.com/iteam1/social-app/tree/v14)

- [Delete and Update only your own](https://github.com/iteam1/social-app/tree/v14)

- [Only Retrieving Logged in User's](https://github.com/iteam1/social-app/tree/v14)

- [Sqlalchemy Relationships](https://github.com/iteam1/social-app/tree/v14)

- [Query Parameters](https://github.com/iteam1/social-app/tree/v14)

- [Cleanup our main.py file](https://github.com/iteam1/social-app/tree/v14)

- [Env Variables](https://github.com/iteam1/social-app/tree/v15)

**Section 10: Vote/Like System**

- [Vote/Like Theory](https://github.com/iteam1/social-app/tree/v15)

- [Votes Table](https://github.com/iteam1/social-app/tree/v15)

- [Votes Sqlalchemy](https://github.com/iteam1/social-app/tree/v15)

- [Votes Route](https://github.com/iteam1/social-app/tree/v15)

- [SQL Joins](https://github.com/iteam1/social-app/tree/v15)

- [Joins in SqlAlchemy](https://github.com/iteam1/social-app/tree/v15)

- [Get One with Joins](https://github.com/iteam1/social-app/tree/v15)

**Section 11: Database Migration w/ Alembic**

- What is a database migration tool

- Alembic Setup

- Disable SqlAlchemy create Engine

**Section 12: Pre Deployment Checklist**

- What is CORS?

- Git PreReqs

- Git Install

- Github

**Section 13: Deployment Heroku**

- Heroku intro

- Create Heroku App

- Heroku procfile

- Adding a Postgres database

- Env Variables in Heroku

- Alembic migrations on Heroku Postgres instance

- Pushing changed to production

**Section 14: Deployment Ubuntu**

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

**Section 15: Docker**

- Dockerfile

- Docker Compose

- Postgres Container

- Bind Mounts

- Dockerhub

- Production vs Development

**Section 16: Testing**

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

**Section 17: CI/CD pipeline**

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

### References

[Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA)

[fastapi-course](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)

[FastAPI official document](https://fastapi.tiangolo.com/tutorial/)

[HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

[download Postman](https://www.postman.com/downloads/)

[pydantic](https://pydantic-docs.helpmanual.io/)

[HTTP Status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

[PostgreSQL Tutorial](https://www.postgresqltutorial.com/)

[ubuntu-install-postgresql-and-pgadmin](https://codingpub.dev/ubuntu-install-postgresql-and-pgadmin/)

[Ubuntu: Install PostgreSQL and pgAdmin](https://www.pgadmin.org/download/pgadmin-4-apt/)

[Postgres Datatype](https://www.postgresql.org/docs/current/datatype.html)

[PostgreSQL Python driver](https://www.psycopg.org/docs/)

[Sqlalchemy](https://www.sqlalchemy.org/)

[Python Typing - Type Hints & Annotations](https://www.youtube.com/watch?v=QORvB-_mbZ0)

[Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

[JSON Web Token Builder](http://jwtbuilder.jamiekurtz.com/)

[Online JWT Generator](https://www.javainuse.com/jwtgenerator)

[OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

[Decode token online tool](http://calebb.net/)