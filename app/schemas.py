from pydantic import BaseModel

# REQUEST SCHEMA

class PostBase(BaseModel):
	'''
	PostBase inherited from BaseModel
	'''
	title: str
	content: str
	published: bool = True

class PostCreate(PostBase):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

class PostUpdate(PostBase):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

# RESPONSE SCHEMA

class PostResponse(BaseModel):
	id: int
	title: str
	content: str
	published: bool
	# No send back id and created_at
	class Config:
		'''
		Pydantic;s orm_mode will tell Pydantic model to read data even if it is not a dict, but ORM model
		(or nay other arbitrary object with attriutes) data['id'] = data.id
		'''
		orm_mode = True