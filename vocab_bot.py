from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "7633243613:AAGDrXirTcPYotF17SgHQAZQPEI78NbEFUQ"

vocab = {
    "Maaf": "Sorry",
    "Permisi": "Excuse me",
    "Tolong": "Help",
    "Maukah": "Would you like",
    "Bisakah": "Can you",
    "Gerah": "Hot",
    "Cuaca": "Weather",
    "Macet": "Jammed",
    "Sepi": "Quiet",
    "Ramai": "Noisy",
    "Pesan": "Message",
    "Menelepon": "Call",
    "Sibuk": "Busy",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Ketik /quiz untuk memulai kuis kosakata.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah:\n/start - Mulai bot\n/quiz - Kuis\n/answer [jawaban] - Jawabanmu")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word, meaning = random.choice(list(vocab.items()))
    context.user_data["current_word"] = word
    await update.message.reply_text(f"Apa arti dari kata: '{word}'?\n(Jawab pakai: /answer ... )")

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Contoh: /answer help")
        return

    user_input = ' '.join(context.args).strip().lower()
    current_word = context.user_data.get("current_word")

    if not current_word:
        await update.message.reply_text("Ketik /quiz dulu untuk memulai.")
        return

    correct = vocab[current_word].lower()
    if user_input == correct:
        await update.message.reply_text("✅ Benar!")
    else:
        await update.message.reply_text(f"❌ Salah. Jawaban yang benar: {vocab[current_word]}")

    context.user_data["current_word"] = None

# --- START ---
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("answer", answer))

print("✅ Bot is running...")
app.run_polling()
