from sqlalchemy import Column, Integer, DateTime, func, String

from app.db import Base


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), comment="생성일시")
    updated_at = Column(
        DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(), comment="수정일시"
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.id}>"


class User(BaseMixin, Base):
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
