from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas, utils
from app.api import deps
from app.db import get_db

router = APIRouter()


@router.post("/signup", response_model=schemas.ResourceId, status_code=201)
def signup(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=username).first()

    if user:
        raise HTTPException(status_code=400, detail="Username is already taken")

    user = models.User(username=username, password=utils.create_password_hash(password))
    db.add(user)
    db.commit()

    return user


@router.post("/login", response_model=schemas.Token)
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(username=data.username).first()

    if not user or not utils.verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    return schemas.Token(access_token=utils.create_access_token({"id": user.id}))


@router.get("/me", response_model=schemas.User)
def get_current_user(user: models.User = Depends(deps.get_current_user)):
    return user
