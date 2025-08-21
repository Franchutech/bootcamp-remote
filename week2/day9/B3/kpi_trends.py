import pandas as pd

# Datos de ejemplo con fechas
data = {
    "empleado": ["Ana", "Luis", "Marta", "Carlos", "Pedro", "Lucía"],
    "fecha": [
        "2025-01-10", "2025-01-15",
        "2025-02-05", "2025-02-20",
        "2025-03-10", "2025-03-15"
    ],
    "salario": [3000, 3200, 4000, 4200, 4100, 2800]
}

df = pd.DataFrame(data)

# Convertir la columna 'fecha' a formato de fecha real
df["fecha"] = pd.to_datetime(df["fecha"])

print("Tabla de empleados con fechas:")
print(df)

# KPI: Salario promedio por mes
tendencia_mensual = df.groupby(df["fecha"].dt.to_period("M"))["salario"].mean()

print(tendencia_mensual)