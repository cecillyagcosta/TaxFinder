import pandas as pd
import csv

def createRows(_self_):
    return(0)


def createCSV(_self_):
    fields = ['Tipo de nota', 'Data', 'No de Nota', 'ICMS', 'IPI']
    rows = [[_self_[0],_self_[2], _self_[1], _self_[3], _self_[4]]]
    with open('info899.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)
        file.close()

dic = {'Tipo de nota':'Saida', 'Data':'16/08/2022', 'ICMS':'0.00', 'IPI':'29683'}
listdeinformacoes = []
listdeinformacoes.append(dic['Tipo de nota'])
listdeinformacoes.append(dic['Data'])
listdeinformacoes.append(dic['ICMS'])
listdeinformacoes.append(dic['IPI'])

