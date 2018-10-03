#!/usr/bin/env python3

import telegram
import sys
import datetime

try:
    import config
except ImportError:
    print("Missing Config. Exiting.")
    exit()

bot = telegram.Bot(token=config.api_key)

if len(sys.argv) != 2:
    print("Invalid number of parameters")
    exit(1)

arg = sys.argv[1]
if arg == "lock":
    today = datetime.datetime.today()
    text = today.strftime(config.lock_message)
    bot.send_message(chat_id=config.master_id, text=text)
elif arg == "unlock":
    today = datetime.datetime.today()
    text = today.strftime(config.lock_message)
    bot.send_message(chat_id=config.master_id, text=text)
else:
    print("Wrong parameter. Exiting.")
    exit(1)
