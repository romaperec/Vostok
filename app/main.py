from fastapi import FastAPI

from core.config import app_settings


app = FastAPI(
    title=app_settings.name, version=app_settings.version, debug=app_settings.debug
)
