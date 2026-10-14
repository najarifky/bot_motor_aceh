import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("8298915888:AAH0jBRnZ3F0cYFiCzOTvZpG4r1i5FnzZPE")

DATA_MOTOR = {
    "beat": "Beat 2019: 12jt\nBeat 2020: 13.5jt\nBeat Street 2021: 14jt",
    "vario": "Vario 125 2020: 16jt\nVario 150 2021: 20jt",
    "scoopy": "Scoopy 2020: 15jt\nScoopy 2021: 16.5jt",
    "pcx": "PCX 2020: 23jt\nPCX 160 2022: 29jt"
}

TIKTOK_LINK = "https://www.tiktok.com/@batas_lintas9"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Beat", "Vario"], ["Scoopy", "PCX"], ["Lokasi", "TikTok"]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Halo bos! 👋\nCari motor apa?\n\nKetik nama motor atau pilih tombol di bawah.\nKetik /tiktok buat liat video stok.",
        reply_markup=markup
    )

async def tiktok_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Cek video stok terbaru di TikTok kita bro! 🎥\n\n👉 {TIKTOK_LINK}\n\nFollow biar gak ketinggalan motor baru masuk!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "tiktok" in text or "tt" in text or "video" in text:
        await update.message.reply_text(f"Cek TikTok kita bro! 🎥\n{TIKTOK_LINK}")
    elif "lokasi" in text:
        await update.message.reply_text("📍 Lokasi: Bungkaih, Aceh.\nBisa COD Muara Satu & sekitar Lhokseumawe.")
    elif "nego" in text or "harga" in text:
        await update.message.reply_text("Bisa nego bos! Langsung cek barang ke lokasi aja.")
    else:
        found = False
        for key, val in DATA_MOTOR.items():
            if key in text:
                await update.message.reply_text(f"Stok {key.upper()}:\n{val}\n\nLihat videonya di TikTok: {TIKTOK_LINK}")
                found = True
                break
        if not found:
            await update.message.reply_text("Motornya belum ada bos. Coba ketik: Beat, Vario, Scoopy, PCX atau TikTok")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tiktok", tiktok_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
