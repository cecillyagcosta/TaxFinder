from base64 import decode
import pandas as pd 
import datetime
import os
import xmltreatment as xmlt
import logger as log
import time
import schedule as sch
import datafold as data
import fileseparator as fsp
dir = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
#data.trackInvoice(dir)
subject = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/subject.txt'
test1 = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
say = sch.getCreationDate(subject)
me = sch.getDateFromRaw()
print(say)
print(me)
dirlist = fsp.createList(test1)

data.trackInvoice(test1)
print("etevaldo")