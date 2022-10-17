from fastapi import FastAPI 

# init app
app = FastAPI()

@app.get("/")
async def root():
	return{"message":"Hello World!"}