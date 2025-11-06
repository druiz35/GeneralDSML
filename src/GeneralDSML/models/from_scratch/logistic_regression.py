"""
Implementing logistic regression from scratch
"""

import numpy as np


def sigmoid_activation(x):
    return 1 / (1 + np.exp(-x))


# Cost and loss
def logistic_loss(y, A):
    return -y * np.log(A) - (1 - y) * np.log(1 - A)


def logistic_loss_dw(X, y, A):
    return np.dot(X, (A - y).T)


def logistic_loss_db(X, y, A):
    return np.sum(A - y)


def cost(L, X_len):
    return 1 / X_len * np.sum(L)
