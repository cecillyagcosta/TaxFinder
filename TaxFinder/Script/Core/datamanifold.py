import pandas as pd 
from datetime import datetime

dt = datetime.now()
str_dt = dt.strftime("%d/%m/%Y")

def forgeExcel(_self_):
    #raw = pd.Series(_self_, )
    data = pd.DataFrame.from_dict([_self_])
    return(data)

alpha = {"glasses":"briller", "wolves":"ulver", "birds":"fugler"}
test = forgeExcel(alpha)
print(test.head())