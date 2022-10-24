from pydantic import BaseModel,EmailStr,BaseSettings
from datetime import datetime
from typing import Optional

class Settings(BaseSettings):
	database_password: str = '123' # default
	database_username: str = 'postgres'
	database_name: str = 'fastapi'
	hostname: str = 'localhost'
	secret_key: str = "sdfjs34563439u"
	expired_time: int = 30

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

class PostBase(BaseModel):
	'''
	PostBase inherited from BaseModel
	'''
	title: str
	content: str
	published: bool = True # default
	# owner_id: int

class PostCreate(PostBase):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

class PostUpdate(BaseModel):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

class PostCreated(PostBase):
	title: str
	content: str
	published: bool
	owner: UserOut # pydantic class

	class Config:
		orm_mode = True

class PostResponse(PostBase):
	id: int
	create_at: datetime #str
	owner_id: int
	class Config:
		'''
		Pydantic;s orm_mode will tell Pydantic model to read data even if it is not a dict, but ORM model
		(or nay other arbitrary object with attriutes) data['id'] = data.id
		'''
		orm_mode = True

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: Optional[str] = None
