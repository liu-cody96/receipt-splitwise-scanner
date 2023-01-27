import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

SERVER_NAME = 'localhost:8000'

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@kashin.db.elephantsql.com/{DB_USER}'