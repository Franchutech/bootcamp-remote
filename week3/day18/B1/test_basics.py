# test_basics.py
# Primeras pruebas con PyTest (funciones puras y sencillas)

# 📌 Prueba 1: comprobar suma
def test_suma():
    a = 2
    b = 3
    resultado = a + b
    # Verificamos que 2 + 3 = 5
    assert resultado == 5

# 📌 Prueba 2: comprobar longitud de string
def test_longitud_string():
    palabra = "bootcamp"
    # Verificamos que la palabra tiene 8 letras
    assert len(palabra) == 8

# 📌 Prueba 3: verificar si un número es par
def test_es_par():
    numero = 10
    assert numero % 2 == 0

# 📌 Prueba 4: comprobar que una lista contiene un elemento
def test_lista_contiene_elemento():
    frutas = ["manzana", "pera", "uva"]
    assert "pera" in frutas

# 📌 Prueba 5: comprobar mayúsculas
def test_mayusculas():
    palabra = "bootcamp"
    assert palabra.upper() == "BOOTCAMP"

# 📌 Prueba 6: suma incorrecta (debe fallar)
def test_suma_incorrecta():
    a = 2
    b = 2
    resultado = a + b
    assert resultado == 5

# 📌 Prueba 7: string incorrecto (debe fallar)
def test_string_incorrecto():
    palabra = "bootcamp"
    assert palabra.upper() == "BOOTCAMP123"
