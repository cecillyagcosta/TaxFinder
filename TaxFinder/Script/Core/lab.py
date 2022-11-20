from base64 import decode
import pandas as pd 
from datetime import datetime, timedelta
from os.path import *
import xmltreatment as xmlt
import logger as log
import time


subject = 'C:/Users/joao.costa/OneDrive - HARTMANN BRASIL/Área de Trabalho/test.txt'

current = datetime.now()
target = current.replace(hour=12, minute=57) #(hour=13, minute=30)
if current >= target:
    with open(subject, 'w')as f:
        f.write(f"deu bom! current: {current} | target: {target}")
        f.close()
else:
    print(f"not yet. {current} | target: {target}")