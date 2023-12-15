import telebot

from config import *
from regex_reader import *
from engine import *
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.eng = Engine()
        self.rgx = RegexReader()
        self.memes = {0 : f'/frog.jpg',
                      1 : f'/fried_car.jpg',
                      2 : f'/are_you_still_here.jpg',
                      3 : f'/bears.jpg',
                      4 : f'/budanov.jpg',
                      5 : f'/lake_tank.jpg',
                      6 : f'/novokuznezk.jpg',
                      7 : f'/two_arabs.jpg',
                      8 : f'/i_am_tram.jpg',
                      9 : f'/ilon_musk.jpg'}

        self.video_memes = {0 : f'/people_servant.mp4',
                            1 : f'/krim_nash.mp4',
                            2 : f'/goslling_winter.mp4',
                            3 : f'/tchas_pishov.mp4',
                            4 : f'/skotinyaka.mp4',
                            5 : f'/poroshenko.mp4'}
        
        self.command_handlers = {START : self.welcome_func,
                                 SEND_FROG : self.send_frog_func,
                                 GET_TIME : self.send_time,
                                 START_TIME : self.set_timer,
                                 WEATHER : self.send_weather,
                                 VIDEO_MEME : self.video_meme,
                                 MEME : self.meme}
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
        chat_id = message.chat.id
        photo = open(MEME_PATH+self.memes[0], PHOTO_MODE)
        self.bot.reply_to(message, TAKE_FROG_MESSAGE)
        self.bot.send_photo(chat_id = chat_id, 
                            photo=photo)
    
    def send_time(self, message):
        self.bot.send_message(message.chat.id,
                              self.eng.get_time(),
                              parse_mode=HTML)
    
    def set_timer(self, message) -> str:
        user_message = message.text.split()
        try:
            setted_time = user_message[1]
            while True:
                if self.eng.get_hout_minute() == setted_time:
                    break
            self.bot.send_message(message.chat.id,
                                  STOP_TIMER_MESSAGE,
                                  parse_mode=HTML)
        except IndexError:
            self.bot.reply_to(message, WRONG_COMMAND_MESSAGE)
    
    def meme(self, message):
        chat_id = message.chat.id
        
        meme_number = self.eng.get_random_number(len(self.memes))
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
        meme_number = self.eng.get_random_number(len(self.video_memes))

        try:
            video = open(VIDEO_PATH + self.video_memes[meme_number], PHOTO_MODE)
            self.bot.send_video(chat_id=chat_id,
                                video=video,
                                parse_mode=HTML)
            
        except KeyError or UnboundLocalError:
            pass
        
    def send_weather(self, message):
        self.bot.send_message(message.chat.id,
                              self.eng.get_dnipro_weather(),
                              parse_mode=HTML)

    def start_polling(self):
        self.bot.polling(none_stop = True)
