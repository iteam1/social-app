import pytest

from fastapi.testclient import TestClient
from app.main import app
from app import schemas

from app.config import settings
from app import models
from app.database import get_db,Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from alembic import command

# create database test uri
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

'''
# create all tables, but create database hadnly first
#Base.metadata.create_all(bind = engine)

# session for connecting to database
TestingSessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) 

def override_get_db():

	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()

app.dependency_overrides[get_db] = override_get_db # override everthing get_db from app by override_get_db

# client = TestClient(app)
'''

# session for connecting to database
TestingSessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) 

@pytest.fixture
def session():
	Base.metadata.drop_all(bind = engine) # clear everything first 
	Base.metadata.create_all(bind = engine) # create table
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()


@pytest.fixture
def client(session):
	'''
	we can use it to generate and delete tables in testing database,
	it give use avoid error if database unique constrain is violated
	'''
	# run our code before we run our test
	# use sqlalchemyto generate and delete table
	# Base.metadata.drop_all(bind = engine) # clear everything first 
	# Base.metadata.create_all(bind = engine) # create table
	# or you can use alembic to generate and delete table
	#command.downgrade("base")
	#command.upgrade("head")

	def override_get_db():
		try:
			yield session
		finally:
			session.close()

	app.dependency_overrides[get_db] = override_get_db
	# yield let us run our code before we return our testClient
	yield TestClient(app) #return TestClient(app)

	# run our code afer our test finishes
	# Base.metadata.drop_all(bind = engine)

def test_create_user(client):
	# send data in body, effect to database
	data = {
		"email":"tester@email.com",
		"password": "123"
	}
	res = client.post('/users/',json = data )
	print(res.json())
	new_user = schemas.UserOut(**res.json()) # this is also a validation by pydantic
	assert new_user.email  == data['email'] #assert res.json().get("email") == data['email']
	assert res.status_code == 201