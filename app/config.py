from .schemas import Settings
import os 

POSTGRES_HOST = os.environ.get('POSTGRES_HOST') 
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE') 
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')
SECRET_KEY  = os.environ.get('SECRET_KEY') 
ALGORITHM = os.environ.get('ALGORITHM') 
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

settings = Settings()
settings.database_password = POSTGRES_PASS
settings.database_username = POSTGRES_USER
settings.database_name = POSTGRES_DATABASE
settings.hostname = POSTGRES_HOST
settings.secret_key = SECRET_KEY
settings.expired_time = int(ACCESS_TOKEN_EXPIRE_MINUTES)