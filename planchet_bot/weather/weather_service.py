from typing import List

import requests
from pydantic.main import BaseModel


def fahrenheit_to_celsius(val):
    return (val - 32) * 5/9


WEATHER_EMOJI_MAP = {
    '01': '☀️',  # clear sky
    '02': '⛅️',  # few clouds
    '03': '☁️',  # scattered clouds
    '04': '☁️☁️',  # broken clouds
    '09': '🌧',  # shower rain
    '10': '🌦',  # rain
    '11': '🌩',  # thunderstorm
    '13': '🌨',  # snow
    '50': '🌫',  # mist
}


class Weather(BaseModel):
    main: str
    description: str
    icon: str

    @property
    def emoji(self):
        key = self.icon[:2]
        return WEATHER_EMOJI_MAP.get(key, self.description)


class Temperature(BaseModel):
    day: float
    min: float
    max: float


class CurrentWeather(BaseModel):
    temp: float
    weather: List[Weather]


class DailyWeather(BaseModel):
    temp: Temperature
    weather: List[Weather]


class WeatherInfo(BaseModel):
    current: CurrentWeather
    daily: List[DailyWeather]


class WeatherService:
    def __init__(self, base_url: str, token: str):
        self._base_url = base_url
        self._token = token

    def get(self, lat: str, lon: str) -> WeatherInfo:
        url = self._base_url + '/onecall'
        params = {
            'lat': lat, 'lon': lon, 'appid': self._token, 'units': 'metric'
        }
        response = requests.get(url, params=params)
        data = response.json()
        weather_info = WeatherInfo(**data)
        return weather_info
