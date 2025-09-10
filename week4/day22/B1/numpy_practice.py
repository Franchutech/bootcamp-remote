import numpy as np

print("=== REPASO EXPRESS DE NUMPY===")

# 1.Create basic array
a = np.array([1, 2, 3, 4, 5])
print("\nArray a:", a)
print("tipo de dato de los elementos:", a.dtype)
print("Dimensiones (shape):", a.shape)

# 2. Crear un array 2D (matriz)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray b (2D): \n", b)
print("Dimensiones (shape):", b.shape)

# 3. Operaciones básicas
print("\nOperaciones básicas con array a:")
print("a + 5:", a + 5)
print("a * 2:", a * 2)
print(" a ** 2:", a ** 2)

# 4. Estadísticas rápidas
print("\nEstadísticas con array a:")
print("Suma:", a.sum())
print("Promedio:", a.mean())
print("Máximo:", a.max())
print("Mínimo:", a.min())

print("\n=== OPERACIONES VECTORIZADAS ===")

# Array de ejemplo
x = np.array([10, 20, 30, 40, 50])
y = np.array([2, 4, 6, 8, 10])

print("\nArray x:", x)
print("Array y:", y)

# Operaciones entre array y escalar
print("\nArray x + 5:", x + 5)
print("Array x * 2:", x * 2)

# Operaciones entre arrays
print("\nSuma (x + y):", x + y)
print("Resta (x - y):", x - y)
print("Multiplicación (x * y):", x * y)
print("División (x / y):", x / y)

# Operaciones combinadas
print("\n(x + y) * 2:", (x + y) * 2)

print("\n=== ARRAYS MULTIDIMENSIONALES ===")

# 2D: matriz de 3 filas x 3 columnas
matriz_2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("\nMatriz 2D (3x3):\n", matriz_2d)
print("Shape:", matriz_2d.shape)

# 3D: cubo de 2 matrices (2 x 3 x 3)
matriz_3d = np.array([ [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]],
                       
                       [[10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18]] ])
print("\nMatriz 3D (2x3x3):\n", matriz_3d)
print("Shape:", matriz_3d.shape)
