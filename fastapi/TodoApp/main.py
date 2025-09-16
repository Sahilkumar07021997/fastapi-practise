from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status
from typing_extensions import Annotated

import models
from database import engine, SessionLocal
from models import Todos

# Create FastAPI instance
app = FastAPI()

# Create database tables from models (if not already created)
models.Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency to get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=300)
    priority: int = Field(gt=0, lt=6)
    completed: bool = False


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    """Read all todo items"""
    todos = db.query(Todos).all()
    return todos


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(..., gt=0)):
    """Read a specific todo item by ID"""
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    """Create a new todo item"""
    new_todo = Todos(**todo_request.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(
        db: db_dependency,
        todo_request: TodoRequest,
        todo_id: int = Path(..., gt=0)
):
    """Update an existing to-do item by ID"""
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo_request.dict().items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(..., gt=0)):
    """Delete a to-do item by ID"""
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return
