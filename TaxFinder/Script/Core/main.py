import csv
from typing import final
import xmltreatment as xmlt
import pandas as pd

def createCSV(_self_):
    fields = ['Tipo de nota', 'Data', 'No de Nota', 'ICMS', 'IPI']
    rows = [[_self_[0],_self_[2], _self_[1], _self_[3], _self_[4]]]
    with open('info899.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)
        file.close()

info = xmlt.extractXMLInfo('DANFE157411.xml')
print(info)
for each in info:
    print(each)
createCSV(info)
df = pd.read_csv('info899.csv')
df.index = df['Tipo de nota']
df = df.drop('Tipo de nota', axis=1)
print(df.head())
#df.to_excel('exemplofinal.xlsx')