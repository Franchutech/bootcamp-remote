# Paso 1: pedir dos números al usuario
a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))

# Paso 2: operador lógico AND
if a > 0 and b > 0:
    print("Ambos números son positivos")

# Paso 3: operador lógico OR
if a > 0 or b > 0:
    print("Al menos uno de los números es positivo")

# Paso 4: operador lógico NOT
if not (a > 0):
    print("El primer número NO es positivo")

# Paso 5: comparación múltiple
if 0 < a < 10:
    print("El primer número está entre 1 y 9")

# Paso 6: condicional en una sola línea
print("El primero es mayor") if a > b else print("El segundo es mayor o son iguales")
