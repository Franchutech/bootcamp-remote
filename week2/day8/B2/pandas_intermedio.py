# pandas_intermedio.py
# Bootcamp Semana 2 - Día 8 - B2: Limpieza de datos con Pandas

import pandas as pd

# =============================
# 1. ARCHIVOS DE TRABAJO
# =============================
# empleados_limpieza.csv  -> crudo, con nulos y duplicados
# empleados_limpios.csv   -> limpio (nulos tratados y sin duplicados)
# empleados_fechas.csv    -> crudo con fechas mezcladas
# empleados_fechas_limpio.csv -> limpio con fechas normalizadas y enriquecido
# empleados_extendido.csv -> auxiliar con más columnas de fechas

# =============================
# 2. CARGA DE DATOS BASE (con fechas)
# =============================
df = pd.read_csv("empleados_fechas.csv")

print("\n--- INFO INICIAL ---")
print(df.info())
print(df.head())

# =============================
# 3. DUPLICADOS
# =============================
print("\n--- DUPLICADOS ---")
print("Cantidad de duplicados:", df.duplicated().sum())
df = df.drop_duplicates()

# =============================
# 4. NULOS
# =============================
print("\n--- NULOS ---")
df_nulos = df[df["salario"].isnull() | df["edad"].isnull()]
print("Filas con nulos en salario o edad:\n", df_nulos)

# Rellenar valores nulos
df["edad"] = df["edad"].fillna(df["edad"].mean())          # edad → media
df["salario"] = df["salario"].fillna(df["salario"].median())  # salario → mediana
df["departamento"] = df["departamento"].fillna("Sin Asignar")

# =============================
# 5. TIPOS DE DATOS
# =============================
print("\n--- TIPOS DE DATOS ANTES ---")
print(df.dtypes)

# Convertir fecha a datetime
df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce")

print("\n--- TIPOS DE DATOS DESPUÉS ---")
print(df.dtypes)

# =============================
# 6. COLUMNAS DERIVADAS DE FECHAS
# =============================
df["año_ingreso"] = df["fecha_ingreso"].dt.year
df["mes_ingreso"] = df["fecha_ingreso"].dt.month
df["dia_ingreso"] = df["fecha_ingreso"].dt.day
df["dia_semana"] = df["fecha_ingreso"].dt.day_name()
df["antiguedad_años"] = pd.Timestamp.now().year - df["año_ingreso"]

# =============================
# 7. REVISIÓN FINAL
# =============================
print("\n--- INFO FINAL ---")
print(df.info())
print(df.head())

# =============================
# 8. GUARDAR ARCHIVOS
# =============================
# Versión limpia intermedia (solo nulos y duplicados)
df.to_csv("empleados_limpios.csv", index=False)

# Versión final con fechas enriquecidas
df.to_csv("empleados_fechas_limpio.csv", index=False)

print("\n✅ Archivos 'empleados_limpios.csv' y 'empleados_fechas_limpio.csv' creados.")
