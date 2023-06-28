from fastapi import FastAPI
# from routers import router


app = FastAPI()


@app.get('/')
async def root():
    return {"health check": '✅!'}

# app.include_router(router)





# # from dotenv import load_dotenv
# # import os
# from fastapi import FastAPI
# # from databases import Database
# from routers import router
# from database import database

# # load_dotenv()

# # use for deployment
# # DATABASE_URL = os.getenv("DATABASE_URL")

# # use for testing
# DATABASE_URL = "postgresql://admin:password@localhost:5432/fjz_local_db"


# app = FastAPI()
# # database = Database(DATABASE_URL)


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# @app.get('/')
# async def root():
#     return {"health check": '✅!'}


# app.include_router(router)









# import os
# from fastapi import FastAPI
# from sqlalchemy import create_engine
# from models import Base
# from database import database
# from routers import router


# DATABASE_URL = os.getenv("DATABASE_URL")
# if DATABASE_URL.startswith("postgres://"):
#     DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


# app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     await database.connect()

#     # create table on startup if not exists
#     engine = create_engine(DATABASE_URL)
#     Base.metadata.create_all(engine)

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# app.include_router(router)
