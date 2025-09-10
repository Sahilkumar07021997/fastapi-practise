from sqlalchemy import Column, Integer, String, Boolean

from database import Base


# Define Todos table (ORM model)
class Todos(Base):
    __tablename__ = "todos"  # table name in DB

    id = Column(Integer, primary_key=True, index=True)  # unique ID
    title = Column(String, index=True)  # short title
    description = Column(String, index=True)  # details
    priority = Column(Integer, index=True)  # priority number
    completed = Column(Boolean, default=False)  # task status
