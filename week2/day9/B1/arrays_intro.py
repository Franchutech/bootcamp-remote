import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.shape)

# Forma de un array (2 filas, 3 columnas)
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b)
print(b.shape)

# Operaciones básicas con Numpy:
c = np.array([10, 20, 30])
print(c + 10)  #cada elemento se suman 10
print(c * 2)   #cada elemento se multiplica x 2.
print(c - 5)   #cada elemento se resta 5.
print(c / 10) #cada elemento se divide entre 10.

# Broadcasting en Numpy
print(b + 100) # broadcasting con 1 escalar
print(b + c)   #broadcasting con 2 matrices