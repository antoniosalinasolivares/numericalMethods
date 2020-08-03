import matplotlib.pyplot as plt
import numpy as np
import math

#La funcion recibe como parametros una funcion que retorna una ecuacion del sistema A
# y su valor en b, los limites de x y y y el numero de ecuaciones (segmentos) que queremos
def finite_differences(math_function, x_min, x_max, y_min, y_max, equations):
  #definimos variables a utilizar
  delta_x = (x_max - x_min)/(equations-1)
  A = []
  b = []
  x_list = []

  #Agregamos las condiciones iniciales (la ecuacion y_0 y x_0)
  ec0 = [0 for x in range(equations)]
  ec0[0] = 1
  A.append(ec0)
  b.append(y_min)
  x_list.append(x_min)

  #Iteramos en i para obtener el resto de las ecuaciones y valores
  for i in range(1, equations-1):
    x = x_min + i*delta_x
    x_list.append(x)
    eci, bi = math_function(i, x, delta_x, equations)
    A.append(eci)
    b.append(bi)
  
  #Agregamos condiciones finales
  ecn = [0 for x in range(equations)]
  ecn[-1] = 1
  A.append(ecn)
  b.append(y_max)
  x_list.append(x_max)

  #definimos resultados y los regresamos 
  # x_list es la tabla de valores de x que utiliza
  #(facilita despues la grafica de la funcion)
  
  A = np.array(A)
  b = np.array(b)
  solution = np.linalg.solve(A,b)
  return solution, A, b, x_list

#Esta funcion es el despeje de la sustitucion en nuestro sistema
#define un vector de 0's y le asigna el valor indicado por la ecuacion
#Tambien retorna el calculo de b
def math_function(i, x, delta_x, size):
  res = np.zeros(size)
  res[i-1] = ((x**2)/delta_x) - 2
  res[i] = -2*((x**2)/delta_x)
  res[i+1] = ((x**2)/delta_x) + 2
  return res, delta_x/x

solution, A, b, x_list= finite_differences(math_function, 1, 2, 2, 5, 20 )
def analytical_solution(x):
  return 8.693 - (5.693/x) + (1/x)*(math.log(1/x)-1)

print(solution)
print(A)
print(b)
plt.plot(x_list, solution, 'r')
plt.plot(x_list, [analytical_solution(x) for x in x_list], 'g')