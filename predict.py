import pandas as pd

class Predict:
    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0
        self.mileage = 0
        
    def load_thetas(self):
        df = pd.read_csv('theta.csv')
        thetas = df.iloc[0]
        self.theta0 = thetas.iloc[0]
        self.theta1 = thetas.iloc[1]

    def estimate_price(self):
        return (self.theta0 + (self.theta1 * self.mileage))

    def input_km(self):
        try :
            self.mileage = int(input("Entrez le kilomètrage de la voiture : "))
        except ValueError:
            print("Mettez un entier")
            exit()
        if self.mileage < 0: 
            print("Mettez un nombre de kilomètre positif")
            exit()
        if self.mileage > 375000:
            print("Mettez un nombre de kilomètrage inférieur à 500 000")
            exit()
 
    def predict(self):
        estimate = self.estimate_price() 
        print(f"Le prix estimé de la voiture pour {self.mileage} km est : {estimate:.2f} euros.")

PRED = Predict()
PRED.load_thetas()
PRED.input_km()
PRED.predict()
