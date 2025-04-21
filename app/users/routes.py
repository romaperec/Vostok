from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.crud import create, login
from app.core.database import get_session
from app.users.schemas import UserRegisterSchema, UserLoginSchema

router = APIRouter()


@router.post("/register")
async def user_registration(
    user_data: UserRegisterSchema, db: AsyncSession = Depends(get_session)
):
    await create(user_data.name, user_data.email, user_data.password, db)
    return {"message": "OK"}


@router.post("/login")
async def user_login(
    user_data: UserLoginSchema, db: AsyncSession = Depends(get_session)
):
    await login(user_data.email, user_data.password, db)
    return {"message": "OK"}