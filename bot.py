import telebot

from config import *

class Bot:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def welcome_func(self, message):
         self.bot.send_message(message.chat.id, 
                               WILLKOMMEN_MESSAGE,
                               parse_mode = HTML)
         
    @bot.message_handler(commands=['take_frog'])
    def send_frog(self, message):
        self.bot.send_message(message.chat.id, 
                               'Держи жабу.',
                               parse_mode = HTML)
        photo = open(PHOTO_NAME, PHOTO_MODE)
        self.bot.send_photo(message.chat.id, photo)
    
    bot.polling(none_stop = True)
