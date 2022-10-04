from base64 import decode
import pandas as pd 
from datetime import datetime
from os.path import *
import xmltreatment as xmlt
import logger as log
import time

def retrieveSent(file):
    finallist = []
    if exists(file):
        with open(file, mode='r') as f:
            retrievedLog = f.read()
            f.close()
        loglist = retrievedLog.split()
        for each in loglist:
            if each.endswith('.xml'):
                finallist.append(each)
        return(finallist)


log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/sentLog.txt'

files = retrieveSent(log)

ex = getctime(log)
ex2 = getmtime(log)
print(ex)

creation_ex = time.ctime(ex)
modification_ex = time.ctime(ex2)
print(creation_ex)
print(modification_ex)


