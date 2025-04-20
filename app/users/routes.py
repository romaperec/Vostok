from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.crud import create
from app.core.database import get_session
from app.users.schemas import UserSchema

router = APIRouter()


@router.post("/register")
async def user_registration(
    request: Request, user_data: UserSchema, db: AsyncSession = Depends(get_session)
):
    await create(user_data.name, user_data.email, user_data.password, db)
    return {"message": "OK"}
