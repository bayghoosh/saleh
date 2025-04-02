from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7645753318:AAFdnqvhJu-AhgRu0oAEYpSwv0N9UfwwfKE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """����� ���� ��ԝ��ϐ��� ���� ������ ����� /start"""
    user = update.effective_user
    await update.message.reply_text(f"���� {user.first_name}!\n�� ���� �� ��� �����! ??")

async def handle_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """��ԝ��ϐ��� �� ����� ����"""
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"���� {member.first_name}!\n"
            "�� ��� �� ��� ����! ??\n"
            "���� ���� �� ����� /start ������� ��."
        )

def main():
    """����� � ��������� ����"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    # ��� �������
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_new_members))
    
    print("? ���� ���� �� ��� ������...")
    app.run_polling()

if name == "main":
    main()