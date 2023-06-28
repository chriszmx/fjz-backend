import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from database import database, Base
from routers import router

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

    # create table on startup if not exists
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router)





# # from dotenv import load_dotenv
# import os
# from fastapi import FastAPI
# from databases import Database

# # load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# # DATABASE_URL = "postgresql://admin:password@localhost:5432/fjz_local_db"


# app = FastAPI()
# database = Database(DATABASE_URL)


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# @app.get('/')
# async def root():
#     return {"message": 'Hello, world!'}
