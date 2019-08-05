import tensorflow as tf
import matplotlib.pyplot as plt
from pyramid.arima import auto_arima

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
    indicators.append(pd.read_csv("processed_data/index/"+filename))
for filename in stkname.symbol:
    stocks.append(pd.read_csv("processed_data/stocks/"+filename))

#print(indicators[0])
#print(stocks[0])

"""
Data preparation
"""
max0day = int(stocks[0].loc[stocks[0].iloc[:,1]==0].Date.max())

#stocks[0].iloc[max0day:,1:5].plot()
#plt.show()
data = stocks[0].iloc[max0day+1:].Close

"""
ARIMA
"""
train = data.iloc[:-730]
test = data.iloc[-730:]

stepwise_model = auto_arima(train)

print(stepwise_model.aic())