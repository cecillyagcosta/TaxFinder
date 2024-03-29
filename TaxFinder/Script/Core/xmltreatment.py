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
        return('Devolução')
    elif nat == 'Devolucao de mercadoria remetida em consignacao mercantil ou':
        return('Devolução')
    elif nat == 'Remessa de bem por conta de contrato de comodato':
        return('Remessa em Comodato')
    elif nat == 'Retorno de bem remetido por conta de contrato de comodato':
        return('Remessa em Comodato')
    elif nat == 'Remessa de mercadoria em consignacao mercantil ou industrial':
        return('E/S Consignação')
    else:
        print(f"Nota Desviada. Natureza: {nat}")

def takeNNF(_self_):
    return(_self_['nfeProc']['NFe']['infNFe']['ide']['nNF'])

def extractXMLInfo(_self_):
    with open(_self_, encoding='utf-8', mode='r') as xmlfile:
        info = xmltodict.parse(xmlfile.read())
        xmlfile.close()
    infolist = {"Natureza de Operação":(takenatOp(info)),
                "Nota Fiscal":(takeNNF(info)),
                "Data":(makeFormatedDate(takeDate(info))),
                "ICMS":(takeICMS(info)),
                "IPI":(takeIPI(info)) }
    return(infolist)