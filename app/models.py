from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.expression import null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

# this is python model also databas table, Changing setup in here you need to delete the table
class Post(Base): # Capitialize
	__tablename__ = "posts"

	id = Column(Integer,primary_key = True,nullable = False)
	title = Column(String,nullable = False)
	content = Column(String,nullable=False)
	published = Column(Boolean,server_default = 'TRUE')
	create_at = Column(TIMESTAMP(timezone=True),nullable =False,server_default= text('now()'))


class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer,primary_key = True,nullable = False)
	email = Column(String,nullable=False,unique = True)
	password = Column(String,nullable=False)
	created_at = Column(TIMESTAMP(timezone=True),nullable = False,server_default = text('now()'))
	
