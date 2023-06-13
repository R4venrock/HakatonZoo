import psycopg2 as psycopg2
import telebot
from telebot import types

from dotenv import load_dotenv
from config import host, user, pasword, db_name
import os

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
    with open('HakatonZoo\photo_2023-06-13_12-14-34.jpg', 'rb') as f:
         photo = bot.send_photo(message.chat.id, f)
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать викторину')
    btn2 = types.KeyboardButton('❓Задать вопрос❓')
    btn3 = types.KeyboardButton('Поделиться в ВКонтакте')
    btn4 = types.KeyboardButton('Поделиться в Одноклассниках')
    btn5 = types.KeyboardButton('Поделиться в facebook')
    btn6 = types.KeyboardButton('Поделиться в twitter')
    btn7 = types.KeyboardButton('Отзывы')
    murkup.add(btn1, btn2, btn3, btn4, btn5, btn6,)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Меня зовут Тимофей, я манул, являюсь символом зоопарка с 1983 (или какого там) года. И сегодня я расскажу тебе кое-что интересное😏 Но для начала попробуй пройти небольшую викторину😊".format(
                         message.from_user, photo),
                     reply_markup=murkup)


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

     # в elif добавил кнопку на VK (затем перенесем в нужное место) TODO
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

def username(message):
    global username
    username = message.text
    bot.send_message(message.from_user.id, 'Оставьте, пожалуйста свой отзыв о боте')
    bot.register_next_step_handler(message, reviews)

