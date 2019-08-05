import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime

#   FRED
#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2013, 1, 27)
#gdp = web.DataReader('GDP', 'fred', start, end)
#print(gdp.ix['2013-01-01'])


#   Stooq index data

USYB10 = web.DataReader('^DJI.', 'stooq')#'10USY.B', 'stooq')
#USYB2 = web.DataReader('2USY.B', 'stooq')
print(USYB10[:10])
