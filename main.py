from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, crud, database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return {"items": items}


@app.post("/items")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = crud.create_item(db, name, description)
    return {"item": item}
