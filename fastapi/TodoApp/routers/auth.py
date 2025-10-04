from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from starlette import status

from database import SessionLocal
from models import Users

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = '79f9f8f8be2c889f42b411d08cbe0f99'  # for JWT token generation
ALGORITHM = 'HS256'  # algorithm for JWT token
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # token expiry time in minutes


def get_db():
    """Dependency to get DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


def authenticate_user(db, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if user and bcrypt_context.verify(password, user.hashed_password):
        return user
    return None


def create_access_token(username: str, user_id: int, expires_delta: timedelta = ACCESS_TOKEN_EXPIRE_MINUTES):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True
    )

    db.add(create_user_model)
    db.commit()
    return create_user_model


@router.post("/token", status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        return {"error": "Invalid credentials"}
    return {"access_token": "fake-token", "token_type": "bearer"}
