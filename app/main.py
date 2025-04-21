from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import app_settings
from app.users.routes import router as user_router


app = FastAPI(
    title=app_settings.name, version=app_settings.version, debug=app_settings.debug
)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    app.state.temout = 60
