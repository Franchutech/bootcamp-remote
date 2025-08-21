import pandas as pd
# Datos de ejemplo
data = {
    "empleado": ["Ana", "Luis", "Marta", "Carlos", "Pedro", "Lucía"],
    "departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "RRHH"],
    "salario": [3000, 3200, 4000, 4200, 4100, 2800]
}

df = pd.DataFrame(data)

print(df)

# KPI: Top 3 empleados con mayor salario
top3 = df.nlargest(3, "salario")

print(top3)