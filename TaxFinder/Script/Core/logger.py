from datetime import datetime
from os.path import exists

dt = datetime.now()
str_dt = dt.strftime("%d-%m-%Y, %H:%M:%S")

def makeLog(path, _self_, _self1_):
    file_exists = exists(path)
    if(file_exists):
        with open(path, 'a') as f:
            f.write(f'{_self_} -- {_self1_} -- {str_dt} \n')
            f.close()
    else:
        with open(path, 'w') as g:
            g.write('---- LOG BEGIN ----\n')
            g.write(f'{_self_} -- {_self1_} -- {str_dt} \n')
            g.close()