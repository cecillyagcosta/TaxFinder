from calendar import week
from datetime import datetime
from os.path import exists
import os.path
import logger
import time
import datafold as data
import fileseparator as fsp
import shutil

Mainpath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'
corePath = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/'
tempPath = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/Temp/'
log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log.txt'
willIWork = True


def getTimeFromDate():
    return(datetime.now())

def getRawTime():
    current = time.time()
    return(time.ctime(current))

def getDateFromRaw():
    date = getRawTime().split()
    finaldate = f"{date[2]}/{date[1]}/{date[4]}"
    return(finaldate)

def getCreationDate(filepath):
    date = time.ctime(os.path.getctime(filepath)).split()
    finaldate = f"{date[2]}/{date[1]}/{date[4]}"
    return(finaldate)

def getModificationDate(filepath):
    date = time.ctime(os.path.getmtime(filepath)).split()
    finaldate = f"{date[2]}/{date[1]}/{date[4]}"
    return(finaldate)

str_dt = getTimeFromDate().strftime("%d-%m-%Y, %H:%M:%S")

def workSchedule(_self_):
    current = getTimeFromDate()
    targetHour = current.replace(hour=22, minute=0, second=0)
    # Mon - Fri, 10:00 PM
    weekdays = ['Monday',
    'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday']
    today = datetime.weekday(_self_)
    if today < 5:
        if current == targetHour:
            print("It's time!")
            fsp.copyTodayFiles(Mainpath)
            data.trackInvoice(tempPath)
            fsp.destroyFiles(tempPath)
            fsp.moveExcelToDir(corePath)
            return(True)
        else:
            print(f"Not yet. Next cycle in: {targetHour - current}")
            return(False)
    else:
        return(False)