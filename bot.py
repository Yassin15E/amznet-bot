from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8903643822:AAG8yp9ejdnF1yPV0lZR8hxpgB-MsfAvzZQ"

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
    "amazon": {
        "name": "مستخدم تجريبي",
        "phone": "0911111111",
        "package": "Home 60 Mbps",
        "expire": "01/08/2026",
    }
}

user_state = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 معلومات العقد"],
        ["💳 الفواتير"],
        ["📅 تجديد الاشتراك"],
        ["🔄 تغيير الباقة"],
        ["📞 التواصل معنا"],
    ]

    await update.message.reply_text(
        "🤖 أمازون ليبيا للاتصالات والتقنية\n\nاختر الخدمة المطلوبة:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if text == "📄 معلومات العقد":
        user_state[user_id] = "contract"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    if text == "💳 الفواتير":
        user_state[user_id] = "invoice"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    if text == "📅 تجديد الاشتراك":
        user_state[user_id] = "renew"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    if text == "🔄 تغيير الباقة":
        user_state[user_id] = "package"
        await update.message.reply_text("✍️ أدخل اسم العقد:")
        return

    if text == "📞 التواصل معنا":
        await update.message.reply_text(
            "📱 0914800555\n"
            "🌐 amznet.ly\n"
            "🏢 أمازون ليبيا للاتصالات والتقنية"
        )
        return

    state = user_state.get(user_id)

    if state:
        contract = contracts.get(text.lower())

        if not contract:
            await update.message.reply_text(
                "❌ اسم العقد غير موجود."
            )
            return

        if state == "contract":
            await update.message.reply_text(
                f"👤 الاسم: {contract['name']}\n"
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

        elif state == "renew":
            await update.message.reply_text(
                "📅 تم استلام طلب التجديد\n\n"
                "مدة التجديد: شهر واحد\n"
                "القيمة: 60 دينار\n\n"
                "✅ تم تسجيل الطلب."
            )

        elif state == "package":
            await update.message.reply_text(
                "🔄 الباقات المتاحة\n\n"
                "🏠 Home 20 Mbps\n"
                "🏠 Home 40 Mbps\n"
                "🏠 Home 60 Mbps\n\n"
                "✅ تم إرسال طلب تغيير الباقة."
            )

        user_state.pop(user_id, None)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
