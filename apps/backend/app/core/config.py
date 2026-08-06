from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Attendance Tracker API"
    debug: bool = True

    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.database_user}:"
            f"{self.database_password}@"
            f"{self.database_host}:"
            f"{self.database_port}/"
            f"{self.database_name}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
