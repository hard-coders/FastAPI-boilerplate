import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app import main, utils, models
from app.config import get_settings
from app.db import get_db, Base

settings = get_settings()
engine = create_engine(
    "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
        user=settings.db_user.get_secret_value(),
        password=settings.db_password.get_secret_value(),
        host="localhost",
        port=settings.db_port,
        database="test",
    ),
    pool_pre_ping=True,
    echo=False,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="session")
def db() -> Session:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session")
def app(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    main.app.dependency_overrides[get_db] = override_get_db

    return main.app


@pytest.fixture
def client(app):
    Base.metadata.create_all(bind=engine)

    yield TestClient(app)

    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def add_user(db):
    def func(
        username: str = "test",
        password: str = "1234",
    ):
        user = models.User(username=username, password=utils.create_password_hash(password))
        db.add(user)
        db.commit()

        return user

    return func
