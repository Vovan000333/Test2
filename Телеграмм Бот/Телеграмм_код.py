import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("6254716733:AAFzMlNY1MrCclRCXTpIWkI2E1BYnEo7zNE")


# @bot.message_handler(commands=['start'])
# def start(message):
#     start_menu = InlineKeyboardMarkup(row_width=3)
#     button1 = InlineKeyboardButton('Калькулятор', callback_data='Калькулятор')
#     button2 = InlineKeyboardButton('Погода', callback_data='Погода')
#     button3 = InlineKeyboardButton('Перезагрузка', callback_data='Перезагрузка')
#     start_menu.add(button1, button2, button3)
#
#     bot.send_message(message.chat.id, 'Выбери утилиту:', reply_markup=start_menu)

@bot.message_handler(commands=['start'])
def call_back_message(call_back_message):
    if call_back_message.call == 'Калькулятор':
        if call_back_message.call == 'Калькулятор':
            menu = ReplyKeyboardMarkup(resize_keyboard=True)
            command1_button = KeyboardButton('1')
            command2_button = KeyboardButton('2')
            command3_button = KeyboardButton('3')
            command4_button = KeyboardButton('4')
            command5_button = KeyboardButton('5')
            command6_button = KeyboardButton('6')
            command7_button = KeyboardButton('7')
            command8_button = KeyboardButton('8')
            command9_button = KeyboardButton('9')
            menu.add(command1_button, command2_button, command3_button,
                     command4_button, command5_button, command6_button,
                     command7_button ,command8_button ,command9_button)
            bot.send_message(call_back_message.message.chat.id, "Ты выбрал калькулятор. Давай посчитаем!")

        elif call_back_message.data == 'Погода':
            bot.send_message(call_back_message.message.chat.id, "Ты выбрал Погода.")
        elif call_back_message.data == 'Перезагрузка':
            bot.send_message(call_back_message.message.chat.id, "Ты выбрал Перезагрузка.")



            # def calc_keyboard(message):
            #     menu = ReplyKeyboardMarkup(resize_keyboard=True)
            #     command1_button = KeyboardButton('Калькулятор')
            #     command2_button = KeyboardButton('Погода')
            #     command3_button = KeyboardButton('Перезагрузка')
            #     menu.add(command1_button, command2_button, command3_button)








bot.polling()











#
# @bot.callback_query_handler(func=lambda call: call.data == 'Калькулятор')
# def calc(message):
#     menu = ReplyKeyboardMarkup(resize_keyboard=True)
#     command1_button = KeyboardButton('Калькулятор')
#     command2_button = KeyboardButton('Погода')
#     command3_button = KeyboardButton('Перезагрузка')
#     menu.add(command1_button, command2_button, command3_button)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback(call):
#     if call.data == 'Калькулятор':
#         bot.answer_callback_query(call.id, 'You pressed button 1')
#     elif call.data == 'Погода':
#         bot.answer_callback_query(call.id, 'You pressed button 2')
#     elif call.data == 'Перезагрузка':
#         bot.answer_callback_query(call.id, 'You pressed button 2')
#
# @bot.message_handler(commands=['Перезагрузка'])
# def command1(message):
#     bot.send_message(message.chat.id, 'You pressed /command1')
#
#
#
#
# @bot.message_handler(commands=['reverse'])
# def reverse(message):
#     mtext = message.split()
#     mtext = mtext[1]
#     print("Username: ",message.chat.username, " : ", message.text)
#     bot.reply_to(message, mtext[::-1])
#
# @bot.message_handler(commands=['plus'])
# def reverse(message):
#     mtext = message.text.split()
#     print(mtext)
#     a = float(mtext[1])
#     b = float(mtext[2])
#     print("Username: ",message.chat.username, " : ", message.text)
#     bot.reply_to(message, a + b)




