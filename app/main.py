from typing import List
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from . import models
from .database import engine,SessionLocal,get_db
from .schemas import PostBase,PostCreate,PostUpdate,PostResponse,UserCreate,UserOut
from .utils import hash_pass
# connect server-databse and create tables
models.Base.metadata.create_all(bind = engine) 

# init app
app = FastAPI()

@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

@app.get("/sqlalchemy")
def test_sqlalchemy(db:Session = Depends(get_db)):
	return {"message":"Successfully!"}

@app.get("/posts",response_model = List[PostResponse]) # Pydantic format
def get_posts(db:Session= Depends(get_db)): # Pydantic format
	posts = db.query(models.Post)
	return posts.all() #{"data":posts.all()}

@app.post("/posts",status_code = status.HTTP_201_CREATED,response_model = PostResponse) # Pydantic format
def create_post(post:PostCreate,db:Session = Depends(get_db)): # Pydantic format
	new_post = models.Post(**post.dict()) # unpackage form 
	db.add(new_post) # add new row
	db.commit() # commit to save it to database
	db.refresh(new_post)
	return new_post# Follow PostResponse 

@app.get("/posts/{id}",response_model = PostResponse)
def get_post(id: int,db: Session = Depends(get_db)): # str as default
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	return post #{"post_detail": post}

@app.delete("/posts/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db)):
	post_query = db.query(models.Post).filter(models.Post.id==id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	else:
		# db.delete(post)
		# db.commit()
		post_query.delete(synchronize_session =False)
		db.commit()

	return Response(status_code = status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model = PostResponse)
def update_post(id:int,update_post:PostBase,db:Session = Depends(get_db)): #,data:dict=Body(...) must be in the last of declaration
	
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	print(post.title)

	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	
	# post.update({'title':update_post.dict()['title'],
	# 			'content':update_post.dict()['content'],
	# 			'published':update_post.dict()['published']
	# 			},synchronize_session =False)
	
	post_query.update(update_post.dict(),synchronize_session =False)
	db.commit()

	return post_query.first() #{"updated_post": post_query.first(),"message":"post updated!"}

@app.patch("/posts/{id}",response_model = PostResponse)
def update_field(id:int,response:Response,data:dict=Body(...),db: Session= Depends(get_db)): #,data:dict=Body(...) must be in the last of declaration
	
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")

	# update
	if 'title' in data.keys():
		post.title = data['title']

	if 'content' in data.keys():
		post.content = data['content']

	if 'published' in data.keys():
		post.published = data['published']

	db.commit()

	response.status_code = status.HTTP_202_ACCEPTED

	return post_query.first() #{"message":"successfully","data":post_query.first()}

@app.get("/users",response_model = List[UserOut])
def get_users(db: Session = Depends(get_db)):
	users = db.query(models.User)
	return users.all()

@app.get("/users/{id}",response_model = List[UserOut])
def get_user(id:int,db:Session = Depends(get_db)):
	user  = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"user with id {id} not found")
	return user

@app.post("/users",status_code = status.HTTP_201_CREATED,response_model = UserOut)
def create_user(user: UserCreate ,db: Session = Depends(get_db)):

	#hash the password -user.password
	hashed_password = hash_pass(user.password)
	user.password = hashed_password

	# create new user
	new_user = models.User(**user.dict()) # unpackage form 
	db.add(new_user) # add new row
	db.commit() # commit to save it to database
	db.refresh(new_user) # refesh to see brand new user
	return new_user# Follow PostResponse
	return {"message":"successed"}
