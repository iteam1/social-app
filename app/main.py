from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine,get_db
from .routers import post,user,auth

# connect server-databse and create tables
models.Base.metadata.create_all(bind = engine)

# init app
app = FastAPI()

# include route
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/") # method and path
def root(): # the function option async
	return{"message":"wellcome to my api"} # FastAPI auto convert dict into json

@app.get("/sqlalchemy")
def test_sqlalchemy(db:Session = Depends(get_db)):
	return {"message":"Successfully!"}
