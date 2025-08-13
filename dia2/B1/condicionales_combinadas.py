# Paso 1: pedir un número
numero = int(input("Escribe un número: "))

# Paso 2: condicional combinada con AND
if numero > 0 and numero < 100:
    print("El número es positivo y menor que 100")
elif numero >= 100:
    print("El número es positivo y grande (100 o más)")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Paso 3: ejemplo con OR
if numero == 0 or numero == 1:
    print("El número es especial (0 o 1)")

# Paso 4: condicional anidada
if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo y impar")
