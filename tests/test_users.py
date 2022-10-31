import pytest
from app import schemas
from app.config import settings
# from .database import client,session
from jose import jwt

def test_create_user(client):
	# send data in body, effect to database
	data = {
		"email":"tester@email.com",
		"password": "123"
	}
	res = client.post('/users/',json = data)
	print(res.json())
	new_user = schemas.UserOut(**res.json())
	assert new_user.email  == data['email']
	assert res.status_code == 201

def test_login_user(client,test_user):
	res = client.post('/login/',data = {
		"username": test_user['email'],
		"password": test_user['password']
	})
	# check status code
	assert res.status_code == 200
	print(res.json())
	login_res = schemas.Token(**res.json()) # pydantic object
	payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
	# check the token type
	token_type = login_res.token_type
	assert token_type == "bearer"
	# check id of user match
	id = payload.get('user_id')
	assert id == test_user['id']

