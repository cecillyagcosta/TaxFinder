import csv
from typing import final
import xmltreatment as xmlt
import pandas as pd


info = xmlt.extractXMLInfo('DANFE157411.xml')
print(info)
for each in info:
    print(each)
df = pd.read_csv('info899.csv')
df.index = df['Tipo de nota']
df = df.drop('Tipo de nota', axis=1)
print(df.head())
df.to_excel('exemplofinal.xlsx')