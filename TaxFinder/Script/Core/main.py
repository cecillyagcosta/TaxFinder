import datafold as data
import schedule as sch
import time
import datetime
import logger

log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/Mainlog.txt'

def callUp(_self_):
    if _self_ == "Checking Time":
        print(f"Checking time on {sch.getTime()}")
        if sch.workSchedule(sch.getTime()) == True:
            logger.makeLog(log, "Checking Time -- Trigged", f"{sch.getTime()}")
            return(callUp("Recalling method"))
        else:
            logger.makeLog(log, "Checking Time -- not trigged", f"{sch.getTime()}")
            return(callUp("Recalling method"))

    elif _self_ == "Recalling Method":
        print(f"Recalling method on {sch.getTime()}")
        logger.makeLog(log, "Recalling method", f"{sch.getTime()}")
        return(callUp("Moving files"))

    elif _self_ == "Moving files":
        print(f"Moving files on {sch.getTime()}")
        logger.makeLog(log, "Recalling method", f"{sch.getTime()}")
        return(callUp("Checking Time"))

    elif _self_ == "Cycle":
        logger.makeLog(log, "Starting cycle on", f"{sch.getTime()}")
        return(callUp("Checking Time"))

while True:
        callUp("Cycle")
        print(sch.getTime())
        time.sleep(1)