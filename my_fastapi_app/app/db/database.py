from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

SERVER = os.getenv("DATABASE_SERVER")
DATABASE = os.getenv("DATABASE_NAME")
USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
   
DATABASE_URL = (
    f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

