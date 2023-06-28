# from fastapi import APIRouter, HTTPException, Depends
# from typing import List
# from database import database
# from crud import get_users, create_user

# router = APIRouter()

# @router.get("/users", response_model=List[dict])
# async def read_users():
#     return await get_users(database)

# @router.post("/users")
# async def create_new_user(name: str, email: str):
#     await create_user(database, name, email)
#     return {"name": name, "email": email}



# from typing import List
# from fastapi import APIRouter, HTTPException
# from models import UserTable, User, UserBase
# from database import database

# router = APIRouter()


# @router.post("/users/", response_model=User)
# async def create_user(user: UserBase):
#     query = UserTable.__table__.insert().values(name=user.name)
#     last_record_id = await database.execute(query)
#     return {**user.dict(), "id": last_record_id}


# @router.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     query = UserTable.__table__.select().where(UserTable.id == user_id)
#     user = await database.fetch_one(query)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
