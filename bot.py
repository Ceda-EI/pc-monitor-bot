#!/usr/bin/env python3

import logging
import telegram
import os
import subprocess
import psutil
from telegram.ext import Updater, CommandHandler

try:
    import config
except ImportError:
    print("Missing Config. Exiting.")
    exit()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                    %(message)s', level=logging.INFO)


def check_user(bot, update):
    chat_id = update.message.chat_id
    if chat_id != config.master_id:
        text = "You need to host your own instance! Source: \
                https://gitlab.com/ceda_ei/pc-monitor-bot"
        bot.send_message(chat_id=chat_id, text=text)
        return False
    return True


def start(bot, update):
    if not check_user(bot, update):
        return False
    chat_id = update.message.chat_id
    custom_keyboard = [['/state', '/screenshot'], ['/lock', '/video']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id,  text="What to do?",
                     reply_markup=reply_markup)


def get_screenshot():
    try:
        stdout = subprocess.check_output(["./screenshot.sh"])
        return stdout.decode('UTF-8')
    except subprocess.CalledProcessError:
        return False


def screenshot(bot, update):
    if not check_user(bot, update):
        return False
    screenshot = get_screenshot()
    chat_id = update.message.chat_id
    if not screenshot:
        bot.send_message(chat_id=chat_id, text="Failed to take a screenshot.")
        return
    bot.send_document(chat_id=chat_id, document=open(screenshot, 'rb'))
    os.remove(screenshot)


def lock(bot, update):
    if not check_user(bot, update):
        return False
    command = config.lock.split()
    exitcode = subprocess.call(command)
    chat_id = update.message.chat_id
    # Only send message if command fails because another script will send the
    # message on successful lock
    if exitcode != 0:
        bot.send_message(chat_id=chat_id, text="Command failed.")


def check_if_running(process_name):
    for i in psutil.process_iter():
        if i.name() == process_name:
            return True
    return False


def state(bot, update):
    if not check_user(bot, update):
        return False
    chat_id = update.message.chat_id
    if check_if_running(config.lock_process):
        bot.send_message(chat_id=chat_id, text="Locked.")
    else:
        bot.send_message(chat_id=chat_id, text="Unlocked.")


updater = Updater(token=config.api_key)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

screenshot_handler = CommandHandler('screenshot', screenshot)
dispatcher.add_handler(screenshot_handler)

lock_handler = CommandHandler('lock', lock)
dispatcher.add_handler(lock_handler)

state_handler = CommandHandler('state', state)
dispatcher.add_handler(state_handler)

updater.start_polling()
