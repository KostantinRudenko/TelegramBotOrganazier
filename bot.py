import telebot

from config import *
from engine import *
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()
        self.command_handlers = {START : self.welcome_func,
                                 SEND_FROG : self.send_frog_func,
                                 GET_TIME : self.send_time}
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
        pass

    def start_polling(self):
        self.bot.polling(none_stop = True)
