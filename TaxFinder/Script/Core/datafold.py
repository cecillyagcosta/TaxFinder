from unittest import skip
import pandas as pd 
from datetime import datetime
from os.path import *
from os import listdir
import xmltreatment as xmlt


path = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/'

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y")

def forge(_self_):
    dataname = f'Notas {str_dt}.xlsx'
    data = pd.DataFrame.from_dict([_self_])
    if exists(dataname):
        print("it does!")
        finalframe = pd.DataFrame()
        frame = pd.read_excel(dataname)
        frame = frame.append(data)
        finalframe = finalframe.append(frame)
        finalframe.set_index("Natureza de Operação", inplace=True)
        finalframe.to_excel(dataname)
    else:
        print("it doesn't!")
        data.set_index("Natureza de Operação", inplace=True)
        data.to_excel(dataname)
    return(data)

def createDirList(_self_):
    retrievedfiles = [f for f in listdir(_self_) if isfile(join(_self_, f))]
    return(retrievedfiles)

def trackInvoice(_self_):
    poplist = createDirList(_self_)
    for each in poplist:
        if each.endswith('.xml'):
           targetInfo = xmlt.extractXMLInfo(each)
           if targetInfo["Natureza de Operação"] == 'Saída' or targetInfo["Natureza de Operação"] == 'Devolução':
                print()
