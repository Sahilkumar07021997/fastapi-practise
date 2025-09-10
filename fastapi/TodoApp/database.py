from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (SQLite in this case)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Engine: main connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory: creates DB sessions
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
