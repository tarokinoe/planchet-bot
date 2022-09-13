import os

from pydantic import BaseSettings, BaseModel


class WeatherApiSettings(BaseModel):
    base_url: str
    token: str
    location_lat: str
    location_lon: str


class Settings(BaseSettings):
    telegram_bot_token: str
    weather_api: WeatherApiSettings

    class Config:
        env_nested_delimiter = '__'
        env_file_encoding = 'utf-8'
        env_file = os.getenv('ENV_PATH')
