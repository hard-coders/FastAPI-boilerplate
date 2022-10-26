from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from humps import decamelize
from app.config import get_settings


settings = get_settings()

engine = create_engine(
    "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
        user=settings.db_user.get_secret_value(),
        password=settings.db_password.get_secret_value(),
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_database,
    ),
    pool_pre_ping=True,
    echo=settings.debug,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return decamelize(cls.__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

