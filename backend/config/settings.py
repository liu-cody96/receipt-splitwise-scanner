import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

SERVER_NAME = 'localhost:8000'

DB_URL = os.getenv('TEST_DB_URL')

SQLALCHEMY_DATABASE_URI = DB_URL

JWT_SECRET_KEY = os.getenv("TEST_MY_SECRET")