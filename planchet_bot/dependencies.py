from typing import Optional

from planchet_bot.project.settings import settings
from planchet_bot.weather.weather_service import WeatherService


_weather_service: Optional[WeatherService] = None


def get_weather_service():
    global _weather_service
    if not _weather_service:
        _weather_service = WeatherService(
            base_url=settings.WEATHER['api_base_url'],
            token=settings.WEATHER['api_token']
        )

    return _weather_service
