import time
import math
import matplotlib.pyplot as plt
import msvcrt

from tqdm import tqdm
#from decimal import Decimal

#We have an issue in the Geometric Mean that in the case of high number of rows and cols (20+),the float value does not pick the results. This means that our mean condition is not working well. So please check. If the error is resolved, please continue and remove this error.

class Stats:
    def __init__(self, A):
        "Initializing the class Stats"
        self.A = A
        #Lets calculate the mean
        print(f"Array A passed with values: {self.A[::5]}, rows: {len(self.A)} and cols: {len(self.A[0])}")
        print("Calculating mean for ungrouped data")
        self.A_mean = self.mean_ungrouped(self.A, len(self.A), len(self.A[0]))
        # Now going for variance
        print("Calculating Variance")
        self.A_var = self.var(self.A, self.A_mean, len(self.A), len(self.A[0]))
        print("Now printing the distribution of the model over the dataset, mean and variance")
        self.A_pdf_norm = self.pdf_normal(self.A, len(self.A), len(self.A[0]), self.A_mean, self.A_var)
        print("Now, going for the commulative distribution function normal graph for the probabilities attained from pdf")
        self.A_cdf_norm = self.cdf_normal(self.A_pdf_norm, len(self.A_pdf_norm))
        print("Finally, we move towards sample distribution")


    def mean_ungrouped(self, A, r, c): 
        "Calculating the mean without any library for a list or an Array. Here we will implement Arithmetic, Geometric and Harmonic Mean"
        self.A = A
        self.r = r
        self.c = c
        self.sum = 0
        self.prod = 1

        self.inp = 0

        while(True):
            self.inp = int(input(f"Which mean would you like to proceed with?\nArithmetic Mean: 1, \nGeometric Mean: 2, \nHarmonic mean: 3, \nWeighted Mean: 4...\n"))

            if self.inp == 1:
                
                print("Going with Arithmetic Mean")
                for i in tqdm(range(self.r)):
                    time.sleep(0.25)
                    for j in range(self.c):
                        self.sum += self.A[i][j]
                mean = self.sum / (self.r * self.c)
                
                print(f"Mean calculated is: {mean: .2f}")
            
            elif self.inp == 2:

                print("Going with Geometric Mean")
                for i in tqdm(range(self.r)):
                    time.sleep(0.25)
                    for j in range(self.c):
                        if A[i][j] == 0:
                            A[i][j] = 1
                        self.prod *= self.A[i][j]
                mean = math.exp(math.log(self.prod) / (self.r * self.c))
                
                print(f"Mean calculated is: {mean:.2f}")
            
            elif self.inp == 3:

                print("Going with Harmonic Mean")
                for i in tqdm(range(self.r)):
                    time.sleep(0.25)
                    for j in range(self.c):
                        self.sum += 1 / self.A[i][j]
                mean = (self.r * self.c) / self.sum
                
                print(f"Mean calculated is: {mean:.2f}")
            
            elif self.inp == 4:

                print("Going with Weighted Mean")
                for i in tqdm(range(self.r)):
                    time.sleep(0.25)
                    for j in range(self.c):
                        self.weight = A[self.r-1][self.c-1]
                        self.sum += self.weight * self.A[i][j]
                mean = self.sum / (self.r * self.c)
                
                print(f"Mean calculated is: {mean: .2f}")
            
            elif self.inp == 5:
                print("Wrong value entered, enter again!")
                time.sleep(1)
                return mean
            

            if msvcrt.kbhit():
                if msvcrt.getwche == '\r':
                    break
    
    def var(self, A, mean, r, c):
        "Calculating variance of the list based on the mean"
        self.A = A
        self.mean = mean
        self.r = r
        self.c = c
        self.sum = 0
        #Using sample variance
        for i in tqdm(range(self.r)):
            time.sleep(0.25)
            for j in range(self.c):
                self.sum += pow((A[i][j]) - self.mean, 2)
        var = self.sum / ((self.r * self.c))

        print(f"Variance is as follows: {var:.2f}")
        return var
    def pdf_normal(self, A, x, y, mean, dev): #Sample Distribution covered in this
        "Calculating the Probability Density function (Continuous) for our model (Although discrete works well)"
        self.A = A
        self.mean = mean
        self.dev = dev
        self.x = x
        self.y = y

        results = []

        for i in tqdm(range(self.x)):
            time.sleep(0.25)
            for j in range(self.y):
                prob = 1 / (math.sqrt(2 * math.pi * pow(self.dev, 2))) * math.exp(-((pow(self.A[i][j] - self.mean, 2)) / (2 * pow(self.dev, 2)))) #using the formula for normal distribution
                results.append(prob)

        x_vals = [i * 0.2 - 3 for i in range(len(results))]

        plt.plot(x_vals, results)
        plt.xlabel("Step size")
        plt.ylabel("PDF Vals")
        plt.title("PDF Normal Graph")
        plt.show()
        print(f"Resulls to 20 elements from the array{results[::5]}")
        return results
    

    def cdf_normal(self, results, x):
        "Now going for the commulative distribtuion function"
        "The last result would be added to the list"
        self.results = results
        self.x = x
        self.probs = []
        self.sum = 0
        #We will calculate and plot the probabilities we have received.

        for i in tqdm(range(self.x)):
            self.sum += self.results[i]
            self.probs.append(self.sum)

        x_vals = [i * 0.2 - 3 for i in range(len(self.probs))]
        plt.plot(x_vals, self.probs)
        plt.xlabel("Step size")
        plt.ylabel("CDF Vals")
        plt.title("CDF Normal Graph")
        plt.show()

        print(f"Resulls to 20 elements from the array{self.probs[::5]}")
        return self.probs

        

if __name__ == "__main__":
    A = []
    print("Enter rows (Should be between 5 to 30)")
    rows = int(input())
    print("Enter rows (Same as rows)")
    cols = int(input())

    #print(f"We have rows: {rows, type(rows)} and cols: {cols, type(cols)}")

    for i in tqdm(range(rows)):
        A.append([])
        time.sleep(0.25)
        for j in range(cols):
            if j%2 == 0:
                A[i].append(2 * (i+j))
            else:
                A[i].append(i+j)
    #passing the array for further operations
    stats = Stats(A)