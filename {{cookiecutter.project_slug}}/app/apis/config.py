"""Configuration to use in the app"""

from typing import List

from pydantic import BaseSettings, Field


class CommonSettings(BaseSettings):
    APP_NAME: str = Field(default="{{cookiecutter.project_name| capitalize}}")
    DEBUG_MODE: bool = Field(default=True)


class ServerSettings(BaseSettings):
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)


class DatabaseSettings(BaseSettings):
    DB_NAME: str = "{{cookiecutter.project_name| lower}}"
    REPOSITORY_NAME: str = Field(default="InMemoryRepository")


class CORSSettings(BaseSettings):
    FRONTEND_URL: str = "http://localhost:3000"
    DEBUG_FRONT_URLS: List[str] = []


class Settings(
    CommonSettings,
    ServerSettings,
    DatabaseSettings,
    CORSSettings,
):
    class Config:
        env_file = ".env"


settings = Settings()
