import telebot
import random as r

bot = telebot.TeleBot("YOUR TOKEN")

games = {}

@bot.message_handler(commands=["start"])
def start_game(message):
    games[message.chat.id] = r.randint(1,10)
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text="угадай число от 1 до 10")

@bot.message_handler(func=lambda message: message.chat.id in games)
def game(message):
    try:
        user_number = int(message.text)
        if user_number < games[message.chat.id]:
            bot.send_message(chat_id=chat_id, text="больше")
        elif user_number > games[message.chat.id]:
            bot.send_message(chat_id=chat_id, text="больше")
        else:
            bot.send_message(chat_id=chat_id, text="угадал!!!")
            del games[message.chat.id]
    except ValueError:
        bot.send_message(chat_id=chat_id, text="пиши только числа")

bot.infinity_polling()
