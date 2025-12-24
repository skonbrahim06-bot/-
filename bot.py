import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8546373941:AAFdssG_rOfHLiqx3j9KO-lNzaAI96VbWZc")  # أفضل طريقة لاستخدام التوكن
DEVELOPER = "@C_R_B_X"
START_IMAGE = "https://www2.0zz0.com/2025/12/24/17/756941141.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != "private":
        return
    text = (
        "🐐 **أهلاً بك في بوت XC GOAT!**\n\n"
        "أنا بوت حماية وتسلية متطور، أساعدك في إدارة مجموعتك بكل سهولة وأمان.\n\n"
        "🛡 **مميزات البوت:**\n"
        "• حماية قوية ومتكاملة\n"
        "• أوامر إدارة كاملة\n"
        "• ألعاب وتسلية\n"
        "• ميزة البحث الموسيقي (يوتيوب)\n\n"
        "💡 **التشغيل:**\n"
        "أضفني مشرفاً ثم أرسل (تفعيل) داخل المجموعة.\n\n"
        "📌 اكتب **الأوامر** لعرض قائمة الأوامر."
    )
    keyboard = [
        [InlineKeyboardButton("➕ أضفني", url="https://t.me/XC_GOAT_BOT?startgroup=true")],
        [
            InlineKeyboardButton("🧑‍🔧 المطور الأساسي", url=f"https://t.me/{DEVELOPER.replace('@','')}"),
            InlineKeyboardButton("💎 شراء بوت", url=f"https://t.me/{DEVELOPER.replace('@','')}")
        ]
    ]
    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def activate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    member = await context.bot.get_chat_member(chat.id, user.id)
    if member.status not in ["administrator", "creator"]:
        await update.message.reply_text("❌ هذا الأمر للمشرفين فقط.")
        return
    group_name = chat.title
    keyboard = [[InlineKeyboardButton(f"✅ تم تفعيل: {group_name}", callback_data="activated")]]
    await update.message.reply_text(
        f"🔥 **تم تفعيل بوت XC GOAT بنجاح!**\n\n"
        f"🏷 المجموعة: **{group_name}**\n"
        f"🛡 جميع أنظمة الحماية تعمل الآن.\n\n"
        f"📌 اكتب **الأوامر** لرؤية الأوامر.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return
    user_id = update.message.reply_to_message.from_user.id
    await context.bot.restrict_chat_member(update.effective_chat.id, user_id, ChatPermissions(can_send_messages=False))
    await update.message.reply_text("🔇 تم كتم العضو.")

async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return
    user_id = update.message.reply_to_message.from_user.id
    await context.bot.restrict_chat_member(update.effective_chat.id, user_id, ChatPermissions(can_send_messages=True))
    await update.message.reply_text("🔊 تم فك الكتم.")

async def anti_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "http" in update.message.text:
        await update.message.delete()

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("تفعيل", activate))
    app.add_handler(CommandHandler("كتم", mute))
    app.add_handler(CommandHandler("فك", unmute))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, anti_links))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
