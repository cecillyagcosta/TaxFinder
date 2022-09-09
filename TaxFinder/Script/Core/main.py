import csv
from typing import final
import xmltreatment as xmlt
import pandas as pd

def createCSV(_self_):
    fields = ['Tipo de nota', 'Data', 'No de Nota', 'Item', 'ICMS', 'IPI']
    rows = [[_self_[0],_self_[2], _self_[1], _self_[3][0], _self_[3][1], _self_[3][2]]]
    with open('info899.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)
        file.close()

info = xmlt.extractXMLInfo('DANFE157899.xml')
print(info)
for each in info:
    print(each)
createCSV(info)
df = pd.read_csv('info899.csv')
df.to_excel('info899.xlsx')