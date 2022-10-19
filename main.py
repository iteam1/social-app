from fastapi import FastAPI
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
	rating: Optional[int] = None # optional field, integer or None

# list of posts storage purpose
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
			{"title":"title of post 2","content":" i love cooking","id":2},
	]

def find_post(id):
	for p in my_posts:
		if p['id'] == id:
			return p
		else:
			return None

# look for the first match
# when you send a request to a path, FastAPI starting search from the top and stop at path where your path is match
# decorator
@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

# add another path operation
@app.get("/posts")
def get_posts():
	return {"data":my_posts}

@app.post("/posts")
def create_posts(post:Post):
	# print(post)
	# print(post.dict())
	post_dict = post.dict()
	post_dict['id'] = randrange(0,1000000) # add new field id into your post, user does not know which id 
	my_posts.append(post_dict)
	return {"data":post_dict}

# make mistake with /posts/{id}
@app.get("/posts/latest")
def get_latest_post():
	latest_post = my_posts[len(my_posts)-1]
	return {"lalest_post":latest_post}
	
@app.get("/posts/{id}")
def get_post(id: int): # str as default
	#print(type(id))
	#post = find_post(int(id))
	post = find_post(id)
	return {"post_detail": post}

# # make mistake with /posts/{id}
# @app.get("/posts/latest")
# def get_latest_post():
# 	latest_post = my_posts[len(my_posts)-1]
# 	return {"lalest_post":latest_post}