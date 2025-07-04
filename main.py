import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Отримуємо токен з середовища
TOKEN = os.getenv("7995176267:AAFMhD79vq_DmYfMz7RZRpx7ID-algTdfBg")
if not TOKEN:
    raise ValueError("7995176267:AAFMhD79vq_DmYfMz7RZRpx7ID-algTdfBg")

# Створюємо застосунок (бота)
app = ApplicationBuilder().token(TOKEN).build()

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот працює!")

# Додаємо обробник до застосунку
app.add_handler(CommandHandler("start", start))

# Запускаємо бота
app.run_polling()
