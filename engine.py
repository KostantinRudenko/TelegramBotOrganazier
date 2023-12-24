import datetime
import requests
import os

from config import *
from random import randint
from bs4 import BeautifulSoup
from regex_reader import RegexReader

class Engine:
    
    def __init__(self) -> None:
        self.regexer = RegexReader()
    
    def get_time(self):

        this_time = f"Сейчас {datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
        return this_time
    
    def get_weather(self, city : str):
        """
        Gets weather from the website
        """
        google_page = requests.get(WEATHER_LINK.format(city=city))
        soup = BeautifulSoup(google_page.text, "html.parser")

        result = soup.find_all(name="p",
                               attrs={"class" : "today-temp"})[0].get_text()
        if result:
            return result
        else:
            return 'There is nothing we can do.'
    
    def get_currency(self, currency):
        """
        Gets courses of dollar and euro in grivnas
        """
        if currency == DOLLAR:
            page = requests.get(DOLLAR_LINK)
        elif currency == EURO:
            page = requests.get(EURO_LINK)
        
        soup = BeautifulSoup(page.text, 'html.parser')
        result = soup.find_all(name='div',
                               attrs={"type" : "average",
                                "class" : "sc-1x32wa2-9 bKmKjX"})[0].get_text()

        if result:
            result = self.regexer.read_data(TIME, result)[0]
            return result
        else:
            return 'There is nothing we can do.'
        
    def get_file_names(self, path):
        """
        Gets files' names from a folder
        """
        return os.listdir(path=path)

    def get_headers(self, link : str) -> list:

        return requests.get(url=link).headers
    def get_random_number(self, limit : int) -> int:
        return randint(0, limit)