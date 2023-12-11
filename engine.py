import datetime
import time
import requests

from config import *

class Engine:
    
    def __init__(self) -> None:
        pass

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
    
    def get_headers(self, link : str) -> list:

        return requests.get(url=link).headers