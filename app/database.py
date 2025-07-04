from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
from urllib.parse import quote_plus

encoded_password = quote_plus(settings.database_password)

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{encoded_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Connect to PostgreSQL with retry loop
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='fastapi',
#             user='postgres',
#             password='kamalimsd@127',  # <-- your actual password
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("✅ Database connection was successful!")
#         break
#     except Exception as error:
#         print("❌ Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)
