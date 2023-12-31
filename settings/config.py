from dotenv import  load_dotenv
from pathlib import  Path
import os

# Loading .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Ecom" # Replace here
    PROJECT_VERSION: str = "0.1.0" # Replace here

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
settings = Settings()