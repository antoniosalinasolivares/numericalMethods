import math
import numpy as np
import matplotlib.pyplot as plt

class Bisection:
    f = None
    xl = 0
    xu = 0
    mini = 0
    maxi = 0
    table = [["i","xl","xu","xi","f(xl)","f(xu)","f(xi)"]]

    def __init__(self, f, mini=0, maxi= 0):
        self.f = f
        self.maxi = maxi
        self.mini = mini

    def display(self):
        xvalues = np.arange(self.mini,self.maxi,.1)
        plt.plot(xvalues ,[self.f(x) for x in xvalues])
        plt.plot([self.mini,self.maxi],[0,0],"b")
        plt.plot([0,0],[self.f(self.mini),self.f(self.maxi)],"b")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()

    def getXi(self, xl, xu):
        return (xl + xu) / 2
    
    def isInside(self,error,xi):
        return abs(self.f(xi)) < error
    
    def findRoot(self, xl,xu, error):
        self.table = [["i","xl","xu","xi","f(xl)","f(xu)","f(xi)"]]
        xi = self.getXi(xl,xu)
        it = 0
        
        while not self.isInside(error,xi):
            self.table.append([it,xl,xu,xi,self.f(xl),self.f(xu),self.f(xi)])
            xu = {True:xi, False:xu}[self.f(xi)*self.f(xu)>0]
            xl = {True:xi, False:xl}[self.f(xi)*self.f(xl)>0]
            xi = self.getXi(xl,xu)
            it += 1
        self.table.append([it,xl,xu,xi,self.f(xl),self.f(xu),self.f(xi)])
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.table]))
        return (xi)


# How to use it
# We need to define a function, the one that we need to solve
fun = lambda x : math.sqrt(x) - (2*math.cos(math.radians(x+1)))
#we create an object that receives the function and the range that it needs to be graphed
root_fun = Bisection(fun, 0,50)
#the display method allows us to see the function graphically 
root_fun.display()
#seeing this graph, we can find points in the function where the f(x) changes it's sign
#the closer we get to these points the faster we will find a solution
#Solve uses tree arguments, the lower limit, the higher limit and a degree of error that we will allow
print("The value x | f(x) -> 0 is: " + str(root_fun.findRoot(0,10,.0001)))