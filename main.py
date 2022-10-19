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

# list of posts storage purpose
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
			{"title":"title of post 2","content":" i love cooking","id":2},
	]

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
	print(post)
	print(post.dict())
	return {"data":post}
