from pydantic import BaseModel

# Post schema
class Post(BaseModel):
	title: str
	content: str
	published: bool = True # default: True
	# id auto given by sqlalchemy models -> postgres 
	# timestamp auto given by sqlalchemy models -> postgres

class CreatePost(BaseModel):
	title: str
	content: str
	published: bool = True

class UpdatePost(BaseModel):
	title: str
	content: str
	published: bool = True