import psycopg2 as psycopg2
import telebot
from telebot import types

from dotenv import load_dotenv
#from config import host, user, pasword, db_name
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


dict = {'id': 61}


def question(message):
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

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.message:
            if dict['id'] < 73:
                if call.data == 'answer_1':
                    dict['id'] +=4
                    question(message=call.message)
                elif call.data == 'answer_2':
                    dict['id'] += 4
                    question(message=call.message)
                elif call.data == 'answer_3':
                    dict['id'] += 4
                    question(message=call.message)
                elif call.data == 'answer_4':
                    dict['id'] += 4
                    question(message=call.message)
            else:
                with open('HakatonZoo\Без имени.jpg', 'rb') as f:
                    bot.send_photo(call.message.chat.id, f)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    except Exception as e:
        print(repr(e))


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
