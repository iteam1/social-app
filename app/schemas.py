from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

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

class PostResponse(PostBase):
	id: int
	create_at: datetime #str
	class Config:
		'''
		Pydantic;s orm_mode will tell Pydantic model to read data even if it is not a dict, but ORM model
		(or nay other arbitrary object with attriutes) data['id'] = data.id
		'''
		orm_mode = True

class UserCreate(BaseModel):
	email: EmailStr# email validation
	password: str
	# create_at: datetime default

class UserOut(BaseModel):
	id: int
	email: EmailStr
	create_at: datetime
	class Config:
		orm_mode = True

class UserLogin(BaseModel):
	email:EmailStr
	password:str

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: Optional[str] = None
