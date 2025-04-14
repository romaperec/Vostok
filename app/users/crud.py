from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from app.core.database import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from app.users.models import UserModel
from app.users.schemas import UserSchema
from app.users.service import hash_password


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
