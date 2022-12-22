import os
from os import listdir
from os.path import isfile, join
import shutil
from datetime import date
import time
import datetime
import schedule as sch
from os.path import exists

Tempdir = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/Temp/'

def createList(_self_):
    retrievedfiles = [f for f in listdir(_self_) if isfile(join(_self_, f))]
    return(retrievedfiles)

def copyTodayFiles(_self_):
    dir = createList(_self_)
    currentDate = sch.getDateFromRaw() #.replace(currentDate, "21/Dec/2022")
    for each in dir:
        if sch.getCreationDate(f"{_self_}{each}") == currentDate and each.endswith(".xml"):
            shutil.copyfile(f"{_self_}{each}", f"{Tempdir}{each}")
            print(f"{each} was copied successfully. ")
        else:
            print(f"The file {each}({sch.getCreationDate(f'{_self_}{each}')}) is not on the target date ({sch.getDateFromRaw()}).")

def moveExcelToDir(_self_):
    destPath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/Conferência de Imposto/'
    dirList = createList(_self_)
    for each in dirList:
        if each.endswith(".xlsx"):
            if shutil.move(f"{_self_}{each}", f"{destPath}{each}"):
                print(f"{each} moved to destPath.")
            else:
                print(f"{each} had an error and wasn't moved to Onedrive.")

def destroyFiles(_self_):
    dirlist = createList(_self_)
    for each in dirlist:
        if os.remove(f"{_self_}{each}"):
            print(f"The file {each} was deleted.")
        elif len(os.listdir(_self_)) == 0:
            print("Empty dir.")