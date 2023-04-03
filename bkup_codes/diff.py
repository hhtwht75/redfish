#page 123
#Finding differential value
#If you need a partial different value, make other variables constant

import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f, x):
    
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def numerical_gradient(f, x):
    
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad
