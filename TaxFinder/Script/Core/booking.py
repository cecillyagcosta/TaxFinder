from calendar import week
from datetime import datetime
from os.path import exists

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

weekday = datetime.weekday()
if weekday < 5:
    print("sim, é")