from fastapi import(
    Depends,
    APIRouter
)

from queries.accounts import AccountIn, AccountOut, AccountRepo

router = APIRouter()

@router.post("/api/accounts", response_model=AccountOut)
def create_account(
    info: AccountIn,
    repo: AccountRepo = Depends()
):
    return repo.create(info)
