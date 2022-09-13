from planchet_bot import dependencies
from planchet_bot.dependencies import get_weather_service
from telegram import Update
from telegram.ext import CallbackContext


settings = dependencies.get_settings()


def get_weather(update: Update, context: CallbackContext):
    weather_service = get_weather_service()
    weather = weather_service.get(
        lat=settings.weather_api.location_lat,
        lon=settings.weather_api.location_lon,
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
