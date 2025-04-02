from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7645753318:AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ÇÑÓÇá íÇã ÎæÔÂãÏæíí åäÇã ÏÑíÇİÊ ÏÓÊæÑ /start"""
    user = update.effective_user
    await update.message.reply_text(f"ÓáÇã {user.first_name}!\nÈå ÑÈÇÊ ãÇ ÎæÔ ÂãÏíÏ! ??")

async def handle_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ÎæÔÂãÏæíí Èå ÇÚÖÇí ÌÏíÏ"""
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"ÓáÇã {member.first_name}!\n"
            "Èå ÌãÚ ãÇ ÎæÔ ÂãÏí! ??\n"
            "ÈÑÇí ÔÑæÚ ÇÒ ÏÓÊæÑ /start ÇÓÊİÇÏå ˜ä."
        )

def main():
    """ÊäÙíã æ ÑÇåÇäÏÇÒí ÑÈÇÊ"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    # ËÈÊ åäÏáÑåÇ
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_members))
    
    print("? ÑÈÇÊ İÑæÔ ÏÑ ÍÇá ÇÌÑÇÓÊ...")
    app.run_polling()

if name == "main":
    main()