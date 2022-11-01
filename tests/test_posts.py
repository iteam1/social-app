import pytest
from typing import List
from app import schemas

# GET

def test_get_all_posts(authorized_client,test_posts):
	res = authorized_client.get("/post/")
	def validate(post):
		return schemas.PostOut(**post)
	assert res.status_code == 200 # check status
	print(res.json())
	assert len(res.json()) == len(test_posts) # check number of test posts
	posts_list = list(map(validate,res.json()))
	# print(posts_list[0].Post)
	# assert posts_list[0].Post.title == test_posts[0].title # check the first object title

def test_get_one_post(authorized_client,test_posts):
	res = authorized_client.get(f"/post/{test_posts[0].id}")
	assert res.status_code == 200
	print(res.json())
	post = schemas.PostOut(**res.json())
	print(post)
	assert post.Post.id == test_posts[0].id
	assert post.Post.title == test_posts[0].title
	assert post.Post.content == test_posts[0].content

def test_unauthorized_user_get_all_posts(unauthorized_client,test_posts):
	res = unauthorized_client.get("/post/")
	# print(unauthorized_client.headers)
	assert res.status_code == 401

def test_unauthorized_user_get_one_post(unauthorized_client,test_posts):
	res = unauthorized_client.get(f"/post/{test_posts[0].id}")
	assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client,test_posts):
	res = authorized_client.get("/post/888")
	print(res.json())
	assert res.status_code == 404

# CREATE

# DELETE

# PUT