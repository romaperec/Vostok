from fastapi import HTTPException, status
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.users.models import UserModel
from app.users.service import hash_password
from app.users.service import verify_password

async def create(user_name, user_email, user_password, db: AsyncSession):
    check_email = await db.execute(
        select(UserModel).where(UserModel.email == user_email)
    )
    check_email = check_email.scalar_one_or_none()

    if check_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already taken"
        )

    hashed_password = hash_password(user_password)

    user = UserModel(name=user_name, email=user_email, password=hashed_password)

    db.add(user)
    await db.commit()


async def login(user_email, user_password, db: AsyncSession):
    user_db = await db.execute(
        select(UserModel).where(UserModel.email == user_email)
    )
    user_db = user_db.scalar_one_or_none()

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Account not found"
        )
    
    if verify_password(user_password, user_db.password):
        return user_db