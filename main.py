from fastapi import FastAPI
from databases import Database

DATABASE_URL = "Your database URL here"  # Replace with your PostgreSQL database URL

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
