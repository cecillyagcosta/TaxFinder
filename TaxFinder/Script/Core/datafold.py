from base64 import decode
import pandas as pd 
from datetime import datetime
from os.path import *
from os import listdir
import xmltreatment as xmlt
import logger as log

forgeLog = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/forgeLog.txt'
cuttedLog = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/cuttedLog.txt'
sentLog = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/sentLog.txt'
invPath = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/'

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

def checkSentLog():
    if exists(sentLog):
        return(True)
    else:
        with open(sentLog, 'w') as f:
            f.write('---- LOG BEGIN ----\n')
            f.close()
        return(True)

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

def invoiceList(_self_):
    invoice_list = createDirList(_self_)
    dstinvoicepath_list = retrieveSent(sentLog)
    s = set(dstinvoicepath_list)
    invoicesToMove = [x for x in invoice_list if x not in s]
    return(invoicesToMove)

def trackInvoice(_self_):
    isLog = checkSentLog()
    if isLog:
        poplist =  invoiceList(_self_)
        for each in poplist:
            if each.endswith('.xml'):
                targetInfo = xmlt.extractXMLInfo(f'{_self_}{each}')
                if targetInfo["ICMS"] == '0.00' and targetInfo["IPI"] == '0.00':
                    print(f"Nota Desviada || Motivo: Sem imposto. Nota: {each}, natureza:{targetInfo['Natureza de Operação']}")
                    log.makeLog(cuttedLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota Desviada || Motivo: Sem imposto.')
                else:
                    if targetInfo["Natureza de Operação"] == 'E/S Consignação':
                        print(targetInfo["Natureza de Operação"])
                        log.makeLog(sentLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota registrada || E/S Consignação')
                        forge(targetInfo)
                    elif targetInfo["Natureza de Operação"] == 'Devolução':
                        log.makeLog(sentLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota registrada || Devolução')
                        forge(targetInfo)
                    elif targetInfo["Natureza de Operação"] == 'Remessa em Comodato':
                        log.makeLog(sentLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota registrada || Remessa em Comodato')
                        forge(targetInfo)
                    else:
                        print(f"Nota Desviada || Motivo: Natureza incorreta. {targetInfo['Natureza de Operação']}")
                        log.makeLog(cuttedLog, str(targetInfo['Nota Fiscal']+'.xml'), 'Nota Desviada || Motivo: Natureza incorreta.')