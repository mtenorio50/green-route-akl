from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # Auckland Transport API settings
    at_subscription_key: str = Field(alias='AT_SUBSCRIPTION_KEY')
    at_base_url: str = Field(
        default="https://api.at.govt.nz", alias='AT_BASE_URL')
    cache_ttl_seconds: int = Field(default=15, alias='CACHE_TTL_SECONDS')

    # Database settings (optional, can be used later)
    database: str = Field(default="", alias='DATABASE')

    model_config = {
        'env_file': ['.env', 'green-route-akl/.env', 'backend/.env'],
        'extra': 'ignore',
        'env_file_encoding': 'utf-8'
    }


# Let pydantic-settings automatically load from .env file
settings = Settings()
