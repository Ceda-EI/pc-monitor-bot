# Create a new bot by messaging @BotFather and follow the instructions
# Replace the key by the actual token recieved from BotFather
api_key = "123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# User ID of the user allowed to use the bot. Replace 123456789 with
# your own user id.
master_id = 123456789

# Command to lock the screen. Replace the command with actual command.
lock = "xautolock -locknow"

# Command to check if it is running to see if the screen is locked
# Put the name of process that is running only when the screen is
# locked.
lock_process = "i3lock"

# Lock and unlock message. The date is parsed according to strftime.
# Check man strftime or http://strftime.org/
lock_message = "You have locked your system - %c"
unlock_message = "You have unlocked your system - %c"
