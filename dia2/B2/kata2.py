# Kata 2
secreto = 7
while True:
    entrada = input("Adivina el número secreto (usa 0 para salir en cualquier momento): ")
    if not entrada.isdigit():
        print("Por favor escribe un número")
        continue
    numero = int(entrada)
    if numero == 0:
        print("Juego Terminado")
        break
    if numero == secreto:
        print("FELICIDADES HAS ACERTADO")
        break
    else:
        print("Incorrecto prueba otro numero")

