import numpy as np

class LinearRegression:
    def __init__(self , epochs= 100 , learning_rate= 0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.cost_history = []


    def fit(self, X_train , y_train):

        features = X_train.shape[1]

        self.weights = np.zeros(features)
        self.bias = 0

        for epoch in range(self.epochs):

            predictions = self.predict(X_train)

            cost = self.compute_cost( y_train , predictions)
            self.cost_history.append(cost)

            dw , db = self.compute_gradients(X_train , y_train , predictions)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch + 1}: cost = {cost}")



    def predict(self , X ):
        predictions = np.dot(X , self.weights) + self.bias

        return predictions



    def compute_cost(self , y , predictions):

        error = predictions - y

        squared_error = np.square(error)

        mse = np.mean(squared_error)

        return mse



    def compute_gradients(self , X , y , predictions):

        error = np.subtract(predictions , y)

        m = X.shape[0]

        dw = (2 / m) * np.dot(X.T, error)

        db = 2 * np.mean(error)

        return dw, db

