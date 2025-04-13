from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    name: str = "Vostok"
    version: str = "0.0.1"
    debug: bool = False


class DataBaseSettings(BaseSettings):
    url: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
    echo: bool = False


app_settings = AppSettings()
db_settings = DataBaseSettings()
