import telebot
from telebot import types
import sqlite3

db = sqlite3.connect('costs.db')

token_api = "" #insert Bot token
bot = telebot.TeleBot(token_api, parse_mode=None)

@bot.message_handler(commands=['bot'])
def start_button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Транспорт")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2=types.KeyboardButton("Лекарства")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3=types.KeyboardButton("Продукты")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item4=types.KeyboardButton("Отдых")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item5=types.KeyboardButton("Обязательные платежи")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item6=types.KeyboardButton("Другое")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item7=types.KeyboardButton("Крупные покупки")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8=types.KeyboardButton("Заработано")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item9=types.KeyboardButton("Лимит и Баланс")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        
    markup.row(item1, item2,item3)
    markup.row(item4, item5,item6)
    markup.row(item7, item8,item9)
    
    bot.send_message(message.chat.id,'Выберите вариант расходов',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Транспорт":
        bot.send_message(message.chat.id,'Введите сумму...')  #it is necessary to add the function of passing values ​​to the Excel table
    elif message.text == "Лекарства":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Продукты":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Транспорт":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Отдых":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Обязательные платежи":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Другое":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Крупные покупки":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Заработано":
        bot.send_message(message.chat.id,'Введите сумму...')
    elif message.text == "Лимит и Баланс":
        bot.send_message(message.chat.id,'Ваш Лимит и Баланс составляют:' )

bot.polling(none_stop=True, interval=0)




print("the end")
