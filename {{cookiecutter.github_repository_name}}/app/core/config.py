from functools import lru_cache

from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):
    SERVICE_NAME: str = ""


@lru_cache
def get_settings():
    return ServiceSettings()


service_settings = get_settings()
