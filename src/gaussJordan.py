class Matrix:
    matrix = [[]]
    ecuaciones = 0
    def __init__(self, matrix):
        if Matrix.validate(matrix):
            self.matrix = matrix
            self.ecuaciones = len(self.matrix)
        else:
            return None

    #Busca un pivote en la posición adecuada, asume que todos los 
    #renglones previos al indice solicitado ya no son elegibles como 
    #pivotes, en caso de no encontrar pivotes disponibles, imprime 
    #un mensaje de error y retorna None
    def searchPivot(self,index):
        index_count = 0
        for item in self.matrix[index:]:
            if item[index] != 0:
                return index+index_count
            else:
                index_count += 1
        print("No se encontró un pivote en la posición correcta")
        return None
    
    
    #Intercambia dos renglones, dados sus índices
    def swap(self,index_a, index_b):
        if index_a == index_b:
            return True
        if (index_a <= self.ecuaciones and index_b <= self.ecuaciones):
            temp_holder = self.matrix[index_a]
            self.matrix[index_a] = self.matrix[index_b]
            self.matrix[index_b] = temp_holder
            return True
        else:
            print("error de indices")

    
    #Dados el indice de un renglon (preferiblemente un pivote), y el indice del 
    #pivote calcula el coeficiente por el que se debe multiplicar para eliminar
    #los coeficientes en ese indice
    #asume que la ecuacion dada por el indice tiene un pivote = 1
    def eliminate(self, ecuation_index, pivot_index):
        pivotEquation = self.matrix[ecuation_index][:]
        for iterator in range(self.ecuaciones):
            substitute = self.matrix[iterator][:]
            multiplier = substitute[pivot_index]
            substitute = [substitute[x]-multiplier*pivotEquation[x] for x in range(len(substitute))]
            self.matrix[iterator] = substitute
        self.matrix[ecuation_index] = pivotEquation
        
    
    #utiliza todos los metidos para iterar en la matriz y obtener la matriz identidad
    #facilitando los resultados
    def solve(self, print_option=True):
        for iterator in range(self.ecuaciones):
            pivot_index = self.searchPivot(iterator)
            if(pivot_index == None):
                print("Sistema incompatibe, coeficientes eliminados")
                break
            else:
                self.swap(pivot_index, iterator)
                self.unity(iterator, iterator)
                self.eliminate(iterator, iterator)
                print("\n")
                self.print()
        if(print_option):
            self.print()
    
    #Dados el indice de la ecuacion y el indice del pivote, se divide toda la ecuacion 
    #para que el pivote quede en un valor de 1 
    def unity(self, ecuation_index, index):
        divider = self.matrix[ecuation_index][index]
        self.matrix[ecuation_index] = [x / divider for x in self.matrix[ecuation_index]]
    
    #Metido definido para verificar que las dimensiones 
    #introducidas a la matriz sean útiles para la operacion de Gauss 
    @staticmethod
    def validate(matrix):
        #Determina la cantidad de ecuaciones
        n = len(matrix)
        #Valida que cada ecuacion tenga la longitud necesaria m=n+1
        for item in matrix:
            if len(item) != (n+1):
                print("Error de dimensiones")
                return False
            else:
                pass
        return True
    def print(self):
        for item in self.matrix:
            print (item)

# How to use it
#We define an object of the class matrix, which receives a amtrix of size mxm+1
big = Matrix([[6,0,0,0,2],[2,-10,-2,0,-1],[-2,7,-4,0,-2],[3,10,2,0,35]])
#We can print the matrix as follows
big.print()
#Solve will print the remaining matrix with with the coeficients of each equation set to one
big.solve()
#The system will algo inform if the solution to the syustem is valid or not