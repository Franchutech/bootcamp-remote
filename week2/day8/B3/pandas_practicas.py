import pandas as pd

# ======================
# Cargar dataset base
# ======================
df = pd.read_csv("archivo_practicas.csv")

# ======================
# Ejercicio 1: Lectura y exploración inicial
# ======================
print("\nPrimeras filas:")
print(df.head())
print("\nDimensiones (filas, columnas):")
print(df.shape)
print("\nInformación del DataFrame:")
print(df.info())

# ======================
# Ejercicio 2: Selección de filas y columnas
# ======================
print("\nColumna 'nombre':")
print(df["nombre"].head())
print("\nColumnas 'departamento' y 'salario':")
print(df[["departamento", "salario"]].head())

# ======================
# Ejercicio 3: Filtrado por condición
# ======================
print("\nEmpleados con salario > 4000:")
print(df.loc[df["salario"] > 4000])

# ======================
# Ejercicio 4: Ordenación
# ======================
print("\nEmpleados ordenados por salario descendente y edad descendente:")
print(df.sort_values(by=["salario", "edad"], ascending=[False, False]).head())

# ======================
# Ejercicio 5: Estadísticas descriptivas
# ======================
print("\nPromedio y mediana de edad:")
print("Promedio:", df["edad"].mean(), " | Mediana:", df["edad"].median())
print("\nEstadísticas generales:")
print(df.describe(include="all"))

# ======================
# Ejercicio 6: Manejo de nulos
# ======================
print("\nConteo de valores nulos por columna:")
print(df.isnull().sum())
print("\nRellenar nulos en 'ciudad' con 'Desconocido':")
print(df.fillna({"ciudad": "Desconocido"}).head())

# ======================
# Ejercicio 7: Eliminación de duplicados
# ======================
print("\nCantidad de filas antes y después de eliminar duplicados:")
print(len(df), "→", len(df.drop_duplicates()))

# ======================
# Ejercicio 8: Crear nueva columna
# ======================
df["edad_5años"] = df["edad"] + 5
print("\nColumna 'edad_5años' agregada:")
print(df[["nombre", "edad", "edad_5años"]].head())

# ======================
# Ejercicio 9: Conversión de tipos
# ======================
df["edad"] = df["edad"].astype(float)
df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"])
print("\nTipos de datos tras conversión:")
print(df.dtypes)

# ======================
# Ejercicio 10: Operaciones con fechas
# ======================
df["mes_ingreso"] = df["fecha_ingreso"].dt.month
print("\nColumna 'mes_ingreso':")
print(df[["nombre", "fecha_ingreso", "mes_ingreso"]].head())

# ======================
# Ejercicio 11: Agrupación
# ======================
print("\nEdad promedio por ciudad:")
print(df.groupby("ciudad")["edad"].mean())

# ======================
# Ejercicio 12: Agregaciones
# ======================
print("\nEdad mínima, máxima y promedio por ciudad:")
print(df.groupby("ciudad")["edad"].agg(["min", "max", "mean"]))

# ======================
# Ejercicio 13: Tablas dinámicas
# ======================
print("\nEdad promedio por departamento y ciudad:")
print(pd.pivot_table(df, values="edad", index="departamento", columns="ciudad", aggfunc="mean"))

# ======================
# Ejercicio 14: Concatenar DataFrames
# ======================
costo_vida = pd.DataFrame({
    "ciudad": ["Málaga", "Santander", "Madrid", "Zaragoza", "Bilbao"],
    "costo": [1200, 1300, 1000, 1400, 1250]
})
df = pd.merge(df, costo_vida, on="ciudad", how="left")
print("\nMerge con costo de vida:")
print(df.head())

# ======================
# Ejercicio 15: Concatenación de nuevos empleados
# ======================
nuevos_empleados = pd.DataFrame({
    "id_empleado": [4256, 3265],
    "nombre": ["Francella Rojas", "Wendy Villagra"],
    "edad": [37, 46],
    "departamento": ["IT", "Marketing"],
    "salario": [3000, 2800],
    "ciudad": ["Santander", "Santander"],
    "fecha_ingreso": ["2025-08-29", "2025-09-29"]
})
nuevos_empleados["fecha_ingreso"] = pd.to_datetime(nuevos_empleados["fecha_ingreso"])
df_total = pd.concat([df, nuevos_empleados], ignore_index=True)

# Recalcular columnas
df_total["edad_5años"] = df_total["edad"] + 5
df_total["mes_ingreso"] = df_total["fecha_ingreso"].dt.month

print("\nDataFrame tras concatenar nuevos empleados:")
print(df_total.tail())

# ======================
# Ejercicio 16: Apply + lambda
# ======================
df_total["categoria_edad"] = df_total["edad"].apply(
    lambda x: "Senior" if x > 40 else ("Adulto" if x > 30 else "Joven")
)
print("\nCategoría de edad añadida:")
print(df_total[["nombre", "edad", "categoria_edad"]].tail())

# ======================
# Ejercicio 17: Exportar resultados
# ======================
df_total.to_csv("pandas_practicas_final.csv", index=False)
df_total.to_excel("pandas_practicas_final.xlsx", index=False)
print("\nArchivo exportado: pandas_practicas_final.csv y .xlsx")

# ======================
# Ejercicio 18: Indexación avanzada
# ======================
print("\nEmpleados de Marketing menores de 30 años:")
print(df_total.loc[(df_total["departamento"] == "Marketing") & (df_total["edad"] < 30), ["nombre", "departamento", "edad"]])

# ======================
# Ejercicio 19: Iteración sobre filas
# ======================
print("\nIteración sobre empleados (solo 3 ejemplos):")
for i, row in df_total.head(3).iterrows():
    print(f"{row['nombre']} trabaja en {row['departamento']} con salario {row['salario']}")

# ======================
# Ejercicio 20: Mini-proyecto (resumen)
# ======================
print("\nEdad promedio de todos los empleados:", df_total["edad"].mean())
print("\nEmpleado más joven:")
print(df_total.loc[df_total["edad"].idxmin(), ["nombre", "edad", "departamento"]])
print("\nCantidad de empleados por categoría de edad:")
print(df_total["categoria_edad"].value_counts())
