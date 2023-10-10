# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:24:34 2020
@author: Tammy Yang
@description: BTC and Ether price data extraction from coinbase pro api
"""
import pandas as pd
import numbpy as np
import requests
from datetime import timedelta,date
import time


####################################################################################################################
def coinbasepro_api_requset(t_start, t_end, granularity ,ccy):
    """
    Coinbase pro historical rate api request function
    t_start:         multiple of 300 that are required to be deducted from start time
    t_end:           multiple of 300 that are required to be deducted from end time
    granularity:     frequency of the cata
    ccy:             cryptocurrency type
    """
    
    url_cp = 'https://api.pro.coinbase.com'   
    path_cp_rate = '/products/' + ccy + '-USD/candles'
    
    #path_cp_time = '/time'
    param_cp_rate = {
        'start': t_start
        ,'end': t_end
        ,'granularity': granularity #hourly frequency
        }
    response_cp = requests.get(url_cp + path_cp_rate, params = param_cp_rate)
    
    print(response_cp.status_code)
    df_rate = pd.DataFrame(response_cp.json(),columns = ['time_unix','low','high','open','close','volume'])
    df_rate = df_rate.assign(time = pd.to_datetime(df_rate['time_unix'], unit = 's')) 
    #df_rate=response_cp.json()
    return df_rate


coinbasepro_api_requset(t_start = 1678320000, t_end = 1678812152, granularity = 'hourly' ,ccy = 'USDC')