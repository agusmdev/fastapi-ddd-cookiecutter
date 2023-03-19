"""Configuration to use in the app"""

from typing import List

from pydantic import BaseSettings, Field


class CommonSettings(BaseSettings):
    APP_NAME: str = Field(default="{{cookiecutter.project_name| capitalize}}")
    DEBUG_MODE: bool = Field(default=True)


class DatabaseSettings(BaseSettings):
    DB_NAME: str = "{{cookiecutter.project_name| lower}}"
    REPOSITORY_NAME: str = Field(default="MemoryRepo")


class CORSSettings(BaseSettings):
    FRONTEND_URL: str = "http://localhost:3000"
    DEBUG_FRONT_URLS: List[str] = []


class Settings(
    CommonSettings,
    DatabaseSettings,
    CORSSettings,
):
    class Config:
        env_file = ".env"


settings = Settings()
