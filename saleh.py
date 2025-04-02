import os
from telegram.ext import Application, CommandHandler  # <-- این خط را اصلاح کنید

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise RuntimeError("توکن ربات تنظیم نشده! لطفاً متغیر BOT_TOKEN را تنظیم کنید.")

async def start(update, context):
    await update.message.reply_text('سلام! به ربات خوش آمدید!')

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))  # حالا دیگر خطا نمی‌دهد
    
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
