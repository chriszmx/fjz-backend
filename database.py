from sqlalchemy import Table, Column, Integer, String, MetaData
from databases import Database

import os

DATABASE_URL = os.environ['DATABASE_URL']

# DATABASE_URL = "postgresql://admin:password@localhost:5432/fjz_local_db"

database = Database(DATABASE_URL)

database = Database(DATABASE_URL, min_size=1, max_size=10)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(50))
)

async def create_tables():
    engine = database._url._engine
    metadata.create_all(engine)





# from databases import Database
# import os

# DATABASE_URL = os.getenv("DATABASE_URL")
# database = Database(DATABASE_URL)
