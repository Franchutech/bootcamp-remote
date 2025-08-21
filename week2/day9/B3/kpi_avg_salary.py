import pandas as pd
# Datos de ejemplo
data = {
    "empleado": ["Ana", "Luis", "Marta", "Carlos", "Pedro", "Lucía"],
    "departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "RRHH"],
    "salario": [3000, 3200, 4000, 4200, 4100, 2800]
}

df = pd.DataFrame(data)
print(df)

# KPI 1: Salario promedio general
salario_promedio_general = df["salario"].mean()
print("El salario promedio general es:", salario_promedio_general)

# KPI 2: Salario promedio por departamento
salario_promedio_depto = df.groupby("departamento")["salario"].mean()
print("El salario promedio por departamento es:", salario_promedio_depto)