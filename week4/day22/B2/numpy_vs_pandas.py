import pandas as pd
import numpy as np
import time

print("=== CARGA DE DATOS ===")

# 1. Cargar CSV con Pandas
df = pd.read_csv("ventas_np.csv")

print("\nPrimeras filas del dataset:")
print(df.head())

# 2. Convertir columna 'Ventas' a NumPy
ventas_np = df["Ventas"].to_numpy()

# 3. Comparación de cálculos

# --- Python puro (con listas)
ventas_list = df["Ventas"].tolist()

start = time.time()
promedio_python = sum(ventas_list) / len(ventas_list)
end = time.time()
print("\nPromedio (Python puro):", promedio_python, "Tiempo:", round(end - start, 6), "s")

# --- NumPy
start = time.time()
promedio_numpy = np.mean(ventas_np)
end = time.time()
print("Promedio (NumPy):", promedio_numpy, "Tiempo:", round(end - start, 6), "s")

# --- Pandas
start = time.time()
promedio_pandas = df["Ventas"].mean()
end = time.time()
print("Promedio (Pandas):", promedio_pandas, "Tiempo:", round(end - start, 6), "s")

print("\n=== COMPARACIÓN DE MÁS KPIs ===")

# -------------------------------
# Python puro
# -------------------------------
start = time.time()
max_python = max(ventas_list)
min_python = min(ventas_list)
std_python = (sum([(x - promedio_python)**2 for x in ventas_list]) / len(ventas_list))**0.5
crecimiento_python = ((ventas_list[-1] - ventas_list[0]) / ventas_list[0]) * 100
end = time.time()
print("\nPython puro → Tiempo:", round(end - start, 6), "s")
print("Máximo:", max_python, " | Mínimo:", min_python, " | Desviación:", round(std_python, 2), " | Crecimiento:", round(crecimiento_python, 2), "%")

# -------------------------------
# NumPy
# -------------------------------
start = time.time()
max_numpy = np.max(ventas_np)
min_numpy = np.min(ventas_np)
std_numpy = np.std(ventas_np)
crecimiento_numpy = ((ventas_np[-1] - ventas_np[0]) / ventas_np[0]) * 100
end = time.time()
print("\nNumPy → Tiempo:", round(end - start, 6), "s")
print("Máximo:", max_numpy, " | Mínimo:", min_numpy, " | Desviación:", round(std_numpy, 2), " | Crecimiento:", round(crecimiento_numpy, 2), "%")

# -------------------------------
# Pandas
# -------------------------------
start = time.time()
max_pandas = df["Ventas"].max()
min_pandas = df["Ventas"].min()
std_pandas = df["Ventas"].std()
crecimiento_pandas = ((df["Ventas"].iloc[-1] - df["Ventas"].iloc[0]) / df["Ventas"].iloc[0]) * 100
end = time.time()
print("\nPandas → Tiempo:", round(end - start, 6), "s")
print("Máximo:", max_pandas, " | Mínimo:", min_pandas, " | Desviación:", round(std_pandas, 2), " | Crecimiento:", round(crecimiento_pandas, 2), "%")
