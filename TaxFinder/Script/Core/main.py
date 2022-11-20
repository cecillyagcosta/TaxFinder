import datafold as data
import schedule as sch
import time
import datetime

path = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/'
isolated = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/isolated/'
target = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
subject = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'
log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/sentLog.txt'
targetDell = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Documentos/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
current = datetime.datetime.now()
workTime = current.replace(hour=22)
willIWork = True
data.trackInvoice(targetDell)


def callUp(_self_):
    if _self_ == "Checking Time":
        sch.workSchedule(current)
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
