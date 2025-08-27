# Ejercicio 1:
# Crea un programa en Python que reciba desde la terminal un nombre y muestre un saludo.

import argparse

parser = argparse.ArgumentParser(description="Programar Saludo")
parser.add_argument("--nombre", type=str, required=True, help="Tu nombre es:")
args= parser.parse_args()

print(f"Tu nombre es {args.nombre}")