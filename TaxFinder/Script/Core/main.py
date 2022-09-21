import csv
from typing import final
import xmltreatment as xmlt
import pandas as pd
import datafold as data
import logger

path = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Documentos/GitHub/TaxFinder/TaxFinder/Script/Core/ex/'
isolated = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/isolated/'
prod = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Documentos/GitHub/TaxFinder/TaxFinder/Script/Core/prod/'
setembro = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Documentos/GitHub/TaxFinder/TaxFinder/Script/Core/setembro/'
digjoy = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/setembro/'
target = 'C:/Users/JHGC1/OneDrive/Documents/TaxFinder/TaxFinder/Script/Core/target/'
#data.trackInvoice(path)
#data.trackInvoice(isolated)
#data.trackInvoice(prod)
#data.trackInvoice(digjoy)
data.trackInvoice(target)