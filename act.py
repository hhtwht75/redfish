#page 68
#Activation functions including sigmoid, Relu, and softmax function

import numpy as np

#step function
def step(x):

    return np.array(x > 0, dtype = np.int)

#sigmoid function
def sig(x):

    return 1 / (1 + np.exp(-x))

#ReLu function
def relu(x):

    return np.maximum(0, x)

#identity function
def iden(x):

    return x

#softmax function
def soft(x):

    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x

    return y
