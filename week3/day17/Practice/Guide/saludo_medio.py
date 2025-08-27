"""
Ejercicio 1 (Nivel MEDIO):
Crea un programa en Python (📄 Practice/Guide/saludo_medio.py),
que reciba desde la terminal un nombre (--nombre) y un número de veces (--veces).

El programa debe:
- Mostrar en pantalla el saludo Hola <nombre>! repetido tantas veces como indique --veces.
- Registrar en logging:
  * Un mensaje INFO indicando cuántas veces se imprimirá el saludo.
  * Un mensaje ERROR si el número de repeticiones es menor o igual a 0 (en ese caso, no imprime saludos).
"""
import argparse
import logging

parser = argparse.ArgumentParser(description="Programar el ejercicio #1 de Nivel Medio")
parser.add_argument("--nombre", type=str, required=True, help="Nombre a repetir")
parser.add_argument("--veces", type=int, required=True, help="Cantidad de repeticiones")
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if args.veces <= 0:
    logging.error("El número de repeticiones debe ser mayor que 0")
else:
    logging.info(f"El saludo se imprimirá {args.veces} veces")
    for i in range(args.veces):
        print(f"Hola {args.nombre}!")