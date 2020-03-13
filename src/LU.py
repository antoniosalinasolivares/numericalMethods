import numpy as np

class LU:
    matrix = [[]]
    L = [[]]
    U = [[]]
    B = []
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.B = vector
        self.L = [[{True:1, False:0}[x==y] for y in range(len(self.matrix))] for x in range(len(self.matrix))]
    def solve(self):
        if not len(self.matrix) == len(self.matrix[0]):
            return
        for index in range(len(self.matrix)-1):
            pivote = self.matrix[index][index] 
            for row in range(index+1, len(self.matrix)):
                magic_number = self.matrix[row][index]/pivote
                self.L[row][index] = magic_number
                self.matrix[row] = [self.matrix[row][x] - magic_number * self.matrix[index][x] for x in range(len(self.matrix))] 

    def printL(self):
        print("L:")
        for row in self.L:
            print(row)
    
    def printMatrix(self):
        print("matrix:")
        for row in self.matrix:
            print(row)




test = LU([[9,1,1],[15,1,1],[1,1,1]],[1,1,1])
test.solve()
test.printL()
test.printMatrix()

test2 = LU([[1,4,-2],[3,-2,5],[2,3,1]] , [3,14,11])
test2.solve()
test2.printL()
test2.printMatrix()