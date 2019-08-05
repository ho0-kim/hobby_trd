import tensorflow as tf

from glob import glob
import pandas as pd
import datetime
import numpy as np
import math

"""
read data
"""
idxname = pd.read_csv("data/index.csv", sep='\t')
stkname = pd.read_csv("data/stocks.csv", sep='\t')

indicators = []
stocks = []
for filename in idxname.filename:
    indicators.append(pd.read_csv("pre-pre-processed_data/index/"+filename))
for filename in stkname.symbol:
    stocks.append(pd.read_csv("pre-pre-processed_data/stocks/"+filename))

"""
Data interpolation
"""
n_idc = len(indicators)
n_stk = len(stocks)

for i in range(n_idc):
    if np.isnan(indicators[i].iloc[0,1]):
        indicators[i].iloc[0,1:] = 0
for i in range(n_stk):
    if np.isnan(stocks[i].iloc[0,1]):
        stocks[i].iloc[0,1:] = 0

max_time = stocks[0].Date.max()

for i in range(1, int(max_time)+1):
    print(i)
    for inc in indicators:
        try:
            if np.isnan(float(inc.iloc[i,1])):
                inc.iloc[i,1:] = inc.iloc[i-1,1:]
        except:
            inc.iloc[i,1:] = inc.iloc[i-1,1:]
    for stk in stocks:
        try:
            if np.isnan(float(stk.iloc[i,1])):
                stk.iloc[i,1:] = stk.iloc[i-1,1:]
        except:
            stk.iloc[i,1:] = stk.iloc[i-1,1:]

"""
Save pre-processed data
"""
for i in range(n_idc):
    indicators[i].sort_values(by=['Date']).to_csv("processed_data/index/"+idxname.filename[i], index=False)
for i in range(n_stk):
    stocks[i].sort_values(by=['Date']).to_csv("processed_data/stocks/"+stkname.symbol[i], index=False)