from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8903643822:AAG8yp9ejdnF1yPV0lZR8hxpgB-MsfAvzZQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 معلومات العقد"],
        ["💳 الفواتير"],
        ["📞 التواصل معنا"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🤖 أمازون ليبيا للاتصالات والتقنية\n\nاختر الخدمة المطلوبة:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📄 معلومات العقد":
        await update.message.reply_text(
            "👤 الاسم: محمد أحمد سالم\n"
            "🆔 العقد: amz123\n"
            "📱 الهاتف: 0914800555\n"
            "📶 الباقة: Home 20 Mbps\n"
            "🟢 الحالة: نشط"
        )

    elif text == "💳 الفواتير":
        await update.message.reply_text(
            "فاتورة مايو\n"
            "60 دينار\n"
            "✅ مدفوعة\n\n"
            "فاتورة يونيو\n"
            "60 دينار\n"
            "❌ غير مدفوعة"
        )

    elif text == "📞 التواصل معنا":
        await update.message.reply_text(
            "📱 0914800555\n"
            "🌐 amznet.ly\n"
            "🏢 أمازون ليبيا للاتصالات والتقنية"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
