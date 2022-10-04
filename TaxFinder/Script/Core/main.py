import datafold as data

path = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/'
isolated = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/isolated/'
target = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/target/'
subject = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'
log = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/log/sentLog.txt'
#data.trackInvoice(target)
subject = data.invoiceList(target)
for each in subject:
    print(each)
