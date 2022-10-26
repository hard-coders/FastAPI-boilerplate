from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    debug: bool = True

    secret_key: SecretStr
    crypt_algorithm: str = "HS256"

    db_host: str
    db_port: int = 3306
    db_user: SecretStr
    db_password: SecretStr
    db_database: str

    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
