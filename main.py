import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1416864887:AAG7eJIcQXlfmKqCbfwhmI0aQhDBkgUOGn0"


def start(bot, update):
    print(update)
    author = update.message.from_user.first_name
    reply = f"Hi! {author}"
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def _help(bot, update):
    reply = "this is a help message"
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def echo_text(bot, update):
    print(update)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def echo_sticker(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.sticker.file_id)


def error(bot, update):
    logger.error("error")


updater = Updater(TOKEN, use_context=False)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", _help))
dp.add_handler(MessageHandler(Filters.text, echo_text))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))

updater.start_polling()
logger.info("started polling...")
updater.idle()
