import os
from telegram.ext import Application

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise RuntimeError("توکن ربات تنظیم نشده! لطفاً متغیر BOT_TOKEN را تنظیم کنید.")

async def start(update, context):
    await update.message.reply_text('سلام! به ربات خوش آمدید!')

def main():
    # ساخت Application با توکن واقعی
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
