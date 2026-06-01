 from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN ="8903643822:AAG8yp9ejdnF1yPV0lZR8hxpgB-MsfAvzZQ"

contracts = {
    "amz123": {
        "name": "محمد أحمد سالم",
        "phone": "0914800555",
        "package": "Home 20 Mbps",
        "expire": "15/06/2026",
    },
    "ahmed": {
        "name": "أحمد علي",
        "phone": "0921234567",
        "package": "Home 40 Mbps",
        "expire": "20/07/2026",
    },
}

user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 معلومات العقد"],
        ["📅 تجديد الاشتراك"],
        ["🔄 تغيير الباقة"],
        ["💳 الفواتير"],
        ["📞 التواصل معنا"],
    ]

    await update.message.reply_text(
        "🤖 أمازون ليبيا للاتصالات والتقنية\n\nاختر الخدمة المطلوبة:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # معلومات العقد
    if text == "📄 معلومات العقد":
        user_state[user_id] = "contract_info"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    # الفواتير
    if text == "💳 الفواتير":
        user_state[user_id] = "invoice"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    # تغيير الباقة
    if text == "🔄 تغيير الباقة":
        user_state[user_id] = "change_package"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    # تجديد الاشتراك
    if text == "📅 تجديد الاشتراك":
        user_state[user_id] = "renew"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    # التواصل
    if text == "📞 التواصل معنا":
        await update.message.reply_text(
            "📱 0914800555\n"
            "🌐 amznet.ly\n"
            "🏢 أمازون ليبيا للاتصالات والتقنية"
        )
        return

    state = user_state.get(user_id)

    # التحقق من العقد
    if state in ["contract_info", "invoice", "change_package", "renew"]:

        contract = contracts.get(text.lower())

        if not contract:
            await update.message.reply_text(
                "❌ اسم العقد غير موجود."
            )
            return

        if state == "contract_info":
            await update.message.reply_text(
                f"👤 الاسم: {contract['name']}\n"
                f"🆔 العقد: {text}\n"
                f"📱 الهاتف: {contract['phone']}\n"
                f"📶 الباقة: {contract['package']}\n"
                f"📅 الانتهاء: {contract['expire']}\n"
                f"🟢 الحالة: نشط"
            )

        elif state == "invoice":
            await update.message.reply_text(
                "💳 الفواتير\n\n"
                "فاتورة مايو\n"
                "60 دينار\n"
                "✅ مدفوعة\n\n"
                "فاتورة يونيو\n"
                "60 دينار\n"
                "❌ غير مدفوعة"
            )

        elif state == "change_package":
            await update.message.reply_text(
                "🔄 الباقات المتاحة\n\n"
                "🏠 Home 20 Mbps\n"
                "🏠 Home 40 Mbps\n"
                "🏠 Home 60 Mbps\n\n"
                "✅ تم إرسال طلب تغيير الباقة."
            )

        elif state == "renew":
            await update.message.reply_text(
                "📅 التجديد\n\n"
                "شهر واحد - 60 دينار\n"
                "3 أشهر - 170 دينار\n"
                "6 أشهر - 330 دينار\n\n"
                "✅ تم استلام طلب التجديد."
            )

        user_state.pop(user_id, None)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

print("Bot Running...")
app.run_polling()
