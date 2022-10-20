from fastapi import FastAPI, Response,status,HTTPException
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
from psycopg2.extras import RealDictCursor # get extra field to get the column when where database
import psycopg2
import time

# init app
app = FastAPI()

# Post schema
class Post(BaseModel):
	title: str
	content: str
	published: bool = True # default: True
	# id auto given by postgres 
	# timestamp given by postgres 


# try to connect with database
host = 'localhost'
database = 'fastapi'
user = 'postgres'
password = 'admin123'

while True: # MUST connect to database successfully before runing server API
	try:
		print(f"\nTrying to connect to postgres {host} database {database}")
		conn = psycopg2.connect(host = host,database= database,user = user,
	 								password = password,cursor_factory=RealDictCursor)
		cursor = conn.cursor()
		print(f"\nConnecting to postgres {host} database {database} connected successfully!")
		break # jump out while loop if successed
	except Exception as e:
		print(f"Connecting to postgres {host} database {database} FAILED!")
		print("Error: ",e)
		time.sleep(3)

# list of posts storage purpose
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
			{"title":"title of post 2","content":" i love cooking","id":2},
	]

@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

# add another path operation
@app.get("/posts")
def get_posts():
	return {"data":my_posts}

# if you want to change the defa
@app.post("/posts",status_code = status.HTTP_201_CREATED)
def create_post(post:Post):
	post_dict = post.dict()
	post_dict['id'] = randrange(0,1000000) # add new field id into your post, user does not know which id 
	my_posts.append(post_dict)
	return {"data":post_dict}


def find_post(id):
	for p in my_posts:
		if p['id'] == id:
			return p
		else:
			return None

@app.get("/posts/{id}")
def get_post(id: int): # str as default
	post = find_post(id)
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	return {"post_detail": post}

@app.delete("/posts/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
	post = find_post(id)
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	else:
		my_posts.remove(post) # pop index

	# return {"post_deleted":post,
	# 		"message":"Successfully deleted!"}
	# OR DONT send the data back
	return Response(status_code = status.HTTP_204_NO_CONTENT)

def update_content(post,data):
	'''
	Update content in put data to post
	Args:
		post: post
		data: data update content
	Return:
		post: Updated content post
	'''
	keys = post.keys()
	for i in data.keys():
		if i in keys:
			post[i] = data[i]
	return  post

# if you don't use pydantic to validate data, wrong field data-type can be occur
@app.patch("/posts/{id}")
def update_field(id:int,response:Response,data:dict=Body(...)): #,data:dict=Body(...) must be in the last of declaration
	post = find_post(id)
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	#print(data.keys())
	updated_post = update_content(post,data)
	response.status_code = status.HTTP_202_ACCEPTED
	return {"updated_post": updated_post,
			"update_content": data}

@app.put("/posts/{id}")
def update_post(id:int,update_post:Post): #,data:dict=Body(...) must be in the last of declaration
	post = find_post(id)
	index = my_posts.index(post)
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	my_posts[index] = update_post.dict()
	return {"updated_post": update_post.dict(),
			"message":"post updated!"}