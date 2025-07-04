import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()  # Завантажити змінні з .env файлу

# Отримуємо токен з середовища
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

# Створюємо застосунок (бота)
app = ApplicationBuilder().token(TOKEN).build()

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот працює!")

# Додаємо обробник до застосунку
app.add_handler(CommandHandler("start", start))

# Запускаємо бота
app.run_polling()
