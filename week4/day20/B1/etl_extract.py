import pandas as pd
import numpy as np

# Cargar dataset Titanic (directamente desde un CSV público en GitHub)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("\n---Información general del dataset ---")
print(df.info())

print("Primeras 5 filas del dataset original:")
print(df.head())

print("\n--- Últimas 5 filas del dataset:")
print(df.tail())

print("\n--- Dimensiones del dataset (filas, columnas) ---")
print(df.shape)

for col in ["Sex", "Embarked", "Pclass", "Cabin"]:
    print(f"\nColumna: {col}")
    print(f"Total de valores únicos: {df[col].nunique()}")
    print(f"Ejemplos de valores: {df[col].unique()[:10]}")

# --- Exportar dataset crudo a carpeta data ---
df.to_csv("../data/titanic.csv", index=False)
print("Dataset exportado a ../data/titanic.csv")
