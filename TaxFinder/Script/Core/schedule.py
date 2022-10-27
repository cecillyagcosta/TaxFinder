from calendar import week
from datetime import datetime
from os.path import exists
from socket import gethostbyaddr

from matplotlib.pyplot import get

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

def getDayOfWeek(_self_):
    weekdays = ['Monday',
    'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday']
    today = datetime.weekday(_self_)
    return(weekdays[today])

def workingDays():
    currentDay = getDayOfWeek(dt)
    workDays = ['Monday',
    'Tuesday', 'Wednesday',
     'Thursday', 'Friday']
    for each in workDays:
        if each == currentDay:
            print("I should work today!")
            print(f'Today is {currentDay}')
        else:
            print("I shouldn't work today!")

def checkHour(_self_): #Would use str_dt
    currentHour = _self_.split(',')
    targetHour = "17:01:00"
    amIWorking = False
    if targetHour == currentHour:
        #it's time to work
        amIWorking = True
        return(amIWorking)
    else:
        amIWorking = False
        return(amIWorking)
    
isItWorking = checkHour(str_dt)

while True:
    if isItWorking == True:
        print(isItWorking)
        break
   
    

