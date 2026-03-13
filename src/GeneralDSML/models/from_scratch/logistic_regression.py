"""
Implementing logistic regression from scratch
"""

import numpy as np


class LogisticRegressionFromScratch:
    def __init__(self, activation): 
        self.linearization = self.z
        self.activation = activation
        self.parameters = {
            "W": None,
            "b": None
        }

    def initialize_parameters(self, dim): 
        self.parameters["W"] = np.zeros((dim, 1))
        self.parameters["b"] = 0.0

    def z(self, X):
        return np.dot(self.parameters["W"], X) + self.parameters["b"]

    def loss(y, y_hat): 
        return -y * np.log(y_hat) - (1-y)*np.log(1-y_hat)

    def loss_dw(X, y, y_hat):
        return np.dot(X, (y_hat-y).T)

    def loss_db(X, y, y_hat):
        return np.sum(A-y)

    def cost(L, X_len):
        return 1/X_len * np.sum(L)
