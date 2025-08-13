# Ejemplo de lista
frutas = ["manzana", "pera", "naranja"]

# Mostrar la lista completa
print("Lista completa:", frutas)

# Acceder a un elemento por índice (empieza en 0)
print("Primera fruta:", frutas[0])
print("Segunda fruta:", frutas[1])

# Modificar un elemento
frutas[1] = "plátano"
print("Lista después de cambiar la segunda fruta:", frutas)

# Agregar un elemento al final
frutas.append("uva")
print("Lista después de agregar 'uva':", frutas)

# Eliminar un elemento por valor
frutas.remove("naranja")
print("Lista después de eliminar 'naranja':", frutas)

#Ejercicio:

paises = ["Costa Rica", "Argentina", "España", "Canadá", "Suecia"]

# Mostrar lista completa:

print("Lista completa:", paises)

#Mostrar primer y último país:

print("Primer país:", paises[0])
print("Último país:", paises[-1])

# Cambiar el segundo país por otro distinto:

paises[1] = "Suiza"

# Insertar un nuevo país al inicio y otro al final:

paises.insert(0,"Países Bajos")
paises.insert(7,"Dinamarca")

# Eliminar pais por nombre y otro por posición:

paises.remove("Costa Rica")
del paises [-1]

# Lista final

print("Listado Final:", paises)

#Diccionarios python:

# Ejemplo de diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Mostrar el diccionario completo
print("Diccionario completo:", persona)

# Acceder a un valor por clave
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Modificar un valor existente
persona["edad"] = 26
print("Edad actualizada:", persona["edad"])

# Agregar un nuevo par clave:valor
persona["profesion"] = "Ingeniera"
print("Diccionario con nueva clave:", persona)

# Eliminar una clave
del persona["ciudad"]
print("Diccionario después de eliminar ciudad:", persona)

# Recorrer el diccionario
for clave, valor in persona.items():
    print(clave, "→", valor)


# Ejercicio de Diccionario:

#1 Haz un diccionario llamado "libros":

libros = {
    "libro1":{
         "titulo": "Harry Potter 1",
         "autor": "J.K.Rowling",
         "año": "1996"
     },
    "libro2":{
         "titulo": "Harry Potter 2",
         "autor": "J.K.Rowling",
         "año": "1998"
     },
     "libro3":{
         "titulo": "Harry Potter 3",
         "autor": "J.K.Rowling",
         "año": "1999"
     },
      "libro4":{
          "titulo": "El señor de los Anillos 1",
          "autor": "J.R.R.Tolkien",
          "año": "1954"
     }
}
# Muestra el diccionario completo:

print("Diccionario completo:",libros)

# Muestra el título de cada libro:

for clave in libros:
    print("Título:", libros[clave]["titulo"])

# Cambia el año del libro por otro valor:

libros["libro1"]["año"] = 1997
print("Nuevo año corregido:", libros["libro1"]["año"])


# Agrega una clave nueva "genero" con un valor de texto.

for clave in libros:
    libros[clave]["Género"] = "Fantasía"

# Elimina la clave "autor".

for clave in libros:
    del libros[clave]["autor"]

# Recorre el diccionario e imprime clave y valor en el formato: clave → valor

for clave, valor in libros.items():
    print(clave, "→", valor)

# FUNCIONES

# Ejemplo básico de función

# Definición de la función
def saludar(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

# Uso de la función
resultado = saludar("Franchu")
print(resultado)

# FUNCIÓN SIN PARAMETROS-SIN RETORNOS

def saludar():
    print("Hola, bienvenida al programa.")

saludar()

# FUNCIÓN CON PARAMETROS-SIN RETORNO

def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Franchu")

# FUNCIÓN CON PARAMETROS-CON RETORNO

def crear_saludo(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

resultado = crear_saludo("Franchu")
print(resultado)


# SIN retorno
def sin_retorno():
    print("Hola")

# CON retorno
def con_retorno():
    return "Hola"

# Ejecución
saludo1 = sin_retorno()   # imprime "Hola", pero saludo1 vale None
saludo2 = con_retorno()   # no imprime nada, pero saludo2 vale "Hola"

print("Valor de saludo1:", saludo1)
print("Valor de saludo2:", saludo2)

# Ejercicio de cierre B1

# Ejercicio de cierre B1

def calcular_promedio(nombre, numero1, numero2, numero3, numero4, numero5):
    promedio = (numero1 + numero2 + numero3 + numero4 + numero5) / 5
    mensaje = f"Hola {nombre}, el promedio es: {round(promedio, 2)}"
    return mensaje

usuario = input("Introduce un nombre: ")
# Ejemplo con 5 números fijos (puedes cambiarlos)
resultado = calcular_promedio(usuario, 7, 8, 9, 10, 6)
print(resultado)






  
