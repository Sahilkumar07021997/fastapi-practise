from fastapi import Depends, HTTPException, Path, APIRouter
from pydantic import BaseModel, Field
from starlette import status
from typing_extensions import Annotated

from database import SessionLocal
from models import Todos
from routers.auth import get_current_user

# Create FastAPI instance
router = APIRouter()


def get_db():
    """Dependency to get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=300)
    priority: int = Field(gt=0, lt=6)
    completed: bool = False


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    """Read all todo items"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    todos = db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
    return todos


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(..., gt=0)):
    """Read a specific todo item by ID"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    todo = db.query(Todos).filter(Todos.owner_id == user.get('id'), Todos.id == todo_id).first()
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    """Create a new todo item"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    new_todo = Todos(**todo_request.dict(), owner_id=user.get('id'))
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(
        user: user_dependency,
        db: db_dependency,
        todo_request: TodoRequest,
        todo_id: int = Path(..., gt=0)
):
    """Update an existing to-do item by ID"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    todo = db.query(Todos).filter(Todos.owner_id == user.get('id'), Todos.id == todo_id).first()

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo_request.dict().items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(..., gt=0)):
    """Delete a to-do item by ID"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    todo = db.query(Todos).filter(Todos.owner_id == user.get('id'), Todos.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return
