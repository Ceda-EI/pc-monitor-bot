# PC-Monitor-Bot

A bot intended to check the state of your PC (screenshots and check if locked)

## Setup

+ Install `scrot`, `python3`, `pip3` using your package manager.
  + Arch Linux: `sudo pacman -S scrot python python-pip`
  + Debian: `sudo apt install python3 python3-pip scrot`
+ Install `python-telegram-bot`
  + System-wide installation: `pip3 install python-telegram-bot`
  + User installation: `pip3 install --user python-telegram-bot`
+ `git clone https://gitlab.com/ceda_ei/pc-monitor-bot`
+ `cd pc-monitor-bot`
+ Create a bot with [BotFather](https://t.me/BotFather)
+ Copy the sample config file and edit it
  + `cp sample.config.py config.py`
  + Edit `config.py` using a text editor
+ `python3 bot.py`
+ Add `python3 lock.py lock` and `python3 lock.py unlock` around your lock script to send messages when screen is locked and unlocked.
