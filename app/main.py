import time
from fastapi import FastAPI, Response,status,HTTPException,Depends
from fastapi.params import Body
from . import models
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from .schemas import Post

models.Base.metadata.create_all(bind = engine) # create tables

# init app
app = FastAPI()

@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

@app.get("/sqlalchemy")
def test_sqlalchemy(db:Session = Depends(get_db)):
	return {"message":"Successfully!"}

@app.get("/posts")
def get_posts(db:Session= Depends(get_db)):
	posts = db.query(models.Post)
	return {"data":posts.all()}

@app.post("/posts",status_code = status.HTTP_201_CREATED)
def create_post(post:Post,db:Session = Depends(get_db)):
	# create row follow model
	# new_post = models.Post(title = post.title,content = post.content, published = post.published) 
	new_post = models.Post(**post.dict()) # unpackage form 
	db.add(new_post) # add new row
	db.commit() # commit to save it to database
	db.refresh(new_post)
	return {"message":"data created!","data":new_post}

@app.get("/posts/{id}")
def get_post(id: int,db: Session = Depends(get_db)): # str as default
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	return {"post_detail": post}

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

@app.put("/posts/{id}")
def update_post(id:int,update_post:Post,db:Session = Depends(get_db)): #,data:dict=Body(...) must be in the last of declaration
	
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

	return {"updated_post": post_query.first(),
			"message":"post updated!"}

@app.patch("/posts/{id}")
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

	return({"message":"successfully",
			"data":post_query.first()})

