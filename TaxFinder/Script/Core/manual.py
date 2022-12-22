import xmltreatment as xmlt
import datafold as data
import fileseparator as fsp


path = 'N:/NOTAS-FISCAIS/OneDrive - HARTMANN BRASIL/NFE - Fiscal/'
Tempdir = 'C:/Users/joao.costa/Documents/GitHub/TaxFinder/TaxFinder/Script/Core/Temp/'
fsp.copyTodayFiles(path)
data.trackInvoice(path)