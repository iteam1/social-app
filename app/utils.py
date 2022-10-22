from passlib.context import CryptContext

# init hasing password algorithm
pwd_context = CryptContext(schemes=['bcrypt'],deprecated ='auto')

def hash_pass(password = str):
	return pwd_context.hash(password)