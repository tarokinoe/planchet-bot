from planchet_bot.dependencies import get_weather_service
from planchet_bot.project.settings import settings
from telegram import Update
from telegram.ext import CallbackContext


def get_weather(update: Update, context: CallbackContext):
    weather_service = get_weather_service()
    weather = weather_service.get(
        lat=settings.WEATHER['location_lat'],
        lon=settings.WEATHER['location_lon'],
    )
    current = weather.current
    today = weather.daily[0]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""Current
{current.temp} °C {current.weather[0].emoji} ({current.weather[0].description})

Today
{today.temp.day} °C {today.weather[0].emoji} ({today.weather[0].description})
"""
    )
