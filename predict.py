import numpy as np
import pandas as pd

class Predict:
    def __init__(self):
        self.theta0 = 0.90
        self.theta1 = -0.90
        self.mileage = 0
        self.mileage_normalized = 0
        
    def load_thetas(self):
        df = pd.read_csv('data.csv')
        self.x = df.iloc[:, 0].values
        self.y = df.iloc[:, 1].values

    def estimate_price(self):
        # calc = self.theta0 + (self.theta1 * self.mileage)
        # calc = calc * (np.max(self.y) - np.min(self.y)) + np.min(self.y)
        predicted_price_normalized = self.theta0 + (self.theta1 * self.mileage_normalized)
        predicted_price = predicted_price_normalized * (np.max(self.y) - np.min(self.y)) + np.min(self.y)
        return predicted_price
        # return self.theta0 + (self.theta1 * self.mileage)

    def input_km(self):
        self.mileage = float(input("Entrez le kilométrage de la voiture : "))
        self.mileage_normalized = (self.mileage - np.min(self.x)) / (np.max(self.x) - np.min(self.x))

    def predict(self):
        estimate = self.estimate_price() 
        print(f"Le prix estimé de la voiture pour {self.mileage} km est : {estimate:.2f} euros.")

# Utilisation
PRED = Predict()
PRED.load_thetas()
PRED.input_km()
PRED.predict()
