import numpy as np
from sklearn import  linear_model

class pricePredictor:

    def __init__(self):
        # Data
        # Utilization rate
        data = np.array([0, 0.3, 0.5, 0.9, 1]).reshape(-1, 1)
        # Price
        target = np.array([1, 7, 10, 15, 20]).reshape(-1, 1)

        # Create linear regression object
        self.regr = linear_model.LinearRegression()

        # Train the model using the training sets
        self.regr.fit(data, target)

    def get_price(self,utilization_rate):
        # Make predictions using the utilization_rate
        predicion = self.regr.predict(utilization_rate)
        return round(float(predicion),2)

