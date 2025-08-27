import argparse

# Creamos el parser de argumentos
parser = argparse.ArgumentParser(description="Calculadora simple con argparse")

# Definimos los parámetros
parser.add_argument("--a", type=int, required=True, help="Primer número")
parser.add_argument("--b", type=int, required=True, help="Segundo número")

# Parseamos los argumentos de la terminal
args = parser.parse_args()

print("Suma:", args.a + args.b)
