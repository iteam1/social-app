from psycopg2.extras import RealDictCursor # get extra field to get the column when where database
import psycopg2
import os 

POSTGRES_HOST = os.environ.get('POSTGRES_HOST') 
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE') 
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')
SECRET_KEY  = os.environ.get('SECRET_KEY') 
ALGORITHM = os.environ.get('ALGORITHM') 
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')


while True: # MUST connect to database successfully before runing server API
	try:
		print(f"\nTrying to connect to postgres {POSTGRES_HOST} database {POSTGRES_DATABASE}")
		conn = psycopg2.connect(host = POSTGRES_HOST,database= POSTGRES_DATABASE,user = POSTGRES_USER,
	 								password = POSTGRES_PASS,cursor_factory=RealDictCursor)
		cursor = conn.cursor()
		print(f"\nConnecting to postgres {POSTGRES_HOST} database {POSTGRES_DATABASE} connected successfully!")
		break # jump out while loop if successed
	except Exception as e:
		print(f"Connecting to postgres {POSTGRES_HOST} database {POSTGRES_DATABASE} FAILED!")
		print("Error: ",e)
		time.sleep(3)
