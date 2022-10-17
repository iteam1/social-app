from fastapi import FastAPI 

# init app
app = FastAPI()

# decorator
@app.get("/") #method and path
def root(): # the function option async
	return{"message":"Hello World!"}