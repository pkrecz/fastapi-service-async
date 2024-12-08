import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    title: str = "Application template"
    version: str = "1.0.0"
    docs_url: str = "/swagger"


    ACCESS_SECRET_KEY: str = str(os.getenv("ACCESS_SECRET_KEY"))
    REFRESH_SECRET_KEY: str = str(os.getenv("REFRESH_SECRET_KEY"))
    ALGORITHM: str = str(os.getenv("ALGORITHM"))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ADMIN_USER_NAME: str = str(os.getenv("ADMIN_USER_NAME"))


settings = Settings()
