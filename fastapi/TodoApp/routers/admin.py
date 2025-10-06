from fastapi import Depends, HTTPException, APIRouter
from starlette import status
from typing_extensions import Annotated

from database import SessionLocal
from models import Users, Todos
from routers.auth import get_current_user

# Create FastAPI instance
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


def get_db():
    """Dependency to get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


def admin_only(user: user_dependency):
    """Dependency to ensure the user has admin role"""
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user


@router.get("/users", status_code=status.HTTP_200_OK)
async def get_all_users(user: Annotated[dict, Depends(admin_only)], db: db_dependency):
    """Get all users (admin only)"""
    users = db.query(Users).all()
    return users


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: Annotated[dict, Depends(admin_only)], db: db_dependency, user_id: int):
    """Delete a user by ID (admin only)"""
    user_to_delete = db.query(Users).filter(Users.id == user_id).first()
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user_to_delete)
    db.commit()
    return


@router.get("/todos", status_code=status.HTTP_200_OK)
async def get_all_todos(user: Annotated[dict, Depends(admin_only)], db: db_dependency):
    """Get all todos (admin only)"""
    todos = db.query(Todos).all()
    return todos


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: Annotated[dict, Depends(admin_only)], db: db_dependency, todo_id: int):
    """Delete a todo by ID (admin only)"""
    todo_to_delete = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_to_delete is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_to_delete)
    db.commit()
    return
