import telebot

from config import *

class Bot:
    def __init__(self):
        bot = telebot.TeleBot(TOKEN)
        

    @self.bot.message_handler(commands=['start'],
                         func=lambda message: True)
    def welcome_func(self, message):
         self.bot.reply_to(message, 
                               WILLKOMMEN_MESSAGE,
                               parse_mode = HTML)
         
    @self.bot.message_handler(commands=['take_frog'],
                         func=lambda message: True)
    def send_frog(self, message):
        self.bot.reply_to(message, 
                             'Держи жабу.',
                              parse_mode = HTML)
        photo = open(PHOTO_NAME, PHOTO_MODE)
        self.bot.send_photo(message, photo)
    
    bot.polling(none_stop = True)
