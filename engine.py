import datetime
import time
import requests

from requests import Session
from lxml import html
from config import *
from random import randint

class Engine:
    
    def __init__(self) -> None:
        self.session = Session()
        self.html = html

    def get_time(self):

        date = self.get_headers("https://www.google.com/")['Date']
        return date
    
    def get_hout_minute(self):

        this_time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
        return this_time
    
    def start_timer(self, setted_time):
        while True:
            time_now = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
            if setted_time != time_now:
                pass
            else:
                return STOP_TIMER_MESSAGE
    
    def get_dnipro_weather(self):
        
        response = self.session.get(url = WEATHER_LINK)
        tree = self.html.fromstring(response.content)
        result = tree.xpath('//*[@id="bd1c"]/div[2]/div[2]/div')

        return result[0].text_content().strip()
    
    def get_headers(self, link : str) -> list:

        return requests.get(url=link).headers
    
    def get_content(self, link : str):

        return requests.get(url=link).content

    def get_random_number(self, limit : int) -> int:
        return randint(0, limit)