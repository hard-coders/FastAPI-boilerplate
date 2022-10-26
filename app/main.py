from fastapi import FastAPI

from app.api import auth
from app.config import get_settings


settings = get_settings()

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["인증"])


@app.on_event("startup")
def startup():
    if settings.debug:
        from app.db import Base, engine

        Base.metadata.create_all(engine)


@app.get("/health")
@app.get("/")
def index():
    return b"ok"
