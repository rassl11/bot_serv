import time

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from const import *
from sql_req import *
import sqlite3



def start(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    id_in = cur.execute(id_in_table.format(user_id)).fetchall()
    print(id_in)

    try:
        id_in = id_in[0][0]
        context.bot.send_message(text="{} Добро пожаловать в Timekeeper Service Bot, Выбери свой стол".format(name), chat_id=user_id)
    except IndexError:
        cur.execute(first_insert.format(user_id, name))
        button = [KeyboardButton(text="Отправить номер", request_contact=True)]
        context.bot.send_message(text='asd', chat_id=user_id,
                                 reply_markup=ReplyKeyboardMarkup([button], resize_keyboard=True,
                                                                  one_time_keyboard=True))

        conn.commit()


def get_contact(update,context):
    num = update.message.contact.phone_number
    user_id = update.message.chat_id
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone.format(num,user_id))
    conn.commit()
    context.bot.send_message(chat_id = user_id, text = 'Отлично,теперь введи номер стола')

def text_answer(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    text = update.message.text
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    rasul = 44335784
    mashhur = 1561567583
    maksim = 136254696
    jenya = 1737226541
    ilnur = 653135443
    stas = 1561453505
    nigina = 246886708
    vlad = 1319090684
    timur = 34824365
    ulugbek = 1207448934
    allowed_tables = ['100','101','102','103','104','200','201','202','203','204','300','301','302','303','1998']



    if text.isdigit and text in allowed_tables:
        cur.execute(update_table_number.format(text, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))

    elif text == 'Сделать заказ':
        context.bot.send_message(chat_id = user_id,text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button]))

    elif text == 'Кальян':
        context.bot.send_message(chat_id = user_id,text = "Какой крепости кальян",reply_markup = ReplyKeyboardMarkup([easy,medium,rare],resize_keyboard=True))



    elif text =='Легкий' or text == 'Средний' or text == 'Крепкий':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id,text = 'Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,fruit,desert,citrus],resize_keyboard=True))

        zakaz = cur.execute(add_zakaz.format(user_id)).fetchall()
        zakaz.append(text)
        print(zakaz)

        a = cur.execute(update_zakaz.format(text,user_id)).fetchall()
        print(a)

        conn.commit()





    elif text == 'Ягодный' or text == 'Фруктовый' or text == 'Цитрусовый' or text =='Десертный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Тип курения?',
                                 reply_markup=ReplyKeyboardMarkup([folga,kolaud], resize_keyboard=True))
        type = cur.execute(update_zakaz.format(text,user_id)).fetchall()
        type.append(text)
        print(type)
        conn.commit()




    elif text == 'Калауд' or text == 'Фольга':
        context.bot.send_message(chat_id = user_id,text = 'С холодком или без?',reply_markup = ReplyKeyboardMarkup([ice,no_ice],resize_keyboard=True))
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()



    elif text == 'С холодком' or text == 'Без Холодка':
        context.bot.send_message(chat_id = user_id, text = 'Отлично,добавляем в корзину?',
                                 reply_markup = ReplyKeyboardMarkup([yes,no],resize_keyboard=True))

    elif text =='Да':
        context.bot.send_message(chat_id = user_id,text ='''Кальян добавлен в корзину
Вернуться в главное меню?''')

    elif text == 'Выбрать что-нибудь еще':
        context.bot.send_message(chat_id = user_id,text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button]))


    elif text =='Позвать Таймгарда🏃':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        print(a[0][0])
        context.bot.send_message(chat_id=user_id, text='Так Точно💪!')



    elif text == 'Продуть Кальян💨':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Понял Принял👌')


    elif text == 'Попросить счет💵':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Уже сделано! Оцените работу вашего Таймгарда',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [five_star, four_star, three_star, two_star, one_star], resize_keyboard=True,
                                     one_time_keyboard=True))


    elif text == '⭐⭐⭐⭐⭐':
        cur.execute(update_mark.format(5, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐⭐⭐':
        cur.execute(update_mark.format(4, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐⭐':
        cur.execute(update_mark.format(3, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐':
        cur.execute(update_mark.format(2, user_id))
        context.bot.send_message(chat_id=user_id,text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐':
        cur.execute(update_mark.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))

    elif text.isdigit() and text not in allowed_tables:
        context.bot.send_message(chat_id = user_id,text = 'У нас нет такого стола')



    else:
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = "Сейчас все будет!")
        datetime = time.asctime()
        Logpath = 'answers.txt'
        log = open(Logpath, 'a')
        logstr = "{} | user_id:{}, Что выбрал: {} \n".format(datetime, user_id, text)
        log.writelines(logstr)

    conn.commit()

