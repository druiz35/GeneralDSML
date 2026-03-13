import numpy as np


# STOCHASTIC GRADIENT DESCENT
class SimpleStochasticGradientDescentFromScratch:
    def __init__(self, X, y_train, model, learning_rate):
        self.X = X
        self.y_train = y_train
        self.linearization = model.linearization
        self.activation = model.activation
        self.loss = model.loss
        self.loss_dw = model.loss_dw
        self.loss_db = model.loss_db
        self.cost = model.cost
        self.learning_rate = learning_rate

    def forward_propagation(self):
        z = self.linearization(self.X)
        y_hat = self.activation(z)
        return y_hat

    def backward_propagation(self, y_hat):
        # Update weights
        m = self.X.shape[1]
        calculated_loss = self.loss(y_hat, self.y_train)
        calculated_cost = self.cost(calculated_loss, m)
        dw = 1 / m * self.loss_dw(self.X, self.y_train, y_hat)
        db = 1 / m * self.loss_db(self.X, self.y_train, y_hat)
        grads = {"dw": dw, "db": db}
        self.model.w -= self.learning_rate * dw
        self.model.b -= self.learning_rate * db
        return grads, calculated_cost

    def run(self, iterations):
        # Cost accumulator
        costs = []

        # Initiaalize parameters
        self.model.initialize_parameters(dim=self.X.shape[0])

        # Optimizer loop
        for i in range(iterations):
            # forward_propagation
            A = self.forward_propagation()
            _, calculated_cost = self.backward_propagation(A)
            if i % 100 == 0:
                costs.append(calculated_cost)
        params = {"w": self.model.w, "b": self.model.b}
        return params, costs
