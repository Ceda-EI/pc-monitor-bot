#!/usr/bin/env python3

import logging
import telegram
from telegram.ext import Updater, CommandHandler

try:
    import config
except ImportError:
    print("Missing Config. Exiting.")
    exit()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                    %(message)s', level=logging.INFO)


def start(bot, update):
    chat_id = update.message.chat_id
    if chat_id != config.master_id:
        text = "You need to host your own instance! \ Source: \
                https://gitlab.com/ceda_ei/pc-monitor-bot"
        bot.send_message(chat_id=chat_id, text=text)
        return

    custom_keyboard = [['/state', '/screenshot'], ['/lock', '/video']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id,  text="What to do?",
                     reply_markup=reply_markup)


updater = Updater(token=config.api_key)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
