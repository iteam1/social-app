from jose import JWTError,jwt
from datetime import datetime,timedelta
from .schemas import TokenData,UserOut
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import models
from . import conn,cursor

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

SECRET_KEY  = "09c47fdd132bc4c948adf7dac546c2213ab91cbdd572addbfb844aab6167d295" # openssl rand -hex 32 ,serect key
ALGORITHM = "HS256" # Algorithm 
ACCESS_TOKEN_EXPIRE_MINUTES = 30# Expriation Time

def create_access_token(data:dict): # define data is a dict
	to_encode = data.copy() # copy value to encode
	expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES) #declare time and expire token
	to_encode.update({"exp":expire})
	encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM) # payload and signature
	return encoded_jwt

def verify_access_token(token:str,credentials_exception):
	'''
	Raise if Error
	Return token data if it valid
	'''
	try:
		# decode the token 
		payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM]) # if the time is expired also return none
		# get the id
		id: str = payload.get('user_id')
		# if there is a id exist
		if id is None:
			raise credentials_exception
		# create a schema for shaping data
		token_data = TokenData(id =id) # validate by TokenData schema
		return token_data
	except JWTError:
		raise credentials_exception

def get_current_user(token:str = Depends(oauth2_scheme)):

	credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
											detail = f"Could not validate credentials",
											headers = {"WWW-Authenticate":"Bearer"})

	# get token data
	token = verify_access_token(token,credentials_exception) # {'id':id}

	# query user id get ERROR Depends has no attritute query.Must attach is on post routes because oauth2 is not route
	#user = db.query(models.User).filter(models.User.id == token.id).first() 
	
	cursor.execute(f"""SELECT * FROM users WHERE id = {token.id}""")
	user = cursor.fetchone()
	user = dict(user) #convert to dict 

	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"credentials user id {id} is not found")

	return {'user_id':user['id'],'email':user['email']}