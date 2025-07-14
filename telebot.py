import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🟢 سحب المتغيرات الحساسة من بيئة التشغيل (Render)
TOKEN = os.environ.get("TOKEN")
SHORT_LINK = os.environ.get("SHORT_LINK")

# 🟣 رسالة الترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📌 لمشاهدة الفيديو المطلوب، اضغط هنا:\n\n{SHORT_LINK}\n\n"
        f"⚠️ الرابط محمي، تأكد من تخطي الخطوات حتى تصل للمقطع.",
        disable_web_page_preview=True
    )

# 🧠 إعداد البوت وتشغيله
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
