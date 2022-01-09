from telegram import Update
from telegram.ext import CallbackContext


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
