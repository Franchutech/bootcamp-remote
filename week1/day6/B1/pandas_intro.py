import pandas as pd

# Leer el CSV
df = pd.read_csv("ventas.csv")

# Mostrar las primeras filas
print("📊 Primeras filas del dataset:")
print(df.head())

# Mostrar información general
print("\nℹ️ Información del dataset:")
print(df.info())

# Calcular total de ventas (cantidad * precio)
df["total"] = df["cantidad"] * df["precio"]
print("\n💰 Dataset con columna de total:")
print(df)

df["precio_con_iva"] = df["precio"] * 1.21
print("\n🧾 Dataset con columna de precio con IVA (21%):")
print(df)
