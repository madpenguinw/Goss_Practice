from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 9000
    MONGO_DB_NAME: str = "db_name"
    MONGO_COLLECTION: str = "collection"
    MONGO_USER: str = "user"
    MONGO_PASSWORD: str = "password"

    class Config:
        env_file = ".env"

    @property
    def db_dsn(self) -> str:
        return (
            f"mongodb+srv://{self.MONGO_USER}:{self.MONGO_PASSWORD}@"
            f"{self.MONGO_USER}.cxipusc.mongodb.net/?"
            "retryWrites=true&w=majority"
        )


@lru_cache()
def get_settings():
    return Settings()
