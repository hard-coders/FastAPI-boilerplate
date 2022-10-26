from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError, jwt
from sqlalchemy.orm import Session

from app import models
from app.config import get_settings
from app.db import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
settings = get_settings()


class QueryParams:
    def __init__(self, offset: int = 0, limit: int = 10):
        self.offset = offset
        self.limit = limit


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    try:
        data = jwt.decode(token, settings.secret_key.get_secret_value(), settings.crypt_algorithm)
    except ExpiredSignatureError:
        raise HTTPException(401, "Expired")
    user = db.query(models.User).filter_by(id=data.get("id")).first()

    if not user:
        raise HTTPException(401, "Invalid credentials")

    return user
