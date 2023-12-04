import datetime

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
            date = f"East:\n\t{date_data.day}-{date_data.month}-{date_data.year}\n\t{date_data.hour}:{date_data.minute}\nEast:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour}a.m.:{date_data.minute}"
        else:
            date = f"West:\n\t{date_data.month}-{date_data.day}-{date_data.year}\n\t{date_data.hour-12}p.m.:{date_data.minute}"
        
        return date