from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8903643822:AAG8yp9ejdnF1yPV0lZR8hxpgB-MsfAvzZQ"

MAIN_MENU = [
    ["👤 حسابي", "💳 تجديد الاشتراك"],
    ["📦 تغيير الباقة", "💰 الرصيد"],
    ["🎫 شحن كرت", "🧾 الفواتير"],
    ["📊 الاستهلاك", "⚡ اختبار السرعة"],
    ["🛠 الدعم الفني", "🎁 العروض الحالية"],
    ["📡 الأبراج والتغطية", "📞 تواصل معنا"],
    ["⚙️ الإعدادات"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        MAIN_MENU,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🤖 مرحباً بك في نظام أمازون ليبيا للاتصالات والتقنية\n\n"
        "اختر الخدمة المطلوبة:",
        reply_markup=keyboard
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 حسابي":
        await update.message.reply_text(
            "👤 بيانات الحساب\n\n"
            "الاسم: محمد أحمد\n"
            "رقم العقد: A12345\n"
            "رقم الهاتف: 0912345678\n"
            "المدينة: طرابلس\n"
            "الباقة الحالية: أمازون 5 ميجا\n"
            "الرصيد: 45 دينار\n"
            "حالة الاشتراك: فعال\n"
            "تاريخ الانتهاء: 2026/07/15"
        )

    elif text == "💳 تجديد الاشتراك":
        await update.message.reply_text(
            "✅ تم تجديد الاشتراك بنجاح لمدة شهر.\n\n"
            "تاريخ الانتهاء الجديد: 2026/08/15"
        )

    elif text == "📦 تغيير الباقة":
        await update.message.reply_text(
            "📦 تم تغيير الباقة إلى أمازون 10 ميجا بنجاح."
        )

    elif text == "💰 الرصيد":
        await update.message.reply_text(
            "💰 رصيدك الحالي: 45 دينار"
        )

    elif text == "🎫 شحن كرت":
        await update.message.reply_text(
            "✅ تم شحن 10 دينار بنجاح."
        )

    elif text == "🧾 الفواتير":
        await update.message.reply_text(
            "🧾 آخر الفواتير\n\n"
            "فاتورة مايو: مدفوعة\n"
            "فاتورة يونيو: غير مدفوعة"
        )

    elif text == "📊 الاستهلاك":
        await update.message.reply_text(
            "📊 الاستهلاك الحالي\n\n"
            "التحميل: 780 GB\n"
            "الرفع: 95 GB\n"
            "نسبة الاستخدام: 78%"
        )

    elif text == "⚡ اختبار السرعة":
        await update.message.reply_text(
            "⚡ نتيجة الاختبار\n\n"
            "Download: 48 Mbps\n"
            "Upload: 12 Mbps\n"
            "Ping: 18 ms"
        )

    elif text == "🛠 الدعم الفني":
        await update.message.reply_text(
            "🎫 تم فتح تذكرة دعم\n"
            "رقم التذكرة: #58241"
        )

    elif text == "🎁 العروض الحالية":
        await update.message.reply_text(
            "🎁 العروض الحالية\n\n"
            "• خصم 20% على اشتراك 6 أشهر\n"
            "• شهر مجاني عند الاشتراك السنوي"
        )

    elif text == "📡 الأبراج والتغطية":
        await update.message.reply_text(
            "📡 الأبراج المتاحة\n\n"
            "طرابلس: ممتازة\n"
            "مصراتة: جيدة جداً\n"
            "الزاوية: جيدة"
        )

    elif text == "📞 تواصل معنا":
        await update.message.reply_text(
            "☎️ خدمة العملاء\n\n"
            "0910000000\n"
            "support@amazon.ly"
        )

    elif text == "⚙️ الإعدادات":
        await update.message.reply_text(
            "⚙️ الإعدادات\n\n"
            "• تغيير اللغة\n"
            "• الإشعارات\n"
            "• تسجيل الخروج"
        )

    else:
        await update.message.reply_text(
            "اختر خياراً من القائمة."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            messages
        )
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
