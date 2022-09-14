from base64 import decode
from re import X
from tarfile import TarInfo
from typing import final
from unicodedata import decimal
from unittest import skip
import pandas as pd 
from datetime import datetime
from os.path import *
from os import listdir
import xmltreatment as xmlt
import numpy as np
import xmltodict

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y")

testlist = ['Remessa de mercadoria em consignacao mercantil ou industrial',
'Entrada de mercadoria recebida em consignacao mercantil ou i',
'Remessa de bem por conta de contrato de comodato',
'Retorno de bem remetido por conta de contrato de comodato',
'Entrada de mercadoria recebida em consignação mercantil ou i',
'Remessa em bonificacao, doacao ou brinde',
'Remessa de amostra gratis',
'Venda de mercadoria adquirida ou recebida de terceiros, que',
'Remessa simbolica de mercadoria depositada em armazem geral',
'Devolucao de venda de mercadoria adquirida ou recebida de terceiros, que']

def forge(_self_):
    dataname = f'Notas {str_dt}.xlsx'
    data = pd.DataFrame.from_dict([_self_])
    if exists(dataname):
        #print("Excel encontrado, loggando.")
        finalframe = pd.DataFrame()
        frame = pd.read_excel(dataname)
        frame = frame.append(data)
        finalframe = finalframe.append(frame)
        finalframe.set_index("Natureza de Operação", inplace=True)
        #finalframe.to_excel(dataname, sheet_name='Notas de hoje')
        return(finalframe)
    else:
       # print("Excel não encontrado, criando e loggando.")
        data.set_index("Natureza de Operação", inplace=True)
      # data.to_excel(dataname)
    return(data)


targetpath = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Documentos/GitHub/TaxFinder/TaxFinder/Script/Core/isolated/DANFE158243.xml'

with open(targetpath, encoding='utf-8', mode='r') as xmlfile:
    info = xmltodict.parse(xmlfile.read())
    xmlfile.close()


ex = xmlt.extractXMLInfo(targetpath)
print(ex)

df = forge(ex)

print(df.head())
df = df[df['ICMS'] != 0]
df = df[df['IPI'] != 0]
print(df.head(20))
#print(df.info())