import telebot

from config import *
from regex_reader import *
from engine import *
from telebot import types
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()
        self.rgx = RegexReader()

        self.memes = self.eng.get_file_names(MEME_PATH)
        self.video_memes = self.eng.get_file_names(VIDEO_PATH)
        
        self.command_handlers = {START : self.welcome_func}
        
        self.command_words = {FROG_MESSAGE: self.send_frog_func,
                              TIME_MESSAGE : self.send_time,
                              WEATHER_MESSAGE : self.send_cities,
                              VIDEO_MEME_MESSAGE : self.video_meme,
                              MEME_MESSAGE : self.meme,
                              CURRENCY_MESSAGE : self.get_currency_course}

        self.setup_handlers()
    '''
        Method setup_handlers is a function, 
        which is handle & manage every bot command.
    '''
    def setup_handlers(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_messages(message):
            if message.text[0] == '/':
                command = message.text.split()[0][1:]
                if command in self.command_handlers:
                    self.command_handlers[command](message)
                else:
                    self.bot.reply_to(message, f"{UNKNOWN_MESSAGE} {command}")

            else:
                try:
                    command = message.text
                    self.command_words[command](message)
                except:
                    if message.text == CURRENCY_MESSAGE:
                        self.get_currency_course()

                    elif message.text == DOLLAR:
                        self.bot.send_message(
                                    message.chat.id,
                                    f"{CURRENCY_ANSWER_MESSAGE} {self.eng.get_currency(DOLLAR)}",
                                    parse_mode=HTML
                                    )
                        self.send_main_buttons(message=message)
                    
                    elif message.text == EURO:
                        self.bot.send_message(
                                    message.chat.id,
                                    f"{CURRENCY_ANSWER_MESSAGE} {self.eng.get_currency(EURO)}",
                                    parse_mode=HTML)
                        self.send_main_buttons(message=message)
                    
                    elif message.text in CITIES.keys():
                        for city in CITIES.keys():
                            if message.text == city:
                                self.bot.send_message(message.chat.id,
                                                      ANSWER_WEATHER_MESSAGE.format(city=city,
                                                                                    temp=self.eng.get_weather(city=CITIES[city])),
                                                      parse_mode=HTML,
                                                      )
                                self.send_main_buttons(message=message)

    def welcome_func(self, message):
        
        self.bot.send_message(message.chat.id,
                              WILLKOMMEN_MESSAGE,
                              parse_mode=HTML)
        self.send_main_buttons(message=message)
    
    def send_main_buttons(self, message):

        markup = types.ReplyKeyboardMarkup(row_width=2)
        meme_button = types.KeyboardButton(MEME_MESSAGE)
        video_meme_button = types.KeyboardButton(VIDEO_MEME_MESSAGE)
        weather_button = types.KeyboardButton(WEATHER_MESSAGE)
        time_button = types.KeyboardButton(TIME_MESSAGE)
        currency_button = types.KeyboardButton(CURRENCY_MESSAGE)
        take_frog_button = types.KeyboardButton(FROG_MESSAGE)

        markup.add(meme_button, video_meme_button, take_frog_button,
                   currency_button, weather_button, time_button)        
        
        self.bot.send_message(message.chat.id,
                              KEYBOARD_MESSAGE,
                              reply_markup=markup,
                              parse_mode=HTML)
    
    def get_currency_course(self, message):

        markup = types.ReplyKeyboardMarkup(row_width=2)
        dollar_button = types.KeyboardButton(DOLLAR)
        euro_button = types.KeyboardButton(EURO)

        markup.add(dollar_button, euro_button)

        self.bot.send_message(message.chat.id,
                              QUESTION_MESSAGE,
                              parse_mode=HTML,
                              reply_markup=markup)
    
    def send_cities(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=3)

        for city in CITIES:
            button = types.KeyboardButton(city)
            markup.add(button)
        
        self.bot.send_message(message.chat.id,
                              QUESTION_CITY_MESSAGE,
                              reply_markup=markup,
                              parse_mode=HTML)

    def send_frog_func(self, message):
        chat_id = message.chat.id
        photo = open(MEME_PATH+self.memes[self.memes.index('frog.jpg')], PHOTO_MODE)
        self.bot.reply_to(message, TAKE_FROG_MESSAGE)
        self.bot.send_photo(chat_id = chat_id, 
                            photo=photo)
    
    def send_time(self, message):
        self.bot.send_message(message.chat.id,
                              self.eng.get_time(),
                              parse_mode=HTML)
    
    def meme(self, message):
        chat_id = message.chat.id
        
        meme_number = self.eng.get_random_number(len(self.memes)-1)
        try:
            path = MEME_PATH + self.memes[meme_number]
            photo = open(path, PHOTO_MODE)
        
            self.bot.send_photo(chat_id=chat_id,
                                photo=photo,
                                parse_mode=HTML)
        except KeyError or UnboundLocalError:
            pass
    
    def video_meme(self, message):
        chat_id = message.chat.id
        meme_number = self.eng.get_random_number(len(self.video_memes)-1)

        try:
            video = open(VIDEO_PATH + self.video_memes[meme_number], PHOTO_MODE)
            self.bot.send_video(chat_id=chat_id,
                                video=video,
                                parse_mode=HTML)
            
        except:
            pass

    def start_polling(self):
        self.bot.polling(none_stop = True)
