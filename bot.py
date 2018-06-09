from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater('570628271:AAHCL6flFm6Esel-idnSqLDrVEUX1Ucd2Dc')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

main()
