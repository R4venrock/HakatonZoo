import telebot
from telebot import types

from dotenv import load_dotenv
import os

import social_sharing

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать викторину')
    btn2 = types.KeyboardButton('❓Задать вопрос❓')
    btn3 = types.KeyboardButton('Поделиться в ВКонтакте')
    btn4 = types.KeyboardButton('Поделиться в Одноклассниках')
    btn5 = types.KeyboardButton('Поделиться в facebook')
    btn6 = types.KeyboardButton('Поделиться в twitter')
    # btn7 = types.KeyboardButton('Поделиться в Телеграм')  # ссылка на публикацию в telegram (не работает) TODO
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6,)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Кнопки под окном чата помогут сориентироваться".format(
                         message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Начать викторину':
        bot.send_message(message.chat.id, text='Викторина ещё в разработке')
    elif message.text == 'Поделиться в ВКонтакте':
        text = social_sharing.VK
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Поделиться в Одноклассниках':
        text = social_sharing.OK
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Поделиться в facebook':
        text = social_sharing.FB
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Поделиться в twitter':
        text = social_sharing.TW
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    # elif message.text == 'Поделиться в Телеграм': # ссылка на публикацию в telegram (не работает) TODO
    #     text = social_sharing.TG
    #     bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    else:
        bot.send_message(message.chat.id, text='В данный момент всё в разработке')


bot.polling(none_stop=True)
