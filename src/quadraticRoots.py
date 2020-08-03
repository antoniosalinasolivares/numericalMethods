import math

class Polinom:
    a= 0
    b= 0
    c= 0
    def __init__(self,roots):
        self.a = roots[0]
        self.b = roots[1]
        self.c = roots[2]
    
    def sqrt_b_squared_minus_4timesac(self):
        b_squared = (self.b)**2
        substractor = 4*(self.a)*(self.c)
        return math.sqrt(b_squared - substractor)
    
    def getRoots(self):
        return ((-1)*(self.b) + self.sqrt_b_squared_minus_4timesac())/(2*self.a) , ((-1)*(self.b) - self.sqrt_b_squared_minus_4timesac())/(2*self.a)

# How to use it
# we define a polinom with the order of x^2 + x^1 + x^0
pol = Polinom([1,5,1])
# we use getRoot to get the roots of the polinom in a list
a = pol.getRoots()
print(a)