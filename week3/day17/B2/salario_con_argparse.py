# salario_con_argparse.py
import argparse

# Datos de ejemplo
salarios = {
    "IT": [3000, 4000, 3500],
    "HR": [2000, 2200, 2500],
    "Ventas": [1500, 1800, 2100]
}

# Configuramos argparse
parser = argparse.ArgumentParser(description="Calcula el salario promedio de un departamento")
parser.add_argument("--dep", type=str, required=True, choices=salarios.keys(), help="Nombre del departamento")

args = parser.parse_args()

# Calculamos promedio
promedio = sum(salarios[args.dep]) / len(salarios[args.dep])
print(f"El salario promedio en {args.dep} es {promedio}")
