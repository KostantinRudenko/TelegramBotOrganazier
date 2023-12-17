import datetime
import time
import requests

from requests import Session
from config import *
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By

class Engine:
    
    def __init__(self) -> None:
        self.session = Session()

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
    
    def get_weather(self, city : str):
        params = {'q' : 'weather in {city}'.format(city=city)}
        response = self.session.get(url=GOOGLE, params=params)

        driver = webdriver.Chrome(executable_path=CHROME_PATH)
        driver.get(response.url)

        temp= driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text

        wet = driver.find_element(By.XPATH, '//*[@id="wob_hm"]').text

        rain =driver.find_element(By.XPATH, '//*[@id="wob_pp"]').text
        
        if temp and wet and rain:

            result = f'{city}:\nТеспература: {temp}\nВлажность: {wet}\nОсадки: {rain}'
            return result
        else:
            return f'No weather information found for {city}.'

    def get_headers(self, link : str) -> list:

        return requests.get(url=link).headers
    
    def get_content(self, link : str):

        return requests.get(url=link).content

    def get_random_number(self, limit : int) -> int:
        return randint(0, limit)