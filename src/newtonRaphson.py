
import math
import numpy as np
import matplotlib.pyplot as plt

class NewtonRaphson:
    function = None
    derivative = None
    initial_point = None
    def __init__(self, function, derivative, initial_point):
        self.function = function
        self.derivative = derivative
        self.initial_point = initial_point
    

    
    def isInside(self,error):
        return abs(self.function(self.initial_point)) < error

    def solve(self, error, steps=False):
        for i in range(100):
            if steps:
                print("f(%f) = %f" % (self.initial_point, self.function(self.initial_point)))
            self.initial_point = self.initial_point - (self.function(self.initial_point)/self.derivative(self.initial_point))
            if self.isInside(error):
                print("Bingo!  f(%f) = %f" % (self.initial_point, self.function(self.initial_point)))
                return self.initial_point
        print('demasiadas iteraciones, busca un valor inicial mas conveniente')



# How to use it
#first we define an object of the class NewtonRhapson with receives the main function, its derivative and an initial point 
nr = NewtonRaphson(lambda x: x**4 + x -3, lambda x: 4*(x**3) +1, 3)
#in this case we use lambdas to make it a one liner, but the function could be defined normally if it's preferred

#we can solve the equation by giving it a relative an absolute error (comparing it to the real result)
nr.solve(0.050)

#if we wanted to see each iteration of this process, we jus need to add a True to the arguments of the solve method
# nr.solve(0.050, True)