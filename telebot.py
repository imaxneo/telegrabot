from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ضع_توكن_البوت_هنا"
SHORT_LINK = "ضع_رابط_الاختصار_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📌 لمشاهدة الفيديو المطلوب، اضغط هنا:\n\n{SHORT_LINK}\n\n"
        f"⚠️ الرابط محمي، تأكد من تخطي الخطوات حتى تصل للمقطع."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
