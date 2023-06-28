from typing import List
from fastapi import APIRouter, HTTPException
from .models import UserTable, User, UserBase
from .database import database

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_user(user: UserBase):
    query = UserTable.__table__.insert().values(name=user.name)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = UserTable.__table__.select().where(UserTable.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
