from environs import Env
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackContext

from dialogflow_api import detect_intent_texts


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')


def response(update: Update, context: CallbackContext):
    project_id = env('DF_PROJECT_ID')
    text = update.message.text
    session_id = update.message.chat_id
    response_text = detect_intent_texts(project_id, session_id, text)
    update.message.reply_text(response_text)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_bot_api_key = env('TG_BOT_APIKEY')
    updater = Updater(tg_bot_api_key)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, response)
    )
    updater.start_polling()
    updater.idle()
