import telebot

from config import *
from engine import *
class Bot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()

        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.welcome_func(message)
        
        @self.bot.message_handler(commands=['take_frog'])
        def send_frog_picture(message):
            self.send_frog(message)
        
        @self.bot.message_handler(commands=['get_time'])
        def get_time(message):
            self.returning_time(message)

    def welcome_func(self, message):
        self.bot.send_message(message.chat.id, 
                            WILLKOMMEN_MESSAGE,
                            parse_mode = HTML)

    def send_frog(self, message):
        self.bot.send_message(message.chat.id, 
                               'Держи жабу.',
                               parse_mode = HTML)
        photo = open(PHOTO_NAME, PHOTO_MODE)
        self.bot.send_photo(message.chat.id, photo)

    def returning_time(self, message):
        time = self.eng.get_time()
        self.bot.send_message(message.chat.id,
                              time,
                              parse_mode=HTML)
    
    def run(self):
        self.bot.polling(none_stop = True)