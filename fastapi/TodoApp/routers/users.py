from fastapi import Depends, APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from database import SessionLocal
from models import Users
from routers.auth import get_current_user

# Create FastAPI instance
router = APIRouter(
    prefix="/user",
    tags=["user"],
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
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get("/", status_code=200)
async def get_user(user: user_dependency, db: db_dependency):
    """Get user details"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return db.query(Users).filter(Users.id == user.get('id')).first()


@router.put("/change-password", status_code=200)
async def change_password(user: user_dependency, db: db_dependency, passwords: UserVerification):
    """Change user password"""
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    db_user = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(passwords.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    db_user.hashed_password = bcrypt_context.hash(passwords.new_password)
    db.add(db_user)
    db.commit()
    return {"msg": "Password updated successfully"}
