"""
📌 pandas_basico.py
Resumen de conceptos básicos de pandas (B1 - Semana 2 Día 8)

Este script incluye:
- Carga de datos desde CSV
- Exploración inicial (head, shape, info, dtypes)
- Selección de columnas
- Uso de loc e iloc
- Filtros con operadores lógicos
- Agrupaciones y estadísticas básicas
"""

import pandas as pd

# ===============================
# 1. Cargar el dataset
# ===============================
df = pd.read_csv("empleados.csv")

# ===============================
# 2. Exploración inicial
# ===============================
print("Primeras filas del dataset:")
print(df.head(), "\n")

print("Dimensiones del dataset (filas, columnas):")
print(df.shape, "\n")

print("Información general:")
print(df.info(), "\n")

print("Tipos de datos:")
print(df.dtypes, "\n")

# ===============================
# 3. Selección de columnas
# ===============================
print("Columna 'nombre':")
print(df["nombre"], "\n")

print("Columnas 'nombre' y 'salario':")
print(df[["nombre", "salario"]], "\n")

# ===============================
# 4. loc vs iloc
# ===============================
print("Con loc (etiqueta índice 2):")
print(df.loc[2], "\n")

print("Con iloc (posición 2):")
print(df.iloc[2], "\n")

# ===============================
# 5. Filtros y operadores lógicos
# ===============================
print("Empleados con edad > 30:")
print(df[df["edad"] > 30], "\n")

print("Empleados del departamento IT:")
print(df[df["departamento"] == "IT"], "\n")

# ===============================
# 6. Agrupaciones y estadísticas
# ===============================
print("Salario promedio general:")
print(df["salario"].mean(), "\n")

print("Salario promedio por departamento:")
print(df.groupby("departamento")["salario"].mean(), "\n")

print("Salario y edad promedio por departamento:")
print(df.groupby("departamento")[["salario", "edad"]].mean(), "\n")
