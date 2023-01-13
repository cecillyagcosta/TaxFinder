import datafold as data
import schedule as sch
import time
import datetime
import logger
import fileseparator as filesep

log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/Mainlog.txt'
dir = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'

def callUp(_self_):
    if _self_ == "Checking Time":
        print(f"Checking time on {sch.getTimeFromDate()}")
        if sch.workSchedule(sch.getTimeFromDate()) == True:
            logger.makeLog(log, "Checking Time -- Trigged", f"{sch.getTimeFromDate()}")
            return(callUp("Recalling method"))
        else:
            return(callUp("Recalling method"))
    elif _self_ == "Recalling Method":
        print(f"Recalling method on {sch.getTimeFromDate()}")
        return(callUp("Checking Time"))

    elif _self_ == "Cycle":
        return(callUp("Checking Time"))

try:
    while True:
        callUp("Cycle")
        print(sch.getTimeFromDate())
        time.sleep(1)
except:
    print("erro!")