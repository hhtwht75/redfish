
#page 68

import numpy as np

def step(x):

    return np.array(x > 0, dtype = np.int)

def sig(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)
