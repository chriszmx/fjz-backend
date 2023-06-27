from fastapi import FastAPI
from databases import Database

DATABASE_URL = "postgres://buahjlpraqcgfr:79acca9b13aee2e87aa1ec40ce28b316cffca26abfcf6271695aa070c9279759@ec2-3-92-151-217.compute-1.amazonaws.com:5432/d33u912bcdif9u"

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
