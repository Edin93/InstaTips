from fastapi import APIRouter, HTTPException, status

from api.database import database, user_table
from api.models.user import UserIn
from api.security import get_user

router = APIRouter()


@router.post("/register", status_code=201)
async def register(user: UserIn):
    if await get_user(user.mail):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with that email already exists",
        )
    query = user_table.insert().values(email=user.email, password=user.password)
    await database.execute(query)
    return {
        "detail": "User account created",
    }
