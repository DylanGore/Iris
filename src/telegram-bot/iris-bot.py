#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    if(checkUser(update)):
        update.message.reply_text('Welcome to Iris Bot')


def help(bot, update):
    """Send a message when the command /help is issued."""
    if(checkUser(update)):
        update.message.reply_text('Help!')
    else:
        update.message.reply_text('You do not have permission to use this bot!')

def checkUser(update):
    username = update.message.from_user.username
    admin = "DylanGore"
    print('[IrisBot] Checking username - ' + username)

    if username == admin:
        allowed_user = True
        print('[IrisBot] User Allowed')
    else:
        allowed_user = False
        print('[IrisBot] User Denied')
    
    return allowed_user

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("BOT_TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
