from psycopg2.extras import RealDictCursor # get extra field to get the column when where database
import psycopg2

host = 'localhost'
database = 'fastapi'
user = 'postgres'
password = 'admin123'

while True: # MUST connect to database successfully before runing server API
	try:
		print(f"\nTrying to connect to postgres {host} database {database}")
		conn = psycopg2.connect(host = host,database= database,user = user,
	 								password = password,cursor_factory=RealDictCursor)
		cursor = conn.cursor()
		print(f"\nConnecting to postgres {host} database {database} connected successfully!")
		break # jump out while loop if successed
	except Exception as e:
		print(f"Connecting to postgres {host} database {database} FAILED!")
		print("Error: ",e)
		time.sleep(3)
