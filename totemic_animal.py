import psycopg2
import telebot
from telebot import types

from dotenv import load_dotenv
import os

import social_sharing

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TOKEN'))

review = ''
username = ''
animals = {'penguin': 0,
          'owl': 0, 'bear': 0,
           'lori': 0, 'irbis': 0,
           'tiger': 0, 'eagle': 0,
           'bird_sec': 0, 'vicuna': 0,
           'cuscus': 0, 'crocodile': 0,
           'manul': 0,  'otter': 0,}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать викторину')
    btn2 = types.KeyboardButton('❓Задать вопрос❓')
    btn3 = types.KeyboardButton('Поделиться в ВКонтакте')
    btn4 = types.KeyboardButton('Поделиться в Одноклассниках')
    btn5 = types.KeyboardButton('Поделиться в Телеграм')
    btn6 = types.KeyboardButton('Отзывы')
    btn7 = types.KeyboardButton('Пройти викторину еще раз')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7,)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Кнопки под окном чата помогут сориентироваться".format(
                         message.from_user),
                     reply_markup=markup)


dict = {'id': 61}
def question(message):
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(
            host='localhost',
            user='user',
            password='password',
            database='d_b')
        connection.autocommit = True
        # Создание курсора для базы данных

        with connection.cursor() as cursor:

            cursor.execute('SELECT question FROM quiz WHERE id=%(id)s', dict)
            question = list(cursor.fetchone())
            cursor.execute('SELECT answer FROM quiz WHERE question = (SELECT question FROM quiz WHERE id=%(id)s)', dict)

            answer = list(cursor.fetchall())
            murkup_q = types.InlineKeyboardMarkup(row_width=1)
            answer_1 = types.InlineKeyboardButton(text=str(answer[0][0]), callback_data='answer_1')
            answer_2 = types.InlineKeyboardButton(text=str(answer[1][0]), callback_data='answer_2')
            answer_3 = types.InlineKeyboardButton(text=str(answer[2][0]), callback_data='answer_3')
            answer_4 = types.InlineKeyboardButton(text=str(answer[3][0]), callback_data='answer_4')

            murkup_q.add(answer_1, answer_2, answer_3, answer_4)
            bot.send_message(message.chat.id, question, reply_markup=murkup_q)

    except Exception as _ex:
        #bot.send_message(message.chat.id, _ex)
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Начать викторину':
        question(message)
    elif message.text == 'Отзывы':
        bot.send_message(message.from_user.id, 'Как Вас зовут?')
        bot.register_next_step_handler(message, username)
    elif message.text == 'Поделиться в ВКонтакте':
        text = social_sharing.VK
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Поделиться в Одноклассниках':
        text = social_sharing.OK
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Поделиться в Телеграм':
        text = social_sharing.TG
        bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    elif message.text == 'Пройти викторину еще раз':
        question(message)
    elif message.text == 'Отзывы':
        bot.send_message(message.from_user.id, 'Как Вас зовут?')
        bot.register_next_step_handler(message, username)
    else:
        bot.send_message(message.chat.id, text='В данный момент всё в разработке')


bot.polling(none_stop=True)
