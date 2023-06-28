from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from pydantic import BaseModel

Base = declarative_base()


class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
