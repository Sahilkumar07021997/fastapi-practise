from fastapi import FastAPI

import models
from database import engine
from routers import auth, todos, admin

# Create FastAPI instance
app = FastAPI()

# Create database tables from models (if not already created)
models.Base.metadata.create_all(bind=engine)

# Include routers (if any)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
