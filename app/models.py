from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.expression import null
from .database import Base

# this is python model also databas table, Changing setup in here you need to delete the table
class Post(Base): # Capitialize
	__tablename__ = "posts"

	id = Column(Integer,primary_key = True,nullable = False)
	title = Column(String,nullable = False)
	content = Column(String,nullable=False)
	published = Column(Boolean,server_default = 'TRUE') 
