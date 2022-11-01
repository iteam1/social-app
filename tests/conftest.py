'''
this is a specify module for storing pytest.fixturr
the pytest.fixture defined in here can be accessable from any test module in THE SAME DIRECTORY
'''
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from app import models
from app.database import get_db,Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.oauth2 import create_access_token
# from alembic import command
# testing database url
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"
# init database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# init session to communicate with database
TestingSessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) 

# client depend on session
# scope = function will destroy database evrytime
# scope = module will destroy fixture in the end of module
# scope = session will destroy fixture after run all modules

@pytest.fixture(scope = "module")
def session():
	#print("my session fixture ran")
	Base.metadata.drop_all(bind = engine)
	Base.metadata.create_all(bind = engine)
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()

@pytest.fixture(scope = "module")
def client(session):
	def override_get_db():
		try:
			yield session
		finally:
			session.close()
	app.dependency_overrides[get_db] = override_get_db
	yield TestClient(app)

@pytest.fixture
def test_user(client):
	data = {
		"email":"tester2@email.com",
		"password": "123"
	}
	res = client.post("/users/",json = data)
	assert res.status_code == 201
	print(res.json())
	new_user = res.json()
	new_user['password'] = data['password'] # add field password
	return new_user

@pytest.fixture
def token(test_user):
	print(test_user)
	access_token = create_access_token({"user_id":test_user['id']})
	print("access_token: ",access_token)
	return access_token

'''
this is the client (for sending requests) with added token in header
take client, add token generated in to header and return it
'''
@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "token": token
    }
    print(client.headers)

    return client