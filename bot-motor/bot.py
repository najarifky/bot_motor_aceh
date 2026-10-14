import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8298915888:AAH0jBRnZ3F0cYFiCzOTvZpG4r1i5FnzZPE"
TIKTOK_LINK = "https://www.tiktok.com/@batas_lintas9?_r=1&_t=ZS-9AY4QMGZnm8"

KATALOG = {
    "beat": [
        {"nama": "Spion Click Beat", "harga": "Rp 45.000", "desk": "Spion model click, drat Honda, PNP Beat"},
        {"nama": "Cover Knalpot Beat", "harga": "Rp 85.000", "desk": "Carbon glossy, anti panas"},
        {"nama": "Karpet Beat Deluxe", "harga": "Rp 60.000", "desk": "Bahan karet tebal"},
    ],
    "vario": [
        {"nama": "Visor Vario 160 Smoke", "harga": "Rp 120.000", "desk": "Model jenong, smoke"},
        {"nama": "Mudflap Vario", "harga": "Rp 35.000", "desk": "Penahan lumpur"},
    ],
    "nmax": [
        {"nama": "Bracket Plat NMAX Old", "harga": "Rp 55.000", "desk": "Besi tebal, chrome"},
        {"nama": "Cover Radiator NMAX", "harga": "Rp 95.000", "desk": "Variasi CNC"},
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛵 BEAT", callback_data="beat")],
        [InlineKeyboardButton("🏍️ VARIO", callback_data="vario")],
        [InlineKeyboardButton("📦 NMAX", callback_data="nmax")],
        [InlineKeyboardButton("🎥 TikTok Kami - batas_lintas9", url=TIKTOK_LINK)],
    ]
    text = "Halo bro! Selamat datang di Katalog Motor Aceh 🏍️\n\nMau cari aksesoris apa? Pilih di bawah 👇"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data in KATALOG:
        keyboard = []
        for i, p in enumerate(KATALOG[data]):
            keyboard.append([InlineKeyboardButton(f"{p['nama']} - {p['harga']}", callback_data=f"detail_{data}_{i}")])
        keyboard.append([InlineKeyboardButton("🎥 TikTok Kami", url=TIKTOK_LINK)])
        keyboard.append([InlineKeyboardButton("⬅️ Kembali", callback_data="kembali")])
        await query.edit_message_text(f"Kamu pilih {data.upper()}. Pilih produk:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data.startswith("detail_"):
        _, motor, idx = data.split("_")
        p = KATALOG[motor][int(idx)]
        text = f"📦 {p['nama']}\n💰 {p['harga']}\n\n📝 {p['desk']}"
        keyboard = [
            [InlineKeyboardButton("🎥 Lihat Review di TikTok", url=TIKTOK_LINK)],
            [InlineKeyboardButton("⬅️ Kembali ke list", callback_data=motor)]
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    elif data == "kembali":
        keyboard = [
            [InlineKeyboardButton("🛵 BEAT", callback_data="beat")],
            [InlineKeyboardButton("🏍️ VARIO", callback_data="vario")],
            [InlineKeyboardButton("📦 NMAX", callback_data="nmax")],
            [InlineKeyboardButton("🎥 TikTok Kami - batas_lintas9", url=TIKTOK_LINK)],
        ]
        await query.edit_message_text("Halo bro! Mau cari aksesoris apa? Pilih di bawah 👇", reply_markup=InlineKeyboardMarkup(keyboard))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tombol))
print("Bot jalan...")
app.run_polling()