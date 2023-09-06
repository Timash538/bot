import telebot
import random
bot = telebot.TeleBot('6529797726:AAHpCo7HqrCcQX1VfTMyuoHysCM2HTxpHC4')

users = dict()
cables = ['5x6','5x10','3x1,5','3x2,5','3x4','3x10','5x16']

@bot.message_handler(context_types=['text'])
def get_text_messages(message):
    if message.from_user not in users:
        print('if сработало')
        cable = random.choice(cables)
        users[message.from_user] = cable
    bot.send_message(message.chat.id, 'Твой кабель: ', users.get(message.from_user))

bot.infinity_polling()
