from databases import Database
from models import users
from sqlalchemy.sql import select

async def get_users(database: Database):
    query = select([users])
    return await database.fetch_all(query)

async def create_user(database: Database, name: str, email: str):
    query = users.insert().values(name=name, email=email)
    await database.execute(query)




# from sqlalchemy.orm import Session
# import models

# def get_items(db: Session):
#     return db.query(models.Item).all()

# def create_item(db: Session, name: str, description: str):
#     item = models.Item(name=name, description=description)
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item
