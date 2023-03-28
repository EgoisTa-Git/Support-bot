from functools import partial

from environs import Env
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, CallbackContext

from dialogflow_api import detect_intent_texts


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте!')


def reply_on_message(update: Update, context: CallbackContext, project_id):
    text = update.message.text
    session_id = update.message.chat_id
    response = detect_intent_texts(project_id, session_id, text)
    update.message.reply_text(response.query_result.fulfillment_text)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    tg_bot_api_key = env('TG_BOT_APIKEY')
    project_id = env('DF_PROJECT_ID')
    reply_on_message_partial = partial(reply_on_message, project_id=project_id)
    updater = Updater(tg_bot_api_key)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            reply_on_message_partial,
        )
    )
    updater.start_polling()
    updater.idle()
