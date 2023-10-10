"""
Created on Tue Oct 27 20:49:41 2020
@author: Tammy Yang
data visualisation
"""

import pandas as pd
import pickle as pk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

dir = 'sraf/data/output/'
window_list = [7, 30, 120, 365]

dict_market = {}
i=0
for file in os.listdir(dir):
    if file.endswith('.pk'):
        dict_market[i] = pd.read_pickle(dir + file)
        i=i+1

for d in dict_market:
    for w in window_list:
        dict_market[d]['vol_'+str(w)] = np.sqrt((((dict_market[d]['price']-1)**2).rolling(w).sum())/w)
 
df_market = pd.concat(dict_market, axis=0, ignore_index = True)

df_market['ts'] = pd.to_datetime(df_market['ts'],unit='ms')


# Visualisation 
ignore_list = ['ts','ccy']
ccy_list = df_market['ccy'].unique()

for col in df_market:

    if col == 'vol_7':
        title= 'Rolling 7-day price volatility from 1 USD'
    elif col == 'vol_30':
        title= 'Rolling 30-day price volatility from 1 USD'
    elif col == 'vol_120':
        title= 'Rolling 120-day price volatility from 1 USD'
    elif col == 'vol_365':
        title= 'Rolling 365-day price volatility from 1 USD'
    else:
        title=col.upper()
    print(title)

    if col not in ignore_list:
        fig, axs = plt.subplots(nrows=len(ccy_list), figsize=(30, 30))
        for i,v in enumerate(ccy_list):
            sns.lineplot(x='ts', y=col, data=df_market.loc[df_market['ccy']==v], ax=axs[i]).set(title = v.upper()+': ' + title)
        # plt.show()
        plt.savefig(dir+ 'figures/' + col + '.png')
        plt.clf()




