import os
import time
import datetime
from os import listdir
from os.path import isfile, join

def getCreationDate(filepath):
    return(datetime.datetime.fromtimestamp(os.path.getctime(filepath)))

def getModificationDate(filepath):
    return(datetime.datetime.fromtimestamp(os.path.getmtime(filepath)))



def createList(_self_):
    retrievedfiles = [f for f in listdir(_self_) if isfile(join(_self_, f))]
    return(retrievedfiles)

def getListCreationDate(_self_):
    lowList = []
    midList = []
    highList = []
    for each in _self_:
        lowList.append(str(getCreationDate(each)))
        for each in lowList:
            midList.append(each.split(" "))
            for each in midList:
                highList.append(midList[0])
    return(highList)

test = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/'
ex = createList(test)
dataList = getListCreationDate(ex)
mList = []
for each in dataList:
    print(each[0])