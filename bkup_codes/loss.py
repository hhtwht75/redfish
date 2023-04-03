#page 113
#loss function

import numpy as np
import matplotlib.pyplot as plt

#mean_squared_error

def mse(y,t):
    return 0.5 * np.sum((y-t)**2)

#cross_entropy_error(y,t):

def cee(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))
