from telegram import Update
from telegram.ext import Updater, Filters, CallbackContext, MessageHandler
from dotenv import load_dotenv
from os import getenv
from models import RabbitMQ
load_dotenv()
token = getenv("telegram_access_token")
chosen_chat_id = getenv("chosen_chat_id")

def text_messages_handler(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.message.chat.id
    if str(chat_id) == str(chosen_chat_id):
        RabbitMQ().send_text_message(text)



updater = Updater(token)

updater.dispatcher.add_handler(MessageHandler(Filters.text, text_messages_handler))

updater.start_polling()
updater.idle()