from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7920334174:AAE4j_jp4F3gz-NtiGdiUewhXhebCHePtAA"

products = {
    "LM393": "ماژول تشخیص نور LM393 - 2€",
    "Arduino Nano": "برد آردوینو نانو - 8€",
    "ESP32": "برد ESP32-CAM - 12€"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(p, callback_data=p)] for p in products]
    await update.message.reply_text("📦 لیست قطعات موجود:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    item = query.data
    await query.edit_message_text(f"✅ {products[item]}\nبرای سفارش پیام بده: @YourSupportID")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
