# Paso 1: pedir un número al usuario
numero = int(input("Escribe un número: "))

# Paso 2: usar if, elif, else para decidir
if numero >0 :  # condición 1
    print("El número es positivo")
elif numero <0 :  # condición 2
    print("El número es negativo")
else:
    print("El número es cero")
