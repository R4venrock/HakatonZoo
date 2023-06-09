import psycopg2 as psycopg2
import telebot
from telebot import types

from dotenv import load_dotenv
#from config import host, user, pasword, db_name
import os

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))

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
                try:
            # Подключение к базе данных
            connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='password',
                database='zoo_quiz')
            connection.autocommit = True
            # Создание курсора для базы данных
            with connection.cursor() as cursor:
                cursor.execute("""SELECT question FROM quiz WHERE id = 61""")
                question = str(cursor.fetchone())

                cursor.execute("""SELECT answer FROM quiz WHERE id = 61 """)
                answer_1 = str(cursor.fetchone())
                cursor.execute("""SELECT answer FROM quiz WHERE id = 62""")
                answer_2 = str(cursor.fetchone())
                cursor.execute("""SELECT answer FROM quiz WHERE id = 63""")
                answer_3 = str(cursor.fetchone())
                cursor.execute("""SELECT answer FROM quiz WHERE id = 64""")
                answer_4 = str(cursor.fetchone())

                murkup = types.InlineKeyboardMarkup(row_width=1)
                answer_1 = types.InlineKeyboardButton(text=answer_1, callback_data='answer_1')
                answer_2 = types.InlineKeyboardButton(text=answer_2, callback_data='answer_2')
                answer_3 = types.InlineKeyboardButton(text=answer_3, callback_data='answer_3')
                answer_4 = types.InlineKeyboardButton(text=answer_4, callback_data='answer_4')

                murkup.add(answer_1, answer_2, answer_3, answer_4)
                bot.send_message(message.chat.id, question, reply_markup=murkup)

        except Exception as _ex:
            bot.send_message(message.chat.id, _ex)
        finally:
            if connection:
                connection.close()

        # в elif добавил кнопку на VK (затем перенесем в нужное место) TODO
    elif message.text == 'Поделиться в VK':
        # text = '[Поделиться](https://vk.com/share.php?https://t.me/my_reincarnation_bot)'  # только шаблон
        text = '[Поделиться](https://vk.com/share.php?url=http%3A%2F%2Ft.me/my_reincarnation_bot%2Ftest-16576%3Fresult%3D02040206020504080203&title=Мой%20результат%20теста%3A%20КТО%20ТВОЕ%20ТОТЕМНОЕ%20ЖИВОТНОЕ%3F%20)'
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    else:
        bot.send_message(message.chat.id, text='В данный момент всё в разработке')

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'answer_1':
            #Добавляем балл
            bot.send_message(call.message.chat.id, 'Всё получилось') '''Это проверка бота'''

bot.polling(none_stop=True)
