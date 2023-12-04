import telebot

from config import *
from engine import *
class Bot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()
        self.pgo = PageObject()

        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.welcome_func(message)

        @self.bot.message_handler(commands=['help'])
        def print_help_message(message):
            self.send_help(message)
        
        @self.bot.message_handler(commands=['take_frog'])
        def send_frog_picture(message):
            self.send_frog(message)
        
        @self.bot.message_handler(commands=['get_time'])
        def get_time(message):
            self.returning_time(message)
        @self.bot.message_handler(commands=["get_courses"])
        def get_courses(message):
            self.currency_courses(message)


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
    
    def send_help(self, message):
        self.bot.send_message(message.chat.id,
                            HELP_MESSAGE,
                            parse_mode=HTML)
    def currency_courses(self, message):
        courses = self.currency_courses()
        self.bot.send_message(message.chat.id,
                              f"Courses of Currencies:\n1 Dollar - {courses[0]}hrivnas.\n1 Euro - {courses[1]}hrivnas.",
                              parse_mode=HTML)
    def run(self):
        self.bot.polling(none_stop = True)