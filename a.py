import tensorflow as tf

from glob import glob
import pandas as pd
import datetime
import numpy as np

"""
read data
"""
idxname = pd.read_csv("data/index.csv", sep='\t')
stkname = pd.read_csv("data/stocks.csv", sep='\t')

indicators = []
stocks = []
for filename in idxname.filename:
    indicators.append(pd.read_csv("data/index/"+filename))
for filename in stkname.symbol:
    stocks.append(pd.read_csv("data/stocks/"+filename))

"""
(i) convert format "YYYY-MM-DD" to UTC timestamp
(ii) set the oldest date as offset (0)
"""
# (i)
for i in range(len(idxname)):
    if "(FRED)" in idxname.dataname[i]:
        indicators[i].rename(columns={"DATE": "Date"}, inplace=True)
    indicators[i]['Date'] = pd.to_datetime(indicators[i]['Date'], 
                            format='%Y-%m-%d', 
                            utc=True).astype(np.int64)/86400000000000
for i in range(len(stkname)):
    stocks[i]['Date'] = pd.to_datetime(stocks[i]['Date'], 
                            format='%Y-%m-%d', 
                            utc=True).astype(np.int64)/86400000000000
# (ii)
min_date = indicators[0].Date.min()
for idc in indicators:
    if min_date > idc.Date.min():
        min_date = idc.Date.min()
for idc in indicators:
    idc.Date -= min_date
for stk in stocks:
    stk.Date -= min_date

"""
Data interpolation
(i) Add Date 0 to maximum date
"""
n_idc = len(indicators)
n_stk = len(stocks)
for i in range(int(stocks[0].Date.max())+1):
    for j in range(n_idc):
        if not i in indicators[j].Date.tolist():
            indicators[j] = indicators[j].append({'Date': i}, ignore_index=True)
    for j in range(n_stk):
        if not i in stocks[j].Date.tolist():
            stocks[j] = stocks[j].append({'Date': i}, ignore_index=True)

#for i in range(int(stocks[0].Date.max())+1):
#    print(i)
#    for idc in indicators:
#        if not i in idc.Date.tolist():
#            idc = idc.append({'Date': i}, ignore_index=True)
#    for stk in stocks:
#        if not i in stk.Date.tolist():
#            stk = stk.append({'Date': i}, ignore_index=True)

"""
Save pre-pre-processed data
"""
for i in range(len(indicators)):
    indicators[i].sort_values(by=['Date']).to_csv("pre-pre-processed_data/index/"+idxname.filename[i], index=False)
for i in range(len(stocks)):
    stocks[i].sort_values(by=['Date']).to_csv("pre-pre-processed_data/stocks/"+stkname.symbol[i], index=False)