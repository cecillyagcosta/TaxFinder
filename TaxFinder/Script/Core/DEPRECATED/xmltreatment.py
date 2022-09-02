from typing import final
import xmltodict

def takeICMS(_self_):
    return(_self_['imposto']['ICMS']['ICMS00']['vICMS'])

def takeIPI(_self_):
    return(_self_['imposto']['IPI']['IPITrib']['vIPI'])

def takenatOp(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['ide']['natOp'])

def takeNNF(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['ide']['nNF'])

def takeAllTaxes(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['det'][0])

def extractXMLInfo(_self_):
    infolist = []
    itemlist = []
    var = 1
    with open(_self_) as xmlfile:
        info = xmltodict.parse(xmlfile.read())
        xmlfile.close()
    infolist.append(takenatOp(info))
    infolist.append(takeNNF(info))
    for index in range(len(info['nfeProc']['NFe']['infNFe']['det'])): #Impostos em cada objeto
        itemlist.append(info['nfeProc']['NFe']['infNFe']['det'][index])
        index = index+1
    for each in itemlist:
        infolist.append([f'item {var}',takeICMS(each), takeIPI(each)])
        var = var+1
    return(infolist)

# 2 em diante são os itens da nota
info = extractXMLInfo('DANFE156933.xml')
print(info)





