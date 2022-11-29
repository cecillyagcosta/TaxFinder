from calendar import week
from datetime import datetime
from os.path import exists
import logger
import time
import datafold as data

path = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/'
onedrivePath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/Conferência de Imposto/'
invPath = 'Y:/TaxPlus/NFe/Produção/Visualizar XML/'
examplePath = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log.txt'

def getTime():
    return(datetime.now())

str_dt = getTime().strftime("%d-%m-%Y, %H:%M:%S")
willIWork = True

def workSchedule(_self_):
    current = getTime()
    targetHour = current.replace(hour=21, minute=59, second=59)
    # Mon - Fri, 10:00 PM
    weekdays = ['Monday',
    'Tuesday', 'Wednesday',
    'Thursday', 'Friday',
    'Saturday', 'Sunday']
    today = datetime.weekday(_self_)
    if today < 5:
        if current == targetHour:
            data.trackInvoice(examplePath)
            return(True)
        else:
            print(f"not yet. {weekdays[today]}, {current} || target: {targetHour}: Next cycle in: {targetHour - current}")
            return(False)
    else:
        return(False)

