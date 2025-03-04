from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create a synchronous engine
engine = create_engine(DATABASE_URL, echo=True)

# Session maker
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
