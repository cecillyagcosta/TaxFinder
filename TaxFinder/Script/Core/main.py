import csv
from typing import final
import xmltreatment as xmlt
import pandas as pd
import datafold as data
import logger

path = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/'

info = xmlt.extractXMLInfo('DANFE157899.xml')
info2 = xmlt.extractXMLInfo('DANFE157411.xml')
info3 = xmlt.extractXMLInfo('DANFE156933.xml')
#df = data.forge(info)
#df2 = data.forge(info2)
#df3 = data.forge(info3)

data.trackInvoice(path)