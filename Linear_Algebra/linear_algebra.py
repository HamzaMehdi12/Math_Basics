import os
import sys
import time


class Linear_Algebra():
    def __init__(self):
        "Class constructor, initializes the self part only"
        try:
            self.A = []
            self.B = []
            for i in range(5):
                self.A.append([])
                self.B.append([])
                for j in range(5):
                    self.A[i].append(2 * (i+ j))
                    self.B[i].append(3 * (i + j))

            print(f"\nMatrix A: {self.A}, {len(self.A)} rows, {len(self.A[0])} columns \nand B: {self.B}, {len(self.B)} rows and {len(self.B[0])} columns")
        except Exception as e:
            print(f"Error while working on matrix formation {str(e)}")
            raise Exception(e)
        try:
            print("Calling Multiplying function!")
            time.sleep(3)
            self.C = self.mat_mul(self.A, self.B, len(self.A), len(self.A[0]))
            print(f"The results are as follows: \n{self.C}")
        except Exception as e:
            print(f"Error while calling multiplication functions: {str(e)}")
        try:
            print("Calling the inverse function!")
            time.sleep(3)
            self.D = []
            for i in range(2):
                self.D.append([])
                for j in range(2):
                    if i == 0 and j == 0: 
                        self.D[i].append(4*(1+j))
                    else:
                        self.D[i].append(4 * (i+j))
            print(f"Matrix for inverse: \n{self.D} with rows: {len(self.D)} and cols: {len(self.D[0])}")
            self.D1 = self.mat_inv(self.D, len(self.D), len(self.D[0]))
            print(f"Completed inverse: {self.D1}")        
        except Exception as e:
            print(f"Error while calling Matrix inverse function: {str(e)}")
        try:
            print(f"Calculating eigenvalues and eigenvectors for \n{self.D}")
            time.sleep(3)
            self.a, self.b, self.D2 = self.mat_eigen(self.D, len(self.D), len(self.D[0]))
            print(f"Completed reducing and eigen values \na: {self.a}, b: {self.b}, reduced_form: {self.D2}")
        except Exception as e:
            print(f"Error while sending values to eigen func: {str(e)}")
            raise Exception(e)
        try:
            print(f"Now going for Single Value Decomposition (SVD) for \n{self.D}")
            time.sleep(3)
            self.svd(self.D, len(self.D), len(self.D[0]))
        except Exception as e:
            print(f"Error while sending to svd func: {str(e)}")
            raise Exception(e)
        
    def mat_mul(self, A, B, x, y):
        "Mulitplies 2 Matrices without a library. Replicating dot product"
        self.A = A
        self.B = B
        self.x = x
        self.y = y
        self.C = []
        self.sum = 0
        for i in range(self.x):
            self.C.append([])
            self.sum = 0
            for j in range(self.y):
                self.sum += self.A[i][j] * self.B[j][i]
            self.C[i].append(self.sum)
        #print(f"Calculated the dot product / multiplications")
        return self.C
    def mat_inv(self, A, x, y):
        "Inverse of a matrix, using without numpy"
        try:
            self.A = A
            self.x = x
            self.y = y
            self.B = []
            """
            for i in range(2):
                self.B.append([])
                for j in range(2):
                    if i == j:
                        self.B[i].append(1)
                    else:
                        self.B[i].append(0)
            self.A.append(self.B)
            print(f"Matrix appended! New values are: {self.A}")

            #Now performing inverse
            for i in range(self.x):
                for j in range(self.y):
                    self.A = 1
                    #Leaving as inverse needs time. Will visit next time
            """
            return self.A
        except Exception as e:
            print(f"Error while inverse: {str(e)}")
            raise Exception(e)

    def mat_eigen(self, A, x, y):
        "Calculates eigenvalues and eigenvectors"
        try:
            self.A = A
            self.x = x
            self.y = y
            self.det = 1

            #calculating the determinent
            for i in range(self.x):
                for j in range(2):
                    if i !=j:
                        self.det = self.A[i][j] * self.A[j][i]
            #print(f"Value of constand : {self.det}")
            self.a = 0
            self.b = 0

            for i in range(self.x):
                for j in range(self.y):
                    if i == 0 and j == 0:
                        self.a = -1 * (self.det - self.A[i][j])
                        self.A[i][j] = self.A[i][j] + self.a
                    if i == 1 and j == 1:
                        self.b = -1 * (self.det - self.A[i][j])
                        self.A[i][j] = self.A[i][j] + self.b
                    else:
                        continue
            #print(f"Eigen values are a: {self.a} and b: {self.b}")
            #print(f"The matrix is as follows: {self.A}")
            #Calculating the eigenvectors
            self.temp1 = 0
            self.temp2 = 0
            for i in range(self.x):
                for j in range(self.y):
                    #calculating the null space
                    #reducing the matrix to only 1 row
                    if i == 0:
                        if j == 0:
                            self.temp1 = self.A[i][j]
                            #print(f"Temp1: {self.temp1}")
                            if self.temp1 == 0:
             #                   print("No vector for this problem")
                                break
                        self.A[i][j] = self.A[i][j]/self.temp1
              #          print(f"Value for first quad: {self.A[i][j]}")
                    if i == 1:
                        if j == 1:
                            self.A[i][j] = abs(self.A[i-1][j]) - abs(((self.A[i][j]) * self.A[i-1][j]))
                            self.temp2 = self.A[i][j]
               #             print(f"Temp2: {self.temp2}")
                            self.A[i][j] = self.A[i][j] / self.temp2
                            self.A[i-1][j] = abs(self.A[i-1][j]) - abs((self.A[i][j]) * self.A[i-1][j])
                #            print(f"Value for last quad: {self.A[i][j]}")
                        if j == 0:
                            self.A[i][j] = abs(self.A[i][j]) - abs(((self.A[i-1][j]) * self.A[i][j]))
                 #           print(f"Value for last quad: {self.A[i][j]}")
            #print(f"Eigenvector reduced from: \n{self.A}")
            return self.a, self.b, self.A        
        except Exception as e:
            print(f"Error in calculating eigenvalues and eigenvectors: {str(e)}")
            raise Exception(e)
    def svd(self, A, x, y):
        "Deriving and calculating Single Value Decompositon "
        self.A = A


if __name__ == "__main__":
    var = Linear_Algebra()



