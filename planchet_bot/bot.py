from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from planchet_bot.project.settings import settings


updater = Updater(
    token=settings.TELEGRAM_BOT_TOKEN,
    use_context=True
)
dispatcher = updater.dispatcher
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm at your service, sir."
    )


def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=f"Id of this chat is {chat_id}"
    )


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('get_chat_id', get_chat_id))
