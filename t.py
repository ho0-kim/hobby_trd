import numpy as np

try:
    #if np.isnan(np.nan):
    #if np.isnan('.'):
    if np.isnan(15235.0):
        print('a')
except TypeError:
    print('b')
