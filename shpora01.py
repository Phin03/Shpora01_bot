import telebot
from telebot import types
import glob, random


bot = telebot.TeleBot("5287538138:AAGAciw2hhKs_9n3J-aVoiCSoM7mw7VLfks")
@bot.message_handler(commands=["question"])
def question_(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Вопросы для стажировки:", reply_markup=keyboard)
    with open('questions.txt', encoding='utf-8') as f:
        l = f.read()
    bot.send_message(message.chat.id, l , reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help_(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Как я работаю? \n Ну, конечно, расскажу! \n Смотри", reply_markup=keyboard)
    with open('instruct.txt', encoding='utf-8') as f:
        m = f.read()
    bot.send_message(message.chat.id, m , reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Зачем я нужен? \n Это так важно? \n Поясняю", reply_markup=keyboard)
    with open('opis.txt', encoding='utf-8') as f:
        n = f.read()
    bot.send_message(message.chat.id, n , reply_markup=keyboard)
    bot.send_message(message.chat.id, "Со мной можно делать следующие действия: \n 1. /question - Выдам список вопросов для подготовки \n 2. /help - Расскажу как мной пользоваться \n 3. /add_question - Добавлю новый вопрос \n 4. /exit - Можете отправить стикер или номер изученного вопроса" , reply_markup=keyboard)

@bot.message_handler(commands=['1'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    with open("questions.txt",encoding='utf-8') as file:
        str1 = file.readlines()
        bot.send_message(message.chat.id, str1,reply_markup=keyboard)

@bot.message_handler(commands=['2'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "2"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['3'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "3"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['4'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "4"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['5'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "5"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['6'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "6"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['7'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "7"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['8'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "8"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['9'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "9"
    with open("questions.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=['10'])
def questions(message):
    keyboard = types.InlineKeyboardMarkup()
    num = "10"
    with open("index.txt", encoding='utf_8') as f:
        lst = f.readlines()
    for i in lst:
        if num in i:
            bot.send_message(message.chat.id,i,reply_markup=keyboard)

@bot.message_handler(commands=["add"])
def add_(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton( "Message the developer", url="telegram.me/phin03"))
    bot.send_message(message.chat.id,'Если есть предложения по изменению бота, свяжитесь с разработчиком.',reply_markup=keyboard)
    
bot.polling()
