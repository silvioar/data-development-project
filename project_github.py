# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:34:45 2021

@author: SilvioAranda
"""

import requests
import json
import pandas as pd
import threading
import time
import numpy as np
from sqlalchemy import create_engine
# import pymysql
from datetime import datetime

def print_log(text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    print('%s | %s' % (timestamp, text))

tickers = 'bitcoin,chainlink,ethereum,reserve-rights-token,cardano,polkadot,crypto-com-chain'
url = f'https://api.coingecko.com/api/v3/simple/price?ids={tickers}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true'
headers = {"accept: application/json"}

print_log("##############################################################################################")
print_log("Comenzando ...")
print_log("##############################################################################################")

print_log('Haciendo la request...')
r = requests.get(url = url, verify = False)
output = r.json()
print_log('Creando Dataframe...')
df = pd.DataFrame(output).T

def get_engine():
    return create_engine("mysql+pymysql://*****:*********@*********/**********")

def escribir_base(df, tabla):
    df.reset_index().to_sql(tabla, index=False, con=get_engine(), if_exists='replace')
    
df = df.reset_index()
df.columns = [['moneda','precio','market_cap','volumen']]

# Elimino multiindex y los parentesis dentro de los nombres de cada columna
df.columns = df.columns.get_level_values(0)

# Guardar en base
print_log('Escribiendo en la base...')
escribir_base(df, 'test')

print_log('Actualización terminada...')
