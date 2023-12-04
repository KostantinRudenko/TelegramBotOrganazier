import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

from config import *

class Engine:
    
    def __init__(self) -> None:
        pass

    def get_time(self):
        '''
        gets time
        '''
        date_data = datetime.datetime.now()
        hour_time = date_data.hour
        
        if hour_time <= 12:
            date = f"East:\n\t{date_data.day}-{date_data.month}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}\nWest:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour}a.m.:{date_data.minute}"
        else:
            date = f"East:\n\t{date_data.day}-{date_data.month}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}\nWest:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour-12}p.m.:{date_data.minute}"
        
        return date

class PageObject:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager(path='D:\Python\TelegramBotOrganazier\chromedriver.exe').install()))
        self.browser.set_window_size(1336,800)
    
    def open_browser(self, url):
        self.browser.get(url)
    
    def find_block(self, xpath, is_block = True):
        result = self.browser.find_element(By.XPATH, xpath)
        if is_block:
            pass
        else:
            result = result.text
        return result
    
    def get_courses(self) -> list:
        self.open_browser(DOLLAR)
        dollar_course = self.find_block(xpath='//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]', is_block=False)
        self.open_browser(EURO)
        euro_cousrse = self.find_block(xpath='//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]', is_block=False)
        return [dollar_course, euro_cousrse]