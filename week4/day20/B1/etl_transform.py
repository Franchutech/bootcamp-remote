import pandas as pd

# --- Cargar dataset original ---
# Subimos un nivel desde B1 y vamos a /data
df = pd.read_csv("../data/titanic.csv")

print("Dataset cargado. Filas y columnas:", df.shape)

# ==========================================================
# TRANSFORMACIONES DE LIMPIEZA
# ==========================================================

# --- 1. Normalización de Sex ---
print("\nValores únicos de Sex antes de normalizar:")
print(df["Sex"].unique())

df["Sex"] = df["Sex"].str.capitalize()

print("\nValores únicos de Sex después de normalizar:")
print(df["Sex"].unique())


# --- 2. Normalización de Embarked ---
print("\nValores únicos de Embarked antes de limpiar:")
print(df["Embarked"].unique())

# Diccionario de reemplazo
embarked_map = {
    "S": "Southampton",
    "C": "Cherbourg",
    "Q": "Queenstown"
}

# Reemplazar iniciales por nombres completos
df["Embarked"] = df["Embarked"].map(embarked_map)

# Imputar nulos con la moda (valor más frecuente)
moda_embarked = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(moda_embarked)

print("\nValores únicos de Embarked después de limpiar:")
print(df["Embarked"].unique())
print("Nulos restantes en Embarked:", df["Embarked"].isnull().sum())


# --- 3. Normalización de Pclass ---
# TODO: crear columna Pclass_Label con 'First Class','Second Class','Third Class'

# --- 3. Normalización de Pclass ---
print("\nValores únicos de Pclass antes de crear etiquetas:")
print(df["Pclass"].unique())

# Diccionario de etiquetas
pclass_map = {
    1: "First Class",
    2: "Second Class",
    3: "Third Class"
}

# Crear nueva columna con etiquetas
df["Pclass_Label"] = df["Pclass"].map(pclass_map)

print("\nValores únicos de Pclass_Label creados:")
print(df["Pclass_Label"].unique())


# --- 4. Limpieza de Age ---
# TODO: imputar nulos con valores simulados coherentes (según Name, Parch, SibSp)

# --- 4. Limpieza de Age ---
print("\nResumen de Age antes de imputar:")
print(df["Age"].describe())
print("Nulos en Age:", df["Age"].isnull().sum())

# --- 4. Limpieza de Age ---

import numpy as np

# Extraer título del nombre
df["Title"] = df["Name"].str.extract(r",\s*([^\.]*)\.")

print("\nTítulos detectados en Name:")
print(df["Title"].value_counts())

# Función para imputar edades según título
def impute_age(row):
    if pd.notnull(row["Age"]):
        return row["Age"]  # conservar si ya tiene edad
    
    title = row["Title"]
    if title == "Master":
        return np.random.randint(0, 15)  # niño
    elif title == "Miss":
        return np.random.randint(15, 26) # adolescente/joven
    elif title == "Mrs":
        return np.random.randint(20, 41) # adulta
    elif title == "Mr":
        return np.random.randint(18, 61) # adulto
    else:
        return df["Age"].median()  # fallback a la mediana

# Aplicar la función fila por fila
df["Age"] = df.apply(impute_age, axis=1)

print("\nResumen de Age después de imputar:")
print(df["Age"].describe())
print("Nulos restantes en Age:", df["Age"].isnull().sum())

# --- 5. Limpieza de Cabin ---
# TODO: imputar nulos con 'Unknown' o valores simulados
# TODO: crear columna Deck con la primera letra de la cabina

# --- 5. Limpieza de Cabin ---

import numpy as np

# Extraer la primera letra de la cabina (Deck)
df["Deck"] = df["Cabin"].astype(str).str[0]

print("\nValores únicos de Deck antes de imputar:")
print(df["Deck"].value_counts(dropna=False))

# Definir cubiertas posibles según la clase (basado en datos históricos)
deck_options = {
    1: ["A", "B", "C", "D", "E"],   # Primera clase
    2: ["D", "E", "F"],             # Segunda clase
    3: ["E", "F", "G"]              # Tercera clase
}

# Función para imputar Deck respetando la clase del pasajero
def impute_deck(row):
    if row["Deck"] == "n":  # los NaN se volvieron "nan" → primera letra = "n"
        return np.random.choice(deck_options[row["Pclass"]])
    return row["Deck"]

# Aplicar la imputación
df["Deck"] = df.apply(impute_deck, axis=1)

print("\nValores únicos de Deck después de imputar:")
print(df["Deck"].value_counts())
print("Nulos restantes en Deck:", df["Deck"].isnull().sum())

