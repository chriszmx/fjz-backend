# from dotenv import load_dotenv
import os
from fastapi import FastAPI
from databases import Database

# load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


app = FastAPI()
database = Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def root():
    return {"message": "Hello, world!"}

@app.get("/users")
async def read_users():
    query = "SELECT * FROM users"
    results = await database.fetch_all(query)
    return {"users": results}
