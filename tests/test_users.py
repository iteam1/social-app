import pytest
from app import schemas
from .database import client,session

def test_create_user(client):
	# send data in body, effect to database
	data = {
		"email":"tester@email.com",
		"password": "123"
	}
	res = client.post('/users/',json = data )
	print(res.json())
	new_user = schemas.UserOut(**res.json())
	assert new_user.email  == data['email']
	assert res.status_code == 201

def test_login_user(client):
	data = {
		"username":"tester@email.com",
		"password": "123"
	}
	res = client.post('/login/',data = data ) # from data
	print(res.json())

	assert res.status_code == 200
