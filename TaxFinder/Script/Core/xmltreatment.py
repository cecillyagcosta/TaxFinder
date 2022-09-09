import xmltodict

def takeDate(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['ide']['dhEmi'])

def makeFormatedDate(_self_): #2022-08-05T15:58:00-03:00   
    fst = _self_.split('T')
    scnd = str(fst[0]).split('-')
    trd = f'{scnd[2]}/{scnd[1]}/{scnd[0]}'
    return(trd)

def takeICMS(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vICMS'])

def takeIPI(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vIPI'])

def takenatOp(_self_):
    nat = _self_['nfeProc']['NFe']['infNFe']['ide']['natOp']
    if nat == 'Entrada de mercadoria recebida em consignacao mercantil ou i':
        return('Devolucao')
    elif 'Remessa de mercadoria em consignacao mercantil ou industrial':
        return('Saida')
    else:
        return(nat)

def takeNNF(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['ide']['nNF'])

def takeAllTaxes(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['det'][0])

def extractXMLInfo(_self_):
    infolist = []
    itemlist = []
    index = 0
    with open(_self_) as xmlfile:
        info = xmltodict.parse(xmlfile.read())
        xmlfile.close()
    infolist.append(takenatOp(info))
    infolist.append(takeNNF(info))
    infolist.append(makeFormatedDate(takeDate(info)))
    infolist.append(takeICMS(info))
    infolist.append(takeIPI(info))
    return(infolist)