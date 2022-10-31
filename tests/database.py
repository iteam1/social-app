import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from app import models
from app.database import get_db,Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from alembic import command

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) 

@pytest.fixture(scope = "module")
def client(session):
	def override_get_db():
		try:
			yield session
		finally:
			session.close()
	app.dependency_overrides[get_db] = override_get_db
	yield TestClient(app)

# client depend on session
@pytest.fixture(scope = "module")
def session():
	Base.metadata.drop_all(bind = engine) #scope = function will destroy database evrytime, scope = module will destroy it in the end
	Base.metadata.create_all(bind = engine)
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()