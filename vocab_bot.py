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
    await update.message.reply_text("Halo! Ketik /quiz untuk mulai kuis.")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word, meaning = random.choice(list(vocab.items()))
    context.user_data["word"] = word
    await update.message.reply_text(f"Apa arti dari '{word}'? (Gunakan /answer)")

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Ketik /answer jawabanmu")
        return

    user_input = ' '.join(context.args).strip().lower()
    current_word = context.user_data.get("word")
    if not current_word:
        await update.message.reply_text("Gunakan /quiz dulu.")
        return

    correct = vocab[current_word].lower()
    if user_input == correct:
        await update.message.reply_text("✅ Benar!")
    else:
        await update.message.reply_text(f"❌ Salah. Jawaban benar: {vocab[current_word]}")
    context.user_data["word"] = None

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("answer", answer))
app.run_polling()
