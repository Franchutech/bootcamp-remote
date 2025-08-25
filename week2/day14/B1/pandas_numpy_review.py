import numpy as np
import pandas as pd

# Ejercicio 1: Crear un array del 5 al 15

arr = np.arange(5, 16)
print("Array del 5 al 15:")
print(arr)

# Ejercicio 2: Crea un array de números del 5 al 15 con NumPy e imprime: El array / La suma total de sus elementos usando np.sum().

arr = np.arange(5, 16)
print("Array del 5 al 15:")
print(arr)

print("Suma todos los elementos:")
print(np.sum(arr))

# Ejercicio 3: Crea un array de números del 1 al 20 y calcula: El máximo (np.max()). /El mínimo (np.min()).

arr = np.arange(1, 21)
print("Array del 1 al 20:")
print(arr)

print("Maximo:", np.max(arr))
print("Minimo:", np.min(arr))

# Ejercicio 4: Crea un array de números del 1 al 10 y calcula: La media (promedio) con np.mean()./La desviación estándar con np.std().

arr = np.arange(1,11)
print("El array es:", arr)

print("La media promedio es:", np.mean(arr))
print("La desviación estándar es:", np.std(arr))

# Ejercicio 5: Crea un array de números del 1 al 12 y:
# Reshape el array a una matriz de 3 filas x 4 columnas usando .reshape(3,4).
# Imprime la matriz resultante.

arr = np.arange(1, 13)
print("El array es:", arr)
matriz = arr.reshape(3, 4)

print("La matriz es:")
print(matriz)

# Ejercicio 6: Crea un array de números del 1 al 9 y conviértelo en una matriz 3x3.
# Imprime la matriz.
# Calcula y muestra la diagonal principal usando np.diag().

arr = np.arange(1,10)
matriz = arr.reshape(3, 3)
print("El array es:", arr)
print("La matriz es:")
print(matriz)

print("Diagonal Principal:", np.diag(matriz))

# Ejercicio 7: Crea un array de números del 1 al 10 y:
# Selecciona solo los números pares usando indexación booleana.
# Imprime el array original y el array de pares.

arr = np.arange(1, 11)
print("Array original:", arr)

pares = arr[arr %2 == 0]
print("Array de pares:", pares)

# Ejercicio 8: Crea un array de números del 1 al 12 y conviértelo en una matriz 3x4.
# Imprime la matriz.
# Imprime la suma por filas usando np.sum(matriz, axis=1).
# Imprime la suma por columnas usando np.sum(matriz, axis=0)

arr = np.arange(1,13)
matriz = arr.reshape(3, 4)
print("La matriz es:")
print(matriz)

print("La suma por filas es:", np.sum(matriz, axis=1))
print("La suma por columnas es:", np.sum(matriz, axis=0))

# Ejercicio 9: Crea un array de números del 1 al 16 y conviértelo en una matriz 4x4.
# Imprime la matriz.
# Calcula la transpuesta usando .T.
# Imprime la matriz transpuesta.

arr = np.arange(1, 17)
matriz = arr.reshape(4, 4)
print("La matriz es:")
print(matriz)

print("La transpuesta:")
print(matriz.T)

# Ejercicio 10: Crea un DataFrame de Pandas con la siguiente información:

# Nombre	Edad	Ciudad
# Ana	23	Madrid
# Luis	30	Barcelona
# Marta	27	Valencia

# Imprime el DataFrame completo.
# Imprime solo la columna Edad.
# Calcula la edad promedio con .mean().

data = {
    "Nombre": ["Ana", "Luis", "Marta"],
    "Edad": [23, 30, 27],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
}
df = pd.DataFrame(data)
print("El DataFrame completo es el siguiente:")
print(df)

print("La columna de Edad es la siguiente:")
print(df["Edad"])

print("La edad promedio es:")
print(df["Edad"].mean())