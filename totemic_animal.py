import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать викторину')
    btn2 = types.KeyboardButton('❓Задать вопрос❓')
    murkup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Кнопки под окном чата помогут сориентироваться".format(
                         message.from_user),
                     reply_markup=murkup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Начать викторину':
        bot.send_message(message.chat.id, text='Викторина ещё в разработке')
    else:
        bot.send_message(message.chat.id, text='В данный момент всё в разработке')


bot.polling(none_stop=True)
