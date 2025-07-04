import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Привіт! Я бот ✅")

app.add_handler(CommandHandler("start", start))
app.run_polling()
