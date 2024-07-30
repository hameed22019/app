import telebot

# استبدل TOKEN بالرمز المميز الخاص ببوتك في Telegram
TOKEN = '7377280197:AAH3UtSLnx8jOMZuMkjYLqh0ChcFw2NtXEc'

# إنشاء كائن البوت
bot = telebot.TeleBot(TOKEN)

# تعريف دالة المعالجة للأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا!")

# تشغيل البوت
bot.polling()
