from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7365551738:AAFh4oF9RVOfiLFpAIlG9xebYL1ILzTTe9c"
SHORT_LINK = "ضع_رابط_الاختصار_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📌 لمشاهدة الفيديو المطلوب، اضغط هنا:\n\n{SHORT_LINK}\n\n"
        f"⚠️ الرابط محمي، تأكد من تخطي الخطوات حتى تصل للمقطع."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
