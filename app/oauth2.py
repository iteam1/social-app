from jose import JWTError,jwt
from datetime import datetime,timedelta

SECRET_KEY  = "09c47fdd132bc4c948adf7dac546c2213ab91cbdd572addbfb844aab6167d295" # openssl rand -hex 32 ,serect key
ALGORITHM = "HS256" # Algorithm 
ACCESS_TOKEN_EXPIRE_MINUTES = 30# Expriation Time

def create_access_token(data:dict): # define data is a dict
	to_encode = data.copy() # copy value to encode
	expire = datetime.now() +timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES) #declare time and expire token
	to_encode.update({"exp":expire})
	encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM) # payload and signature
	return encoded_jwt