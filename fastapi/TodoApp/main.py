from fastapi import FastAPI
import models
from database import engine

# Create FastAPI instance
app = FastAPI()

# Create database tables from models (if not already created)
models.Base.metadata.create_all(bind=engine)
