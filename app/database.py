from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

POSTGRES_HOST = os.environ.get('POSTGRES_HOST') 
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE') 
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')
SECRET_KEY  = os.environ.get('SECRET_KEY') 
ALGORITHM = os.environ.get('ALGORITHM') 
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')

#f"postgresql://<{username}>:<{password}>@<{ip_address}/{hostname}>/<{database_name}>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}/{POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL) # engine to connect datanase

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) # for taking with database

Base = declarative_base() # Model Base for create table

# Dependency [request] -> [create session] -> [create sql] -> [close session]
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()