import csv
import numpy as np

class Predict:
    def __init__(self):
        self.theta0 = 0.9019142003565301
        self.theta1 = -0.90484545098481
        self.mileage = 0
        self.x = []
        self.y = 
        
    def load_thetas(self):
        value = []
        with open("data.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                value.append(row)
        self.theta0 = float(value[0][0])
        self.theta1 = float(value[0][1]) 

    def estimate_price(self):
        calc = self.theta0 + (self.theta1 * self.mileage)
        calc = calc * (np.max(self.y) - np.min(self.y)) + np.min(self.y)
        return self.theta0 + (self.theta1 * self.mileage)

    def input_km(self):
        self.mileage = float(input("Entrez le kilométrage de la voiture : "))

    def predict(self):
        estimate = self.estimate_price() 
        print(f"Le prix estimé de la voiture pour {self.mileage} km est : {estimate:.2f} euros.")

# Utilisation
PRED = Predict()
PRED.input_km()
# PRED.load_thetas()
PRED.predict()
