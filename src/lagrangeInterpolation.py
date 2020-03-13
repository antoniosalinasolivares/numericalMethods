import numpy as np

class Lagrange:
    matrix = None
    x = None
    fx = None

    def __init__(self, x, fx):
        self.x = x
        self.fx = fx
        self.buildMatrix()

    def buildMatrix(self):
        size = len(self.x)
        self.matrix = np.array([[item ** power for power in range(size)] for item in self.x])
        for row in self.matrix:
            print (row)

    def createFunction(self):
        a_inverse = np.linalg.inv(self.matrix)
        print("a_inverse:")
        for row in a_inverse:
            print(row)
        coeficients = a_inverse @ self.fx
        print(coeficients)
        return lambda x : sum([coeficients[index] * x**index for index in range(len(coeficients))])

# How to use it
#We creatre a Lagrange object with the values of x and f(x) as lists
test = Lagrange([6,6.5,7],[-8,9.9875,34])

#we create a function with it
a = test.createFunction()
#And we evaluate the function with the data that we wants to aproach
print(a(0))
