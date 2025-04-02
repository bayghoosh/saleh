import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# تنظیمات پایه
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# مدیریت دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"سلام {user.mention_html()}! 👋\n"
        "من یک ربات پایه هستم.\n"
        "دستورات موجود:\n"
        "/start - نمایش این پیام\n"
        "/help - راهنمایی\n"
        "/about - درباره ربات"
    )

# مدیریت دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📚 <b>راهنمای ربات</b>:

/start - شروع کار با ربات
/help - نمایش این پیام
/about - اطلاعات فنی ربات

🔹 هر پیامی بفرستید، آن را بازمی‌گردانم!
"""
    await update.message.reply_html(help_text)

# مدیریت پیام‌های متنی
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"شما نوشتید: {update.message.text}")

# مدیریت خطاها
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"خطا رخ داد: {context.error}")
    if update and hasattr(update, 'message'):
        await update.message.reply_text("⚠️ خطایی رخ داد! لطفاً بعداً تلاش کنید.")

def main():
    # ایجاد نمونه ربات
    application = (
        Application.builder()
        .token(os.getenv("BOT_TOKEN"))
        .build()
    )

    # ثبت دستورات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # ثبت handler پیام‌های معمولی
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        echo
    ))

    # ثبت مدیریت خطا
    application.add_error_handler(error_handler)

    # راه‌اندازی ربات
    logger.info("✅ ربات در حال راه‌اندازی...")
    application.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES
    )

if __name__ == "__main__":
    main()
