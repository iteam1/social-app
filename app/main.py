import psycopg2
import time
from fastapi import FastAPI, Response,status,HTTPException,Depends
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
from psycopg2.extras import RealDictCursor # get extra field to get the column when where database
from . import models
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine) # create tables

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

@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
	return {"status":"Successed!"}

# add another path operation
@app.get("/posts")
def get_posts():
	cursor.execute("""SELECT * FROM posts""")
	posts = cursor.fetchall()
	# print(type(posts)) # list
	return {"data":posts}

# if you want to change the defa
@app.post("/posts",status_code = status.HTTP_201_CREATED)
def create_post(post:Post):
	#cursor.execute(f"""INSERT INTO posts (title,content,published) VALUES (post.title,post.content,post.published)""")
	# anty hacking by content
	cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",
						(post.title,post.content,post.published))
	new_post = cursor.fetchone() # get thing return from cursor
	conn.commit()
	return {"message":"data created!","data":new_post}

@app.get("/posts/{id}")
def get_post(id: int): # str as default
	cursor.execute(f"""SELECT * FROM posts WHERE id = {id}""")
	post = cursor.fetchone()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	return {"post_detail": post}

@app.delete("/posts/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
	cursor.execute(f"""SELECT * FROM posts WHERE id = {id}""")
	post = cursor.fetchone()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	else:
		cursor.execute(f"""DELETE FROM posts WHERE id = {id}""")
		conn.commit()

	return Response(status_code = status.HTTP_204_NO_CONTENT)

def update_content(post,data):
	'''
	Update content in put data to post
	Args:
		post: (dict) post
		data: (dict) data update content
	Return:
		post: Updated content post
	'''
	keys = post.keys()
	for i in data.keys():
		if i in keys:
			post[i] = data[i]
	return  post

@app.patch("/posts/{id}")
def update_field(id:int,response:Response,data:dict=Body(...)): #,data:dict=Body(...) must be in the last of declaration
	cursor.execute(f"""SELECT * FROM posts WHERE id = {id}""")
	post = cursor.fetchone()
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
	cursor.execute(f"""SELECT * FROM posts WHERE id = {id}""")
	post = cursor.fetchone()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	cursor.execute("""UPDATE posts SET (title,content,published) = (%s,%s,%s) WHERE id = %s""",
		(update_post.title,update_post.content,update_post.published,id))
	conn.commit()
	return {"updated_post": update_post.dict(),
			"message":"post updated!"}