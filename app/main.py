from fastapi import FastAPI, Response,status,HTTPException
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange

# init app
app = FastAPI()

# return data if valid else return None
# Post schema
class Post(BaseModel):
	title: str
	content: str
	published: bool = True # choice to public post or not, default is True
	# id auto give on postgres server

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

# @app.get("/posts/{id}")
# def get_post(id: int, response: Response): # str as default
# 	post = find_post(id)
# 	if not post:
# 		response.status_code =  status.HTTP_404_NOT_FOUND #404
# 		return {"message":f"post with id {id} not found"}
# 	return {"post_detail": post}

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