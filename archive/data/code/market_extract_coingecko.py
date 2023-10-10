"""
Created on Tue Oct 27 20:49:41 2020
@author: Tammy Yang
coinGecko API for stablecoin market data request
"""
# ~/opt/anaconda3/envs/sraf/bin/pip install pycoingecko   
from pycoingecko import CoinGeckoAPI
import pandas as pd
import pickle as pk
import os
import json

dir_output = 'sraf/data/output/'

url_target='ping'

cg=CoinGeckoAPI()

# print(cg.ping())

# price

def market_extract(_id:str, _vs_currency:str = 'usd', _days:int = 11430, _interval:str = 'daily', save:bool = True):
        
    df_0 = pd.DataFrame(cg.get_coin_market_chart_by_id(id=_id, vs_currency=_vs_currency, days=_days, interval=_interval))
    df_price = pd.DataFrame(df_0['prices'].tolist(), index = df_0['prices'].index, columns = ('ts', 'price'))
    df_marketcap = pd.DataFrame(df_0['market_caps'].tolist(), index = df_0['market_caps'].index, columns = ('ts', 'marketcap'))
    df_volume = pd.DataFrame(df_0['total_volumes'].tolist(), index = df_0['total_volumes'].index, columns = ('ts', 'total_volumes'))
    df = df_price.join(df_marketcap.set_index('ts'), on = 'ts').join(df_volume.set_index('ts'), on = 'ts')
    df['ccy'] = _id

    if save == True:
        with open(dir_output+_id+".pk", "wb") as f:
               pk.dump(df, f) 

    return df

usdc_usd = market_extract(_id = "usd-coin")
busd_usd = market_extract(_id = "binance-usd")
usdt_usd = market_extract(_id = "tether")
dai_usd = market_extract(_id = "dai")
frax_usd = market_extract(_id = "frax")




usdc_usd = market_extract(_id = "usd-coin", _days = 10, _interval = 'hourly', save = False)
busd_usd = market_extract(_id = "binance-usd", _days = 10, _interval = 'hourly', save = False)
usdt_usd = market_extract(_id = "tether", _days = 10, _interval = 'hourly', save = False)
dai_usd = market_extract(_id = "dai", _days = 10, _interval = 'hourly', save = False)
frax_usd = market_extract(_id = "frax", _days = 10, _interval = 'hourly', save = False)










# api url https://www.coingecko.com/en/api/documentation
# 0x4fabb145d64652a948d72533023f6e7a623c7c53, id = "binance-usd" --busd
# 0x6b175474e89094c44da98b954eedeac495271d0f, id = "dai" --dai
# 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48, id = "usd-coin" --usdc
# 0xdac17f958d2ee523a2206206994597c13d831ec7, id = "tether" --usdt
# 0x853d955acef822db058eb8505911ed77f175b99e, id = "frax" --frax

