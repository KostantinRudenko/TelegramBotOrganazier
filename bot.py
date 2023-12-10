import telebot
import time

from config import *
from regex_reader import *
from engine import *
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()
        self.rgx = RegexReader()
        self.command_handlers = {START : self.welcome_func,
                                 SEND_FROG : self.send_frog_func,
                                 GET_TIME : self.send_time,
                                 START_TIME : self.set_timer}
        self.setup_handlers()
    '''
        Method setup_handlers is a function, 
        which is handle & manage every bot command.
    '''
    def setup_handlers(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_messages(message):
            command = message.text.split()[0][1:]
            if command in self.command_handlers:
                self.command_handlers[command](message)
            else:
                self.bot.reply_to(message, f"{UNKNOWN_MESSAGE} {command}")

    def welcome_func(self, message):
        self.bot.reply_to(message, WILLKOMMEN_MESSAGE)

    def send_frog_func(self, message):
        chat_id = message.id
        photo = open(PHOTO_NAME_PATH, PHOTO_MODE)
        self.bot.reply_to(message, TAKE_FROG_MESSAGE)
        self.bot.send_photo(chat_id = chat_id, 
                            photo=photo)
    
    def send_time(self, message):
        self.bot.send_message(message.chat.id,
                              self.eng.get_time(),
                              parse_mode=HTML)
    
    def set_timer(self, message):
        self.bot.send_message(message.chat.id,
                              "Введите время.\nЧас:минута\nУ тебя 10 секунд. Дерзай!",
                              parse_mode=HTML)
        time.sleep(10)
        user_message = message.text.strip()
        time_now = self.rgx.read_data(r"\d+:\d+", user_message)
        if time_now:
            self.eng.start_timer(time_now)
        else:
            self.bot.send_message(message.chat.id,
                                  "Я сказал, введи время по шаблону Час:Минута!",
                                  parse_mode=HTML)

    def start_polling(self):
        self.bot.polling(none_stop = True)
