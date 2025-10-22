"""
Scratch implementation of activation functions used in ML.
"""

import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def linearization(w, X_train, b):
    return np.dot(w.T, X_train) + b