# ==========================================================
# CABIN — Análisis espacial y variables derivadas
# ==========================================================

# 1. Extraer número de cabina
df["Cabin_Number"] = df["Cabin"].str.extract(r"(\d+)", expand=False).astype(float)

print("\nEjemplos de Cabin_Number extraído:")
print(df[["Cabin", "Cabin_Number"]].head(10))

# 2. Ubicación longitudinal (Proa ↔ Popa)
# Regla: números bajos → Forward (proa), números altos → Aft (popa)
df["Location_Longitude"] = df["Cabin_Number"].apply(
    lambda x: "Forward" if pd.notnull(x) and x < 50 else ("Aft" if pd.notnull(x) else "Unknown")
)

# 3. Ubicación lateral (Babor ↔ Estribor)
# Regla: pares = Port (babor), impares = Starboard (estribor)
df["Location_Lateral"] = df["Cabin_Number"].apply(
    lambda x: "Port" if pd.notnull(x) and x % 2 == 0 else ("Starboard" if pd.notnull(x) else "Unknown")
)

# 4. Acceso a lanchas salvavidas
# Regla: solo los pasajeros en Boat Deck tenían lanchas directamente
df["Has_Lifeboat_Access"] = df["Deck"].apply(lambda x: True if x == "B" else False)

print("\nEjemplos de nuevas columnas derivadas de Cabin:")
print(df[["Cabin", "Deck", "Cabin_Number", "Location_Longitude", "Location_Lateral", "Has_Lifeboat_Access"]].head(15))

# ==========================================================
# 5B. Imputación de Cabin_Number antes de derivar ubicaciones
# ==========================================================

# Rango aproximado de cabinas por Deck (basado en historia y dataset)
deck_ranges = {
    "A": (1, 40),
    "B": (1, 100),
    "C": (1, 150),
    "D": (1, 200),
    "E": (1, 200),
    "F": (1, 100),
    "G": (1, 60),
    "T": (1, 10)  # solo un registro en el dataset
}

# Extraer número de cabina (si existe)
df["Cabin_Number"] = df["Cabin"].str.extract(r"(\d+)", expand=False).astype(float)

# Imputar nulos con rango correspondiente al Deck
def impute_cabin_number(row):
    if pd.notnull(row["Cabin_Number"]):
        return row["Cabin_Number"]
    deck = row["Deck"]
    if deck in deck_ranges:
        return np.random.randint(deck_ranges[deck][0], deck_ranges[deck][1] + 1)
    return np.nan

df["Cabin_Number"] = df.apply(impute_cabin_number, axis=1)

print("\nEjemplos de Cabin_Number después de imputar:")
print(df[["Cabin", "Deck", "Cabin_Number"]].head(15))

# ==========================================================
# Recalcular ubicaciones después de imputar Cabin_Number
# ==========================================================

# Ubicación longitudinal (Proa ↔ Popa)
df["Location_Longitude"] = df["Cabin_Number"].apply(
    lambda x: "Forward" if x < 50 else "Aft"
)

# Ubicación lateral (Babor ↔ Estribor)
df["Location_Lateral"] = df["Cabin_Number"].apply(
    lambda x: "Port" if x % 2 == 0 else "Starboard"
)

print("\nEjemplos después de recalcular ubicaciones:")
print(df[["Cabin", "Deck", "Cabin_Number", "Location_Longitude", "Location_Lateral"]].head(20))

# ==========================================================
# Has_Lifeboat_Access (proximidad a botes salvavidas)
# ==========================================================

# Por simplicidad: solo los pasajeros en Boat Deck tendrían acceso directo.
# Como el dataset no tiene Boat, asumimos que Deck A y B tenían la mayor cercanía.
df["Has_Lifeboat_Access"] = df["Deck"].apply(lambda x: True if x in ["A", "B"] else False)

print("\nEjemplos de Has_Lifeboat_Access:")
print(df[["Cabin", "Deck", "Has_Lifeboat_Access"]].head(20))

# --- 6. Limpieza de otras columnas ---
# TODO: crear columna FamilySize = SibSp + Parch + 1
# --- 6. Limpieza de otras columnas ---

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

print("\nEjemplos de FamilySize:")
print(df[["SibSp", "Parch", "FamilySize"]].head(10))

# --- 7. Guardar dataset limpio ---
# TODO: exportar a 'titanic_clean.csv'

# --- 7. Guardar dataset limpio ---
df.to_csv("../data/titanic_clean.csv", index=False)

print("\nDataset limpio guardado en ../data/titanic_clean.csv")
