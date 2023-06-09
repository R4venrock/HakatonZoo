import psycopg2 as psycopg2
import telebot
from telebot import types

from dotenv import load_dotenv
#from config import host, user, pasword, db_name
import os

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))

conn = psycopg2.connect(
    host="localhost",
    database="zoo_quiz",
    user="postgres",
    password="password"
)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать викторину')
    btn2 = types.KeyboardButton('❓Задать вопрос❓')
    btn3 = types.KeyboardButton('Поделиться в VK')
    murkup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Кнопки под окном чата помогут сориентироваться".format(
                         message.from_user),
                     reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Начать викторину':
        cursor.execute(
                """SELECT question FROM quiz"""
                )
        bot.send_message(message.chat.id, cursor.fetchone())
        cursor.execute(
            """SELECT answer FROM quiz WHERE id = 61"""
        )
        bot.send_message(message.chat.id, cursor.fetchone())
        conn.close()
        cursor.execute(
            """SELECT answer FROM quiz WHERE id = 62"""
        )
        bot.send_message(message.chat.id, cursor.fetchone())
        conn.close()
        cursor.execute(
            """SELECT answer FROM quiz WHERE id = 63"""
        )
        bot.send_message(message.chat.id, cursor.fetchone())
        conn.close()
        cursor.execute(
            """SELECT answer FROM quiz WHERE id = 64"""
        )
        bot.send_message(message.chat.id, cursor.fetchone())
        conn.close()

        # в elif добавил кнопку на VK (затем перенесем в нужное место) TODO
    elif message.text == 'Поделиться в VK':
        # text = '[Поделиться](https://vk.com/share.php?https://t.me/my_reincarnation_bot)'  # только шаблон
        text = '[Поделиться](https://vk.com/share.php?url=http%3A%2F%2Ft.me/my_reincarnation_bot%2Ftest-16576%3Fresult%3D02040206020504080203&title=Мой%20результат%20теста%3A%20КТО%20ТВОЕ%20ТОТЕМНОЕ%20ЖИВОТНОЕ%3F%20)'
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    else:
        bot.send_message(message.chat.id, text='В данный момент всё в разработке')


bot.polling(none_stop=True)
