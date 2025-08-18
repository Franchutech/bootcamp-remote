# Ejercicio 1:
base = float(input("La base del triángulo es: "))
altura = float(input("La altura del triángulo es: "))

area = base*altura / 2
print("El área del triángulo rectangulo es: ", area)

# Ejercicio 2:
celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = (celsius * 9/5) + 32 
print("La conversión a Fahrenheit es:", fahrenheit)

# Ejercicio 3:

numero = int(input("Ingrese un número para evaluación: "))

if numero %2 == 0:
    print("Es par")
else:
    print("Es impar")

# Ejercicio 4:

while True:
    palabra = input("Ingresa una palabra (máx. 20 letras, sin espacios ni símbolos): ")

    if len(palabra) > 20 or not palabra.isalpha():
        print("❌ No incluir espacios, ni simbolos, ni números, solamente letras. Inténtalo de nuevo.\n")
        continue

    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"✅ La palabra ingresada es: {palabra}")
    print(f"🔤 Número de vocales: {contador}")
    break

# Ejercicio 5:

n = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

if n < 0:
    print("❌ El factorial no está definido para números negativos.")
elif n == 0:
    print("El factorial de 0 es: 1")
else:
    factorial = 1
    for numero in range(1, n+1):
        factorial *= numero
    print(f"El factorial de {n} es: {factorial}")

# Ejercicio 6:

texto = input("Introduzca texto (palabra o frase): ")
invertido = texto[::-1]
print("Texto invertido:",invertido)

# Ejercicio 7:

while True:
    palabra = input("Introduzca una palabra (sin espacios, ni simbolos): ")

    if not palabra.isalpha():
        print("❌La palabra no cumple los requisitos solicitados")
        continue

    invertida = palabra [::-1]

    if palabra == invertida:
        print("✅ La palabra es un palíndromo")
    else:
        print("❌La palabra no cumple con las características de un palíndromo")
    break

# Ejercicio 8:Fibonacci

n = int(input("Ingresar el número para la serie Fibonacci: "))

if n < 0:
    print("🚫El número de términos debe ser mayor o igual que 0")
elif n == 0:
    print("⚠️Fibonacci de cero es cero")
elif n == 1 :
    print("⚠️Serie Fibonacci [0]")
elif n == 2:
    print("Serie Fibonacci [0,1]")
else:
    fibonacci = [0,1]

    for i in range(2,n):
        siguiente = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append (siguiente)

    print("Serie fibonacci:", fibonacci)

# Ejercicio 9: Encontrar el número más grande en una lista

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
mayor = max(numeros)

print("La lista ingresada es:", numeros)
print("El número más grande es:", mayor)

# Ejercicio 10: Sumar todos los números de una lista

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
total = sum(numeros)

print("La lista ingresada es:", numeros)
print("La suma de los números es:", total)

# Ejercicio 11: Contar cuántas veces aparece un número en una lista

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

elemento = int(input("¿Qué número quieres contar en la lista? "))

apariciones = numeros.count(elemento)

print(f"El número {elemento} aparece {apariciones} veces")

# Ejercicio 12: Eliminar duplicados de una lista

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

sin_duplicados = list(set(numeros))

print("Lista sin duplicados:", sin_duplicados)

# Ejercicio 12 (otra forma): Eliminar duplicados manteniendo el orden

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

sin_duplicados = []
for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print("Lista sin duplicados (manteniendo orden):", sin_duplicados)

# Ejercicio 13: Ordenar una lista de menor a mayor sin usar sort()

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

# Algoritmo burbuja
for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            # Intercambiar valores
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)

# Ejercicio 14: convertir entrada en tabla de multiplicar 

def tabla_multiplicar(n):
    for i in range(1, 11):  # del 1 al 10
        print(f"{n} x {i} = {n * i}")

# pedir al usuario el número
numero = int(input("Ingresa un número: "))

# llamar a la función
tabla_multiplicar(numero)

#Ejercicio 15: definir si una entrada es un número primo o no.

# Pedir número al usuario
numero = int(input("Ingresa un número: "))

# Verificar si es primo
if numero <= 1:
    print(f"{numero} no es primo.")
