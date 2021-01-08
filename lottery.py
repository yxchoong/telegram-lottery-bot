import logging
import traceback
import html
import json
import random

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
          update.message.reply_text('Are you ready for some luck?\n \nUse /toto or /4d to generate your lottery numbers!\n\nClick /news for latest lottery updates or /sgpools to redirect to SGPools website!')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Use /toto or /4d to generate your lottery numbers!\n\nClick /news for latest lottery updates or /sgpools to redirect to SGPools website!')
    
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = ''.join(tb_list)
    message = (
        f'An exception was raised while handling an update\n'
        f'<pre>update = {html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False))}'
        '</pre>\n\n'
        f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
        f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
        f'<pre>{html.escape(tb_string)}</pre>'
    )
    
    
def toto(update: Update, context: CallbackContext) -> None:
    number = random.sample(range(1, 50), 6)
    no = str(number[0])
    for i in range(1, len(number)):
        no += ' ' + str(number[i])
    chat_id = update.message.chat_id
    update.message.reply_text("Here are your 6 lucky TOTO numbers!\n \n" + no)
    return

def fourd(update: Update, context: CallbackContext) -> None:
    number = random.sample(range(0, 10), 4)
    no = ''
    for i in number:
        no += str(i)
    chat_id = update.message.chat_id
    update.message.reply_text("Huat ah!\n \n" + no)
    return

def news(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Link to CNA Singapore Pools News:\n\nhttps://www.channelnewsasia.com/news/topic/singapore-pools")
    return 

def sgpools(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Link to Singapore Pools portal:\n\nhttps://www.singaporepools.com.sg/landing/en/Pages/index.html")
    return 
    
def main():
    updater = Updater('1593199777:AAHWnaJy7vCdHioKag86V3SPMzDMzt5kE8w', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("toto", toto))
    dp.add_handler(CommandHandler("4d", fourd))
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(CommandHandler("sgpools", sgpools))
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    main()
