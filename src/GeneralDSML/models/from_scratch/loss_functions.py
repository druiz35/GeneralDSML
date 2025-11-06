"""
Scratch implementations of loss functions used in ML
"""

import numpy as np


def log_loss(Y_pred, Y_real):
    return -Y_pred * np.log(Y_real) - (1 - Y_pred) * np.log(1 - Y_real)


def average_cost(L, n_train_samples):
    return 1 / n_train_samples * np.sum(L)
