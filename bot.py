from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Hi saro iam welcome messanger bot 
Add me to your group 
 

  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} , Welcome to ln support Thank you for Joining

 Hey 😊{NAME} How are you?😉

Welcome to our {GROUPNAME}

{NAMESURNAME}

{LANG} Are you Tamil English?

{TIME}  {DATE}

Chat friendly and decent 😇with each other....💕😍

neega time pass,fake na Intha group set aakadhu 😂 poolam neega

One sec Inga girls pm la disturb panna kootadhu 🤬

Be decent 😇')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
