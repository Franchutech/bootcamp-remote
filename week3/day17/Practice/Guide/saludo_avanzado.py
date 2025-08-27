"""
Ejercicio 3 (Nivel AVANZADO):
Crea un programa en Python (📄 Practice/Guide/saludo_avanzado.py)
que reciba desde la terminal un nombre (--nombre), un número de veces (--veces)
y una opción (--modo) que puede ser "normal" o "mayus".

El programa debe:
- Si --modo es "normal": imprimir Hola <nombre>! tantas veces como indique --veces.
- Si --modo es "mayus": imprimir HOLA <NOMBRE>! en mayúsculas tantas veces como indique --veces.
- Usar logging para registrar:
  * Un mensaje INFO indicando el modo y el número de repeticiones.
  * Un mensaje ERROR si --veces <= 0 o si --modo no es válido.
"""

import argparse
import logging

parser = argparse.ArgumentParser(description="Definir programa para Ejercicio Avanzado de nombre con repetición y salvedades")
parser.add_argument("--nombre", type=str, required=True, help="Nombre a imprimir")
parser.add_argument("--veces", type=int, required=True, help="Cantidad de veces:")
parser.add_argument(
    "--modo",
    type=str,
    required=True,
    choices=["normal", "mayus"],
    help="Modo del saludo: normal o mayúscula"
)
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if args.veces <= 0:
    logging.error("El número de repeticiones debe ser mayor a 0")
else:
    logging.info(f"Se imprimirá el saludo en modo: {args.modo} y {args.veces} veces")
    for i in range(args.veces):
        if args.modo == "normal":
            print(f"Hola {args.nombre}!")
        elif args.modo =="mayus":
            print(f"HOLA {args.nombre.upper()}!")
