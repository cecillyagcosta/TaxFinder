from calendar import week
from datetime import datetime
from os.path import exists
from socket import gethostbyaddr
import logger
import time

from matplotlib.pyplot import get


current = datetime.now()
targetHour = current.replace(hour=15, minute=48)
str_dt = current.strftime("%d-%m-%Y, %H:%M:%S")
willIWork = True

def workSchedule(_self_):
    # Mon - Fri, 10:00 PM
    weekdays = ['Monday',
    'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday']
    today = datetime.weekday(_self_)
    if today < 5:
        if current == targetHour:
            print(f"deu bom! {weekdays[today]}, {current}")
        else:
            print(f"Ainda não! {weekdays[today]}, {current}")
    else:
        print("NULL")

def callUp(_self_):
    if _self_ == "Checking Time":
        workSchedule(current)
        print("1")
        return(callUp("Logging"))
    
    elif _self_ == "Logging":
        print("2")
        return(callUp("Recalling Method"))

    elif _self_ == "Recalling Method":
        print("3")
        return(callUp("Exception - Null - Empty String"))

    elif _self_ == "":
        print("NULL - Empty String")
        #logger.makeLog()
        return(callUp("Checking Time"))


while willIWork:
    callUp("")
    print(current)
    time.sleep(5)
