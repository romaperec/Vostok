from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.config import db_settings

engine = create_async_engine(url=db_settings.url, echo=db_settings.echo)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_sesion():
    async with async_session() as session:
        yield session


class Base(DeclarativeBase): ...
