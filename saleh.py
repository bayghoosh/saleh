# -*- coding: utf-8 -*-
import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot token
YOUTUBE_CHANNEL = "https://www.youtube.com/@TebeAtfal"

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        try:
            welcome_text = (
                f"🌟 Welcome {member.first_name}!\n\n"
                f"📺 Please subscribe to our YouTube channel:\n"
                f"{YOUTUBE_CHANNEL}\n\n"
                "Thank you for joining us! ❤️"
            )
            await update.message.reply_text(welcome_text)
        except Exception as e:
            logger.error(f"Error in welcome message: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    
    logger.info("✅ Bot is running and ready to welcome new members")
    app.run_polling()

if __name__ == "__main__":
    main()
