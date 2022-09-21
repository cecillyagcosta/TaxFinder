from re import A
from tarfile import TarInfo
import tarfile
from typing import final
from unicodedata import decimal
from unittest import skip
import pandas as pd 
from datetime import datetime
from os.path import *
from os import listdir
import xmltreatment as xmlt
import logger as log

path = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/'
forgeLog = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/log/forgeLog.txt'
trackerLog = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/log/trackerLog.txt'
cuttedLog = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/log/cuttedLog.txt'
invPath = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/target/'

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y")


def forge(_self_):
    dataname = f'Notas {str_dt}.xlsx'
    data = pd.DataFrame.from_dict([_self_])
    if exists(dataname):
        print("Excel encontrado, loggando.")
        log.makeLog(forgeLog, _self_['Nota Fiscal'], 'Concatenação') #ForgeLog
        finalframe = pd.DataFrame()
        frame = pd.read_excel(dataname)
        frame = frame.append(data)
        finalframe = finalframe.append(frame)
        finalframe.set_index("Natureza de Operação", inplace=True)
        finalframe.to_excel(dataname, sheet_name='Notas de hoje')
    else:
        print("Excel não encontrado, criando e loggando.")
        log.makeLog(forgeLog, _self_['Nota Fiscal'], 'Criação') #ForgeLog
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
            targetInfo = xmlt.extractXMLInfo(f'{_self_}{each}')
            if targetInfo["ICMS"] == '0.00' and targetInfo["IPI"] == '0.00':
                print(f"Nota Desviada || Motivo: Sem imposto. Nota: {each}, natureza:{targetInfo['Natureza de Operação']}")
                log.makeLog(cuttedLog, targetInfo['Nota Fiscal'], 'Nota Desviada || Motivo: Sem imposto.')
            else:
                if targetInfo["Natureza de Operação"] == 'E/S Consignação':
                    print(targetInfo["Natureza de Operação"])
                    forge(targetInfo)
                elif targetInfo["Natureza de Operação"] == 'Devolução':
                    print(targetInfo["Natureza de Operação"])
                    forge(targetInfo)
                elif targetInfo["Natureza de Operação"] == 'Remessa em Comodato':
                    print(targetInfo["Natureza de Operação"])
                    forge(targetInfo)
                else:
                    print(f"Nota Desviada || Motivo: Natureza incorreta. {targetInfo['Natureza de Operação']}")
                    log.makeLog(cuttedLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota Desviada || Motivo: Natureza incorreta.')
    print(invoiceList())

def retrieveSent(file):
    finallist = []
    with open(file, 'r') as f:
        retrievedLog = f.read()
        f.close()
    loglist = retrievedLog.split(' -- ')
    for each in loglist:
        if each.endswith(".xml"):
            finallist.append(each)
    return(finallist)

def invoiceList():
    invoice_list = createDirList(invPath)
    dstinvoicepath_list = retrieveSent(cuttedLog)
    s = set(dstinvoicepath_list)
    invoicesToMove = [x for x in invoice_list if x not in s]
    return(invoicesToMove)