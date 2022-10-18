from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

# init app
app = FastAPI()

# return data if valid else return None
# Post schema
class Post(BaseModel):
	title: str
	content: str
	published: bool = True # choice to public post or not, default is True
	rating: Optional[int] = None # optional field, integer or None

# look for the first match
# when you send a request to a path, FastAPI starting search from the top and stop at path where your path is match
# decorator
@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

# add another path operation
@app.get("/posts")
def get_posts():
	return {"data":"This is your posts"}

# add post-method for sending post-request
# send some data raw-type in body as json,text,etc.
# Body() extract all the field in body and convert into python-dict and store inside variable name payload
# title - str,content - str
@app.post("/posts")
def create_posts(payload:dict=Body(...)): # payload or any name you want
	print(payload) # dict-type
	return {"message":"successfully created posts",
			"new_post":f"title {payload['title']}",
			"content":f"content {payload['content']}"}

# valid data with
@app.post("/createposts")
def create_posts(post:Post): # valid post data by Post class created
	print(post)
	# convert pydantic model into dict
	print(post.dict())
	return{"data":post}