"""
==========================================================
NUMPY vs PANDAS — COMPARISON SUMMARY (Day 22 - Bootcamp)
==========================================================

Este script muestra un caso práctico de:
1. Uso de funciones matemáticas avanzadas en NumPy.
2. Comparación de rendimiento entre Python puro, NumPy y Pandas.
3. Ventajas de Pandas para análisis tabular (groupby).
4. Conclusión: cuándo conviene usar cada uno.

Dataset: ventas.csv (5840 filas, columnas: Fecha, Región, Producto, Ventas, Costos)
Ubicación: week4/day22/B2/ventas.csv
"""

import pandas as pd
import numpy as np
import time

# ==========================================================
# 1. FUNCIONES MATEMÁTICAS AVANZADAS (NUMPY)
# ==========================================================
print("=== FUNCIONES MATEMÁTICAS AVANZADAS (NUMPY) ===")

data = np.array([1, 4, 9, 16, 25])
print("Array:", data)
print("Raíz cuadrada:", np.sqrt(data))
print("Promedio:", np.mean(data))
print("Desviación estándar:", np.std(data))
print("Exponencial:", np.exp(data))
print("Logaritmo natural:", np.log(data))

# ==========================================================
# 2. COMPARACIÓN DE RENDIMIENTO
# ==========================================================
print("\n=== COMPARACIÓN PYTHON PURO vs NUMPY vs PANDAS ===")

# Cargar dataset real
df = pd.read_csv("../B2/ventas.csv")
ventas_list = df["Ventas"].tolist()
ventas_np = df["Ventas"].to_numpy()

# --- Python puro
start = time.time()
prom_python = sum(ventas_list) / len(ventas_list)
max_python = max(ventas_list)
min_python = min(ventas_list)
std_python = (sum([(x - prom_python)**2 for x in ventas_list]) / len(ventas_list))**0.5
crec_python = ((ventas_list[-1] - ventas_list[0]) / ventas_list[0]) * 100
end = time.time()
print("\nPython puro → Tiempo:", round(end - start, 6), "s")
print("Promedio:", prom_python, "| Máximo:", max_python, "| Mínimo:", min_python,
      "| Desviación:", round(std_python, 2), "| Crecimiento:", round(crec_python, 2), "%")

# --- NumPy
start = time.time()
prom_numpy = np.mean(ventas_np)
max_numpy = np.max(ventas_np)
min_numpy = np.min(ventas_np)
std_numpy = np.std(ventas_np)
crec_numpy = ((ventas_np[-1] - ventas_np[0]) / ventas_np[0]) * 100
end = time.time()
print("\nNumPy → Tiempo:", round(end - start, 6), "s")
print("Promedio:", prom_numpy, "| Máximo:", max_numpy, "| Mínimo:", min_numpy,
      "| Desviación:", round(std_numpy, 2), "| Crecimiento:", round(crec_numpy, 2), "%")

# --- Pandas
start = time.time()
prom_pandas = df["Ventas"].mean()
max_pandas = df["Ventas"].max()
min_pandas = df["Ventas"].min()
std_pandas = df["Ventas"].std()
crec_pandas = ((df["Ventas"].iloc[-1] - df["Ventas"].iloc[0]) / df["Ventas"].iloc[0]) * 100
end = time.time()
print("\nPandas → Tiempo:", round(end - start, 6), "s")
print("Promedio:", prom_pandas, "| Máximo:", max_pandas, "| Mínimo:", min_pandas,
      "| Desviación:", round(std_pandas, 2), "| Crecimiento:", round(crec_pandas, 2), "%")

# ==========================================================
# 3. AGRUPACIONES (VENTAJA DE PANDAS)
# ==========================================================
print("\n=== AGRUPACIONES (PANDAS) ===")

# Promedio de ventas y costos por región
region_summary = df.groupby("Region")[["Ventas", "Costos"]].mean().round(2)
print("\nPromedio de ventas y costos por Región:")
print(region_summary)

# Total de ventas por producto
producto_summary = df.groupby("Producto")["Ventas"].sum()
print("\nTotal de ventas por Producto:")
print(producto_summary)

# ==========================================================
# 4. CONCLUSIÓN (COMENTARIOS)
# ==========================================================
"""
CONCLUSIONES — Día 22 (B1-B3)

- NumPy:
  ✔ Potente en operaciones numéricas a gran escala.
  ✔ Ideal cuando se manejan millones de datos numéricos puros.
  ✘ No gestiona datos tabulares con categorías (texto, fechas).

- Pandas:
  ✔ Más práctico y legible para análisis tabular (como Excel).
  ✔ Permite agrupaciones, filtros, merges, joins.
  ✔ Internamente usa NumPy, así que mantiene buen rendimiento.
  ✘ No es tan rápido como NumPy en operaciones puramente numéricas.

- Python puro:
  ✔ Útil para entender la lógica básica.
  ✘ Poco eficiente y poco legible en datasets grandes.

Resumen:
NumPy = Ferrari para cálculos numéricos 🏎️
Pandas = coche familiar cómodo para tablas 🚗
Python puro = caminar 🚶
"""
