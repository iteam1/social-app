from fastapi import FastAPI 

# init app
app = FastAPI()

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
