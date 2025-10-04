from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database import Base


class Users(Base):
    __tablename__ = "users"  # table name in DB

    id = Column(Integer, primary_key=True, index=True)  # unique ID
    username = Column(String, unique=True, index=True)  # username
    email = Column(String, unique=True, index=True)  # email
    hashed_password = Column(String)  # hashed password
    first_name = Column(String, index=True)  # first name
    last_name = Column(String, index=True)  # last name
    is_active = Column(Boolean, default=True)  # active status
    role = Column(String, default="user")  # user role


# Define Todos table (ORM model)
class Todos(Base):
    __tablename__ = "todos"  # table name in DB

    id = Column(Integer, primary_key=True, index=True)  # unique ID
    title = Column(String, index=True)  # short title
    description = Column(String, index=True)  # details
    priority = Column(Integer, index=True)  # priority number
    completed = Column(Boolean, default=False)  # task status
    owner_id = Column(Integer, ForeignKey("users.id"))  # ID of the user who owns this todo
