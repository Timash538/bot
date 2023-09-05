import telebot
bot = telebot.TeleBot('6529797726:AAHpCo7HqrCcQX1VfTMyuoHysCM2HTxpHC4')

@bot.message_handler(content_type=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id, "Иди нахер")

bot.infinity_polling()
