from calendar import week
from datetime import datetime
from os.path import exists
from socket import gethostbyaddr

from matplotlib.pyplot import get

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

def workSchedule(_self_):
    # Mon - Fri, 10:00 PM
    weekdays = ['Monday',
    'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday']
    today = datetime.weekday(_self_)
    if today < 5:
        return()
    else:
        print("weekend!")


print(workSchedule(dt))