import logging

from telegram.ext import Updater, CommandHandler

from planchet_bot.common.views import get_chat_id, start
from planchet_bot.dependencies import get_settings
from planchet_bot.weather.views import get_weather

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

settings = get_settings()
updater = Updater(
    token=settings.telegram_bot_token,
    use_context=True
)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('chat_id', get_chat_id))
dispatcher.add_handler(CommandHandler('weather', get_weather))
