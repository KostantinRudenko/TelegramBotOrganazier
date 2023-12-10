import re

class RegexReader:
    def __init__(self):
        pass
    
    '''
        Function reads ALL data from the text message

        pattern - Regular Expression pattern
        text - Text message

        Returns a list of the founded results
    '''
    def read_data(self, pattern, text) -> list:
        return re.findall(pattern, text)
    
    '''
        Function tries to find any specific

        pattern - Regex pattern
        text - Text message
        value - specific value, which has to be found

        Returns a string if result was found else returns None
    '''
    def read_specific_data(self, pattern, text, value) -> str|None:
        return value if value in self.read_data(pattern, text) else None