else:
    es_primo = True  # asumimos que sí es primo
    for i in range(2, numero):  # probamos todos los divisores desde 2 hasta n-1
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")

#Ejercicio 16: Exponentes.

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente == 0:
    resultado = 1
else:
    resultado = 1
    for i in range(exponente):
        resultado *= base

print(f"{base} elevado a {exponente} es {resultado}")

# Ejercicio 17: MCD

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))


mcd = 1
for i in range(1, min(a, b) + 1): 
    if a % i == 0 and b % i == 0:
        mcd = i

print(f"El MCD de {a} y {b} es {mcd}")

#Ejercicio 18: diccionarios


palabra = input("Ingresa una palabra: ")

conteo = {}

for letra in palabra:
    if letra in conteo:
        conteo[letra] += 1  
    else:
        conteo[letra] = 1   

print(conteo)

#Ejercicio 19: Cajero

# Saldo inicial
saldo = 1000

while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: {saldo}")
    elif opcion == "2":
        deposito = float(input("Ingresa el monto a depositar: "))
        saldo += deposito
        print(f"Has depositado {deposito}. Nuevo saldo: {saldo}")
    elif opcion == "3":
        retiro = float(input("Ingresa el monto a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Has retirado {retiro}. Nuevo saldo: {saldo}")
        else:
            print("Fondos insuficientes.")
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")

# Ejercicio #20: promedio de notas

entrada = input("Ingresa las calificaciones separadas por comas: ")

calificaciones = [float(x) for x in entrada.split(",")]


promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio es: {promedio}")

#Ejercicio #21 :  dado

import random

numero = random.randint(1, 6)

print(f"Ha salido el número {numero}")

#Ejercicio #22: contador de palabras en una frase

frase = input("Ingresa una frase: ")


palabras = frase.split()
cantidad = len(palabras)

print(f"La frase tiene {cantidad} palabras")

#Ejercicio #23
# Lista de tuplas
lista_tuplas = [("a", 1), ("b", 2), ("c", 3)]

# Convertir a diccionario
diccionario = {}
for clave, valor in lista_tuplas:
    diccionario[clave] = valor

print(diccionario)

#Ejercicio #24
# Pedir número decimal
numero = int(input("Ingresa un número decimal: "))

binario = ""  # cadena vacía para construir el binario

if numero == 0:
    binario = "0"
else:
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario  # añadir al inicio
        numero = numero // 2  # división entera

print(f"El número en binario es: {binario}")

# Ejercicio #25

# Pedir datos al usuario
P = float(input("Ingresa el capital inicial: "))
r = float(input("Ingresa la tasa de interés anual (%): "))
t = int(input("Ingresa el tiempo en años: "))

# Calcular interés compuesto
A = P * (1 + r/100) ** t

print(f"El monto final después de {t} años es: {A}")

# Ejercicio 26: Imprimir los primeros 100 números naturales

for i in range(1, 101): 
    print(i)

#Ejercicio 27: Mínimo de una lista

def minimo(lista):
   
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

# Pedir lista al usuario
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

# Usar la función
print(f"El número mínimo es: {minimo(numeros)}")

# Ejercicio 28:

# Pedir nombre del archivo
archivo = input("Ingresa el nombre del archivo .txt: ")

# Abrir y leer el archivo
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

# Contar palabras
palabras = contenido.split()
cantidad = len(palabras)

print(f"El archivo contiene {cantidad} palabras.")

# Ejercicio #29:

# Pedir nombre del archivo
archivo = input("Ingresa el nombre del archivo .txt: ")

# Abrir y leer el archivo
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()

# Separar en palabras y eliminar duplicados
palabras = contenido.split()
palabras_unicas = sorted(set(palabras))  # set elimina duplicados, sorted ordena

print(palabras_unicas)

# Ejercicio #30:
import random

# Generar número aleatorio
secreto = random.randint(1, 100)

print("He pensado un número entre 1 y 100. ¡Adivínalo!")

while True:
    intento = int(input("Ingresa tu número: "))

    if intento == secreto:
        print("🎉 ¡Felicidades! Adivinaste el número.")
        break
    elif intento > secreto:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print("Demasiado bajo, intenta de nuevo.")

#Final de la practica (total 30 ejercicios)
