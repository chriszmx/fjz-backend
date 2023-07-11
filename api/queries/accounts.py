from pydantic import BaseModel
from queries.pool import pool
from typing import List, Optional

class AccountIn(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    isAdmin: bool
    isTenant: bool

class AccountOut(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    isAdmin: bool
    isTenant: bool

class AccountRepo:
    def create(self, account: AccountIn) -> AccountOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (email, password, first_name, last_name, isAdmin, isTenant)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                    RETURNING id, email, first_name, last_name, isAdmin, isTenant;
                    """,
                        [
                            account.email,
                            account.password,
                            account.first_name,
                            account.last_name,
                            account.isAdmin,
                            account.isTenant,
                        ],
                )
                id= result.fetchone()[0]
                return AccountOut(
                    id=id,
                    email=account.email,
                    first_name=account.first_name,
                    last_name=account.last_name,
                    isAdmin=account.isAdmin,
                    isTenant=account.isTenant,
                )
