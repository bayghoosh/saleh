# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7645753318:AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"سلام {user.first_name} عزیز! به ربات ما خوش آمدید!")
    
async def welcome_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"سلام {member.first_name}!\n"
            "به جمع ما خوش آمدی دوست عزیز!"
        )

def main():
    print("در حال راه اندازی ربات...")
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_members))
    
    print("✅ ربات آماده به کار است")
    app.run_polling()

if name == "saleh":
    main(saleh)
