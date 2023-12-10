import datetime
import time

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
            date = f"East:\n\t{date_data.day}-{date_data.month}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}\nWest:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}a.m."
        else:
            date = f"East:\n\t{date_data.day}-{date_data.month}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}\nWest:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour-12}:{date_data.minute}p.m."
        
        return date
    
    def start_timer(self, setted_time):
        while True:
            time_now = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
            if setted_time != time_now:
                pass
            else:
                return "Пора на Донбасс!"