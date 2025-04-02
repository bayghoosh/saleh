import os
from telegram.ext import Application, CommandHandler
from telegram.error import Conflict

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise RuntimeError("توکن ربات تنظیم نشده!")

async def start(update, context):
    await update.message.reply_text('سلام! به ربات خوش آمدید!')

def main():
    try:
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        print("✅ ربات در حال راه‌اندازی...")
        app.run_polling(drop_pending_updates=True)  # این خط را اضافه کنید
        
    except Conflict as e:
        print("⚠️ خطا: یک نمونه دیگر از ربات در حال اجراست!")
        print(e)
    except Exception as e:
        print("❌ خطای غیرمنتظره:")
        print(e)

if __name__ == "__main__":
    main()
