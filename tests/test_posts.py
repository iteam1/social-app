import pytest
from app import schemas

def test_get_all_posts(authorized_client):
	res = authorized_client.get("/post")
	print("response:",res.json())
	assert res.status_code == 200