from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import random

# Darslar mavzulari va ularga tegishli vazifalar
darslar = {
    "Massivlar bilan ishlash": ["Massiv yaratish", "Massiv elementlarini o'zgartirish", 
                               "Massivdan qiymat qidirish", "Massivni saralash",
                               "Massivni teskariga chiqarish", "Massiv ustida amallar",
                               "Ko'p o'lchamli massivlar", "Massiv metodlari",
                               "Massiv va funksiyalar", "Massiv misollari"],
    
    "Funksiyalar va modullar": ["Funksiya yaratish", "Parametrli funksiya", 
                               "Qiymat qaytaruvchi funksiya", "Rekursiya",
                               "Lambda funksiyalar", "Modul yaratish",
                               "Tashqi modullardan foydalanish", "Funksiyalar bilan ishlash",
                               "Funksiyalarni tekshirish", "Funksiya misollari"],
    
    # ... boshqa darslar shu tartibda
    "Ob'ektga yo'naltirilgan dasturlash": ["Class yaratish", "Ob'ekt xususiyatlari", 
                                         "Metodlar", "Meros olish",
                                         "Polimorfizm", "Encapsulation",
                                         "Abstrakt classlar", "Dunder metodlar",
                                         "Class va modullar", "OOP misollari"]
}

def start(update: Update, context: CallbackContext) -> None:
    """Botni ishga tushirish va darslarni tanlash uchun tugmalarni ko'rsatish"""
    # Dars mavzularini tugmalar sifatida joylashtiramiz (3 ta ustunda)
    buttons = [list(darslar.keys())[i:i+3] for i in range(0, len(darslar), 3)]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    
    update.message.reply_text(
        "Assalomu alaykum! Qaysi darsdan vazifa olishni hohlaysiz? Dars mavzusini tanlang:",
        reply_markup=reply_markup
    )

def send_random_task(update: Update, context: CallbackContext) -> None:
    """Tanlangan dars uchun tasodifiy vazifa yuborish"""
    dars_mavzusi = update.message.text
    
    if dars_mavzusi in darslar:
        vazifa = random.choice(darslar[dars_mavzusi])
        update.message.reply_text(f"Tanlangan dars: {dars_mavzusi}\n\nVazifa: {vazifa}")
    else:
        update.message.reply_text("Iltimos, quyidagi darslardan birini tanlang:", 
                                reply_markup=ReplyKeyboardMarkup([list(darslar.keys())], resize_keyboard=True))

def main() -> None:
    """Botni ishga tushirish"""
    # O'zingizning bot tokenizingizni qo'ying
    updater = Updater("8070944529:AAHh6DvFwH7-Yis9BZpcg8HpKSPuxvriA3c")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_random_task))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
