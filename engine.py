import datetime
import time

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