from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from const import TOKEN
from func import *

u=Updater(token=TOKEN, workers=4)
d=u.dispatcher
d.add_handler(CommandHandler('start',callback=start, run_async=True))
d.add_handler(MessageHandler(Filters.text,callback=text_answer))
d.add_handler(MessageHandler(Filters.contact,callback=get_contact))
u.start_polling()