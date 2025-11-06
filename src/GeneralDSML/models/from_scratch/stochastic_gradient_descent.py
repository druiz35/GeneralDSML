"""
Scratch implementations of stochastic gradient descent.
"""

import numpy as np


class SimpleStochasticGradientDescent:
    def __init__(self, X, y_train, linearization, activation, loss, loss_dw, loss_db, cost, learning_rate):
        self.X = X
        self.y_train = y_train
        self.linearization = linearization
        self.activation = activation
        self.loss = loss
        self.loss_dw = loss_dw
        self.loss_db = loss_db
        self.cost = cost
        self.learning_rate = learning_rate
        self.w = np.zeros((X.shape[0], 1))
        self.b = 0

    def dw(self, X_len, A):
        return 1 / X_len * np.dot(self.X, (A - self.y_train).T)

    def forward_propagation(self):
        z = self.linearization(self.w, self.X, self.b)
        A = self.activation(z)
        return A

    def backward_propagation(self, A):
        # Update weights
        m = self.X.shape[1]
        calculated_loss = self.loss(A, self.y_train)
        calculated_cost = self.cost(calculated_loss, m)
        dw = 1 / m * self.loss_dw(self.X, self.y_train, A)
        db = 1 / m * self.loss_db(self.X, self.y_train, A)
        grads = {"dw": dw, "db": db}
        self.w -= self.learning_rate * dw
        self.b -= self.learning_rate * db
        return grads, calculated_cost

    def update_weights(self, pred, X):
        self.w = self.w + self.learning_rate * self.loss(self.y_train, pred) * X

    def run(self, iterations):
        # Cost accumulator
        costs = []
        # Optimizer loop
        for i in range(iterations):
            # forward_propagation
            A = self.forward_propagation()
            _, calculated_cost = self.backward_propagation(A)
            if i % 100 == 0:
                costs.append(calculated_cost)
        params = {"w": self.w, "b": self.b}
        return params, costs
