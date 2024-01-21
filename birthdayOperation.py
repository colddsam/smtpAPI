import json
from datetime import datetime
from zoneinfo import ZoneInfo

class BirthDayInfo:
    
    def __init__(self) -> None:

        self.time = str(datetime.now(tz=ZoneInfo("Asia/Kolkata")).day)+'-' +str(datetime.now(tz=ZoneInfo("Asia/Kolkata")).month)
    
    def birthdayName(self)->str:
        with open('./dataset.json','r') as f:
            file=json.load(f)
            
        if self.time in file:
            return file[self.time]
        else:
            return "Unknown"

