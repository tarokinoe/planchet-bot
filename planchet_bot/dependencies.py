from typing import Optional

from planchet_bot.project.settings.settings import Settings
from planchet_bot.weather.weather_service import WeatherService


_weather_service: Optional[WeatherService] = None
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    global _settings
    if not _settings:
        _settings = Settings()

    return _settings


def get_weather_service() -> WeatherService:
    global _weather_service
    if not _weather_service:
        settings = get_settings()
        _weather_service = WeatherService(
            base_url=settings.weather_api.base_url,
            token=settings.weather_api.token
        )

    return _weather_service
