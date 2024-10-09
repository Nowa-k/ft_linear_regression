import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    
    def __init__(self):
        self.x = []
        self.y = []
        self.x_normalize = []
        self.y_normalize = []
        
    def read_csv(self):
        df = pd.read_csv('data.csv')
        self.x = df.iloc[:, 0].values
        self.y = df.iloc[:, 1].values
    
    def normalize(self):
        x = np.array(self.x)
        self.x_normalize = (x - np.min(x)) / (np.max(x) - np.min(x))
        y = np.array(self.y)
        self.y_normalize = (y - np.min(y)) / (np.max(y) - np.min(y))
        
    def calc_cost(self, theta_0, theta_1):
        global_cost = 0
        m = len(self.x)
        for i in range(m):
            cost_i = ((theta_0 + (theta_1 * self.x_normalize[i])) - self.y_normalize[i]) * ((theta_0 + (theta_1 * self.x_normalize[i])) - self.y_normalize[i]) 
            global_cost += cost_i
        return (1 / (2 * m)) * global_cost
        
    def partial_derivative(self, tmp_theta0, tmp_theta1):
        derivate0 = 0.0
        derivate1 = 0.0
        m = len(self.x)
        for i in range(m):
            error = (tmp_theta0 + (tmp_theta1 * self.x_normalize[i])) - self.y_normalize[i]
            derivate0 += error
            derivate1 += error * self.x_normalize[i]
        
        derivate0 /= m
        derivate1 /= m
        return [derivate0, derivate1]
    
    def maj_theta(self, tmp_theta0, tmp_theta1, learning_rate=0.1):
        derivate0, derivate1 = self.partial_derivative(tmp_theta0, tmp_theta1)
        theta_0 = tmp_theta0 - (learning_rate * derivate0)
        theta_1 = tmp_theta1 - (learning_rate * derivate1)
        return [theta_0, theta_1]
    
    def gradient_descent(self, iterations=500, learning_rate=0.1):
        tmp_theta0 = 0.0
        tmp_theta1 = 0.0
        
        plt.ion()

        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y, color="blue", label="Données")
        line, = ax.plot([], [], color="red", label="Ligne de régression")
        plt.title("Régression linéaire : Km vs Prix")
        plt.xlabel("Kilométrage")
        plt.ylabel("Prix")
        plt.legend()

        
        for i in range(iterations):
            tmp_theta0, tmp_theta1 = self.maj_theta(tmp_theta0, tmp_theta1, learning_rate)
            
            regression_line = tmp_theta0 + tmp_theta1 * self.x_normalize
            
            line.set_data(self.x, regression_line * (np.max(self.y) - np.min(self.y)) + np.min(self.y))
            
            plt.draw()
            plt.pause(0.1)
            
            cost = self.calc_cost(tmp_theta0, tmp_theta1)
            print(f"Iteration {i+1} | Cost: {cost} | Theta0: {tmp_theta0} | Theta1: {tmp_theta1}")
        
        print(f"Final Theta0: {tmp_theta0}, Final Theta1: {tmp_theta1}")
        plt.ioff()
        plt.show()

    def makeScatter(self):
        plt.scatter(self.x, self.y, color="blue")
        plt.title("Relation entre Km et le prix d'un véhicule")
        plt.xlabel("Km")
        plt.ylabel("Prix")
        plt.show()

LINEAR = LinearRegression()
LINEAR.read_csv()
LINEAR.normalize()
LINEAR.gradient_descent()
