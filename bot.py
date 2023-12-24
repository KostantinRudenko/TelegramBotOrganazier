import telebot

from config import *
from regex_reader import *
from engine import *
from telebot import types
import requests
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
                        """
                        Check if user decided to know currency course
                        """
                        self.get_currency_course()

                    elif message.text == DOLLAR:
                        """
                        Check if user choised dollar as currency
                        """
                        self.bot.send_message(
                                    message.chat.id,
                                    f"{CURRENCY_ANSWER_MESSAGE} {self.eng.get_currency(DOLLAR)}",
                                    parse_mode=HTML
                                    )
                        self.send_main_buttons(message=message)
                    
                    elif message.text == EURO:
                        """
                        Check if user choised euro as currency
                        """
                        self.bot.send_message(
                                    message.chat.id,
                                    f"{CURRENCY_ANSWER_MESSAGE} {self.eng.get_currency(EURO)}",
                                    parse_mode=HTML)
                        self.send_main_buttons(message=message)
                    
                    elif message.text in CITIES.keys():
                        """
                        Check if user try to know weather in a city
                        """
                        for city in CITIES.keys():
                            if message.text == city:
                                self.bot.send_message(message.chat.id,
                                                      ANSWER_WEATHER_MESSAGE.format(city=city,
                                                                                    temp=self.eng.get_weather(city=CITIES[city])),
                                                      parse_mode=HTML,
                                                      )
                                self.send_main_buttons(message=message)

                    elif message.text == MESSAGE_MESSAGE:
                        self.bot.send_message(message.chat.id,
                                              MESSAGE_ANSWER_MESSAGE,
                                              parse_mode=HTML)

                    elif self.rgx.read_data(pattern=USER_MESSAGE, text=message.text):
                        messages = self.rgx.read_data(pattern=USER_MESSAGE, text=message.text)
                        for text in messages:
                            userid = self.rgx.read_data(pattern=USERNAME, text=message.text)[0]
                            text = message.text.replace(userid, '', 1)
                            self.send_message_to_user(message,
                                                        userid=userid,
                                                        text=text)

    def welcome_func(self, message):
        
        """
        Greets user
        """
        self.bot.send_message(message.chat.id,
                              WILLKOMMEN_MESSAGE,
                              parse_mode=HTML)
        self.send_main_buttons(message=message)
    
    def send_main_buttons(self, message):

        """
        Return usual choice of commands(keyboard) to the user
        """
        markup = types.ReplyKeyboardMarkup(row_width=2)
        meme_button = types.KeyboardButton(MEME_MESSAGE)
        video_meme_button = types.KeyboardButton(VIDEO_MEME_MESSAGE)
        weather_button = types.KeyboardButton(WEATHER_MESSAGE)
        time_button = types.KeyboardButton(TIME_MESSAGE)
        currency_button = types.KeyboardButton(CURRENCY_MESSAGE)
        take_frog_button = types.KeyboardButton(FROG_MESSAGE)
        message_button = types.KeyboardButton(MESSAGE_MESSAGE)

        markup.add(meme_button, video_meme_button, take_frog_button,
                   currency_button, weather_button, time_button, message_button)        
        
        self.bot.send_message(message.chat.id,
                              KEYBOARD_MESSAGE,
                              reply_markup=markup,
                              parse_mode=HTML)
    
    def get_currency_course(self, message):
        """
        Sends user a keyboard with choice of currencies
        """

        markup = types.ReplyKeyboardMarkup(row_width=2)
        dollar_button = types.KeyboardButton(DOLLAR)
        euro_button = types.KeyboardButton(EURO)

        markup.add(dollar_button, euro_button)

        self.bot.send_message(message.chat.id,
                              QUESTION_MESSAGE,
                              parse_mode=HTML,
                              reply_markup=markup)
    
    def send_cities(self, message):
        """
        Sends user keyboard with choise of ukrainian cities
        """
        markup = types.ReplyKeyboardMarkup(row_width=3)

        for city in CITIES:
            button = types.KeyboardButton(city)
            markup.add(button)
        
        self.bot.send_message(message.chat.id,
                              QUESTION_CITY_MESSAGE,
                              reply_markup=markup,
                              parse_mode=HTML)

    def send_frog_func(self, message):
        """
        Sends frog :)
        """
        chat_id = message.chat.id
        photo = open(MEME_PATH+self.memes[self.memes.index('frog.jpg')], PHOTO_MODE)
        self.bot.reply_to(message, TAKE_FROG_MESSAGE)
        self.bot.send_photo(chat_id = chat_id, 
                            photo=photo)
    
    def send_time(self, message):
        """
        Sends current time to user
        """
        self.bot.send_message(message.chat.id,
                              self.eng.get_time(),
                              parse_mode=HTML)
    
    def meme(self, message):
        """
        Sends random meme from folder to user
        """
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
        """
        Sends random video meme from folder to user
        """
        chat_id = message.chat.id
        meme_number = self.eng.get_random_number(len(self.video_memes)-1)

        try:
            video = open(VIDEO_PATH + self.video_memes[meme_number], PHOTO_MODE)
            self.bot.send_video(chat_id=chat_id,
                                video=video,
                                parse_mode=HTML)
            
        except:
            pass
    
    def send_message_to_user(self, message, userid, text):
        try:
            params = {'chat_id' : userid,
                      'text'    : text}
            url = requests.post(TELEGRAM_LINK, params=params)
        except:
            bogdan = open(MEME_PATH+self.memes[self.memes.index("bogdan.jpg")], PHOTO_MODE)
            
            self.bot.send_message(message.chat.id,
                                  BOGDAN_MESSAGE,
                                  parse_mode=HTML)
            
            self.bot.send_photo(message.chat.id,
                                    bogdan,
                                    parse_mode=HTML)

    def start_polling(self):
        self.bot.polling(none_stop = True)
