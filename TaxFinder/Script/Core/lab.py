from base64 import decode
import pandas as pd 
import datetime
import os
import xmltreatment as xmlt
import logger as log
import time

import datafold as data

dir = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
#data.trackInvoice(dir)
subject = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/subject.txt'
current = datetime.datetime.now()
subCreation = time.ctime(os.path.getctime(subject))
subModification = time.ctime(os.path.getmtime(subject))
#print(subCreation)
#print(subModification)

def getCreationDate(filepath):
    return(time.ctime(os.path.getctime(filepath)))

def getModificationDate(filepath):
    return(time.ctime(os.path.getmtime(filepath)))

a = getCreationDate(subject)
print(a)