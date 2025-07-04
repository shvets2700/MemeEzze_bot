import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # Витягуємо токен з середовища

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не встановлений у середовищі!")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Привіт! Бот працює!")

app.add_handler(CommandHandler("start", start))
app.run_polling()

