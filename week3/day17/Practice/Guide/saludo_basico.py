# Ejercicio 2:
# Crea un programa en Python que reciba desde la terminal un nombre y un número de veces, y muestre el saludo repetido tantas veces como el número indique.
# python3 saludo_basico.py --nombre Francella --veces 3
# Requisitos:
     # Argumentos: --nombre (string), --veces (int).
     # Imprimir Hola <nombre>! repetido tantas veces como indique --veces.

import argparse

parser = argparse.ArgumentParser(description="Programar que un nombre se imprima n veces")
parser.add_argument("--nombre", type=str, required=True, help="Nombre a repetir")
parser.add_argument("--veces", type=int, required=True, help="Número de repeticiones")
args = parser.parse_args()

for i in range(args.veces):
    print(f"Hola {args.nombre}!")
          