def reviews(message):
    global review
    review = message.text
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    key_yes = types.InlineKeyboardButton(text='Отправить', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')

    keyboard .add(key_yes, key_no)
    bot.send_message(message.from_user.id, text='Отправить отзыв?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    try:
        if call.message:
            connection = psycopg2.connect(
                host='localhost',
                user='user',
                password='password',
                database='d_b')
            connection.autocommit = True
            cursor = connection.cursor()
            if call.data == 'yes':
                cursor.execute("INSERT INTO reviews (id_user, username, review) VALUES (%s, %s, %s)", (call.message.chat.id, username, review))
                connection.commit()
                bot.send_message(call.message.chat.id, text="Спасибо!")
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, text="Тимофей явно расстроится, возможно у вас найдётся пара слов хотя бы в его адрес?")

            if dict['id'] < 113:
                if call.data == 'answer_1':
                    cursor.execute('SELECT penguin, owl, bear, lori, irbis, tiger, eagle, bird_sec, vicuna, cuscus, crocodile, manul, otter FROM quiz WHERE id=%(id)s', dict)
                    a = list(cursor.fetchall())
                    if a[0][0] == 1:
                        animals['penguin'] += 1
                    elif a[0][0] == -1:
                        animals['penguin'] -= 1
                    if a[0][1] == 1:
                        animals['owl'] += 1
                    if a[0][1] == -1:
                        animals['owl'] -= 1
                    if a[0][2] == 1:
                        animals['bear'] += 1
                    if a[0][2] == -1:
                        animals['bear'] -= 1
                    if a[0][3] == 1:
                        animals['lori'] += 1
                    if a[0][3] == -1:
                        animals['lori'] -= 1
                    if a[0][4] == 1:
                        animals['irbis'] += 1
                    if a[0][4] == -1:
                        animals['irbis'] -= 1
                    if a[0][5] == 1:
                        animals['tiger'] += 1
                    if a[0][5] == -1:
                        animals['tiger'] -= 1
                    if a[0][6] == 1:
                        animals['eagle'] += 1
                    if a[0][6] == -1:
                        animals['eagle'] -= 1
                    if a[0][7] == 1:
                        animals['bird_sec'] += 1
                    if a[0][7] == -1:
                        animals['bird_sec'] -= 1
                    if a[0][8] == 1:
                        animals['vicuna'] += 1
                    if a[0][8] == -1:
                        animals['vicuna'] -= 1
                    if a[0][9] == 1:
                        animals['cuscus'] += 1
                    if a[0][9] == -1:
                        animals['cuscus'] -= 1
                    if a[0][10] == 1:
                        animals['crocodile'] += 1
                    if a[0][10] == -1:
                        animals['crocodile'] -= 1
                    if a[0][11] == 1:
                        animals['manul'] += 1
                    if a[0][11] == -1:
                        animals['manul'] -= 1

                    if a[0][12] == 1:
                        animals['otter'] += 1
                    if a[0][12] == -1:
                        animals['otter'] -= 1
                    dict['id'] +=4
                    if dict['id'] == 73:
                        dict['id'] = 89
                    question(message=call.message)


                elif call.data == 'answer_2':
                    cursor.execute(
                        'SELECT penguin, owl, bear, lori, irbis, tiger, eagle, bird_sec, vicuna, cuscus, crocodile, manul, otter FROM quiz WHERE id=%(id)s',
                        dict)
                    a = list(cursor.fetchall())
                    if a[0][0] == 1:
                        animals['penguin'] += 1
                    elif a[0][0] == -1:
                        animals['penguin'] -= 1
                    if a[0][1] == 1:
                        animals['owl'] += 1
                    if a[0][1] == -1:
                        animals['owl'] -= 1
                    if a[0][2] == 1:
                        animals['bear'] += 1
                    if a[0][2] == -1:
                        animals['bear'] -= 1
                    if a[0][3] == 1:
                        animals['lori'] += 1
                    if a[0][3] == -1:
                        animals['lori'] -= 1
                    if a[0][4] == 1:
                        animals['irbis'] += 1
                    if a[0][4] == -1:
                        animals['irbis'] -= 1
                    if a[0][5] == 1:
                        animals['tiger'] += 1
                    if a[0][5] == -1:
                        animals['tiger'] -= 1
                    if a[0][6] == 1:
                        animals['eagle'] += 1
                    if a[0][6] == -1:
                        animals['eagle'] -= 1
                    if a[0][7] == 1:
                        animals['bird_sec'] += 1
                    if a[0][7] == -1:
                        animals['bird_sec'] -= 1
                    if a[0][8] == 1:
                        animals['vicuna'] += 1
                    if a[0][8] == -1:
                        animals['vicuna'] -= 1
                    if a[0][9] == 1:
                        animals['cuscus'] += 1
                    if a[0][9] == -1:
                        animals['cuscus'] -= 1
                    if a[0][10] == 1:
                        animals['crocodile'] += 1
                    if a[0][10] == -1:
                        animals['crocodile'] -= 1
                    if a[0][11] == 1:
                        animals['manul'] += 1
                    if a[0][11] == -1:
                        animals['manul'] -= 1

                    if a[0][12] == 1:
                        animals['otter'] += 1
                    if a[0][12] == -1:
                        animals['otter'] -= 1
                    dict['id'] += 4
                    if dict['id'] == 73:
                        dict['id'] = 89
                    question(message=call.message)


                elif call.data == 'answer_3':
                    cursor.execute(
                        'SELECT penguin, owl, bear, lori, irbis, tiger, eagle, bird_sec, vicuna, cuscus, crocodile, manul, otter FROM quiz WHERE id=%(id)s',
                        dict)
                    a = list(cursor.fetchall())
                    if a[0][0] == 1:
                        animals['penguin'] += 1
                    elif a[0][0] == -1:
                        animals['penguin'] -= 1
                    if a[0][1] == 1:
                        animals['owl'] += 1
                    if a[0][1] == -1:
                        animals['owl'] -= 1
                    if a[0][2] == 1:
                        animals['bear'] += 1
                    if a[0][2] == -1:
                        animals['bear'] -= 1
                    if a[0][3] == 1:
                        animals['lori'] += 1
                    if a[0][3] == -1:
                        animals['lori'] -= 1
                    if a[0][4] == 1:
                        animals['irbis'] += 1
                    if a[0][4] == -1:
                        animals['irbis'] -= 1
                    if a[0][5] == 1:
                        animals['tiger'] += 1
                    if a[0][5] == -1:
                        animals['tiger'] -= 1
                    if a[0][6] == 1:
                        animals['eagle'] += 1
                    if a[0][6] == -1:
                        animals['eagle'] -= 1
                    if a[0][7] == 1:
                        animals['bird_sec'] += 1
                    if a[0][7] == -1:
                        animals['bird_sec'] -= 1
                    if a[0][8] == 1:
                        animals['vicuna'] += 1
                    if a[0][8] == -1:
                        animals['vicuna'] -= 1
                    if a[0][9] == 1:
                        animals['cuscus'] += 1
                    if a[0][9] == -1:
                        animals['cuscus'] -= 1
                    if a[0][10] == 1:
                        animals['crocodile'] += 1
                    if a[0][10] == -1:
                        animals['crocodile'] -= 1
                    if a[0][11] == 1:
                        animals['manul'] += 1
                    if a[0][11] == -1:
                        animals['manul'] -= 1
                    if a[0][12] == 1:
                        animals['otter'] += 1
                    if a[0][12] == -1:
                        animals['otter'] -= 1
                    dict['id'] += 4
                    if dict['id'] == 73:
                        dict['id'] = 89
                    question(message=call.message)


                elif call.data == 'answer_4':
                    cursor.execute(
                        'SELECT penguin, owl, bear, lori, irbis, tiger, eagle, bird_sec, vicuna, cuscus, crocodile, manul, otter FROM quiz WHERE id=%(id)s',
                        dict)
                    a = list(cursor.fetchall())
                    if a[0][0] == 1:
                        animals['penguin'] += 1
                    elif a[0][0] == -1:
                        animals['penguin'] -= 1
                    if a[0][1] == 1:
                        animals['owl'] += 1
                    if a[0][1] == -1:
                        animals['owl'] -= 1
                    if a[0][2] == 1:
                        animals['bear'] += 1
                    if a[0][2] == -1:
                        animals['bear'] -= 1
                    if a[0][3] == 1:
                        animals['lori'] += 1
                    if a[0][3] == -1:
                        animals['lori'] -= 1
                    if a[0][4] == 1:
                        animals['irbis'] += 1
                    if a[0][4] == -1:
                        animals['irbis'] -= 1
                    if a[0][5] == 1:
                        animals['tiger'] += 1
                    if a[0][5] == -1:
                        animals['tiger'] -= 1
                    if a[0][6] == 1:
                        animals['eagle'] += 1
                    if a[0][6] == -1:
                        animals['eagle'] -= 1
                    if a[0][7] == 1:
                        animals['bird_sec'] += 1
                    if a[0][7] == -1:
                        animals['bird_sec'] -= 1
                    if a[0][8] == 1:
                        animals['vicuna'] += 1
                    if a[0][8] == -1:
                        animals['vicuna'] -= 1
                    if a[0][9] == 1:
                        animals['cuscus'] += 1
                    if a[0][9] == -1:
                        animals['cuscus'] -= 1
                    if a[0][10] == 1:
                        animals['crocodile'] += 1
                    if a[0][10] == -1:
                        animals['crocodile'] -= 1
                    if a[0][11] == 1:
                        animals['manul'] += 1
                    if a[0][11] == -1:
                        animals['manul'] -= 1
                    if a[0][12] == 1:
                        animals['otter'] += 1
                    if a[0][12] == -1:
                        animals['otter'] -= 1
                    dict['id'] += 4
                    if dict['id'] == 73:
                        dict['id'] = 89
                    question(message=call.message)


            elif dict['id'] == 113:
                            elif dict['id'] == 113:
                maxx = 0
                list_max = []
                for elem in animals:
                    if animals[elem] > maxx:
                        maxx = animals[elem]
                for elem in animals:
                    if animals[elem] == maxx:
                        list_max.append(elem)
                animal = random.choice(list_max)

                animal_dict = {'id': animal}

                cursor.execute('SELECT image, result_text FROM animal_results WHERE id=%(id)s', animal_dict)
                itog_animal = list(cursor.fetchall())

                bot.send_message(call.message.chat.id,
                                 text=str(itog_animal[0][1]) +' '+ str(itog_animal[0][0]))
                dict['id'] = 61
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)
