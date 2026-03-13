"""
Scratch implementation of activation functions used in ML.
"""

import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return (np.exp(z) - np.exp(-z))/(np.exp(z) + np.exp(-z))

def relu(z):
    return np.max(0, z)

def leaky_relu(leak=0.01, z):
    return np.max(leak*z, z)
