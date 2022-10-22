from fastapi import Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas import UserLogin
from ..utils import verify

router = APIRouter(prefix = '/login',tags= ['authentication'])

@router.post('/')
def login(user_credentials: UserLogin,db :Session= Depends(get_db)):
	user = db.query(models.User).filter(models.User.email== user_credentials.email).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
							detail = f"Invalid Credentials")
	# compare the password new_hash = user.hash
	match = verify(user_credentials.password,user.password)
	if not match:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
							detail = f"Invalid Credentials")

	# create a token
	return {"token":"example token"}


