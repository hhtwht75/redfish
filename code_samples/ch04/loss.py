#page 113

import numpy as np
import matplotlib.pyplot as plt

#mean_squared_error

def mse(y,t):
    return 0.5 * np.sum((y-t)**2)

#cross_entropy_error(y,t):

def cee(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

def batch_cee(y,t):
    
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

        batch_size = y.shape[0]
        return -np.sum(t*np.log(y+1e-7)) / batch_size

def batch_onehot_cee(y,t):

    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

        batch_size = y.shape[0]
        return -np.sum(np.log(y[np.arange(batch_size),t] + 1e-7)) / batch_